import random
import requests
from bs4 import BeautifulSoup
import json,re
class MoaktEmailHandler:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://moakt.com/en"
        self.email = None

    def create_random_email(self):
        """
        Sends the first request to create a random email address.
        """
        url = f"{self.base_url}/inbox"
        data = {
            'domain': 'teml.net',
            'username': '',
            'random': 'Get a Random Address',
            'preferred_domain': 'moakt.co'
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://moakt.com',
            'referer': 'https://moakt.com/en',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

        # Send the request to create a random email address
        response = self.session.post(url, data=data, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to create a random email address.")

        # Fetch the email address from the next request
        self.fetch_email()

    def fetch_email(self):
        """
        Fetches the email address by making the second request.
        """
        url = f"{self.base_url}/inbox"
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://moakt.com/en',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

        response = self.session.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch email inbox.")

        soup = BeautifulSoup(response.text, 'html.parser')
        email_div = soup.find('div', {'id': 'email-address'})
        if email_div:
            self.email = email_div.text.strip()
        else:
            raise Exception("Failed to extract email address.")

    def random_capitalize_domain(self, email):
        """
        Randomly capitalizes the domain of the email address.
        """
        user, domain = email.split('@')
        domain_parts = domain.split('.')
        capitalized_domain = '.'.join(
            ''.join(random.choice([c.upper(), c.lower()]) for c in part)
            for part in domain_parts
        )
        return f"{user}@{capitalized_domain}"

    def check_messages(self):
        """
        Checks the inbox for messages and extracts the verification code.
        """
        url = f"{self.base_url}/inbox"
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'referer': 'https://moakt.com/en',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }

        response = self.session.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch email inbox.")

        soup = BeautifulSoup(response.text, 'html.parser')
        email_message_list = soup.find('div', {'id': 'email_message_list'})
        if email_message_list:
            # Find all <a> tags inside the email list
            all_links = email_message_list.find_all('a')

            for a_tag in all_links:
                if "Confirmer votre adresse e-mail" in a_tag.get_text(strip=True):
                    href = a_tag.get('href')

                    break
        response = self.session.get("https://moakt.com" + href + "/content/", headers=headers)
        pattern = r'href="(http://link\.vizzit\.com/ls/click\?upn=[^"]+)"'
        matches = re.findall(pattern, response.text)





        return matches[0]

# Example Usage
# if __name__ == "__main__":
#     handler = MoaktEmailHandler()

#     try:
#         # Step 1: Create a random email
#         handler.create_random_email()
#         print("Generated Email:", handler.email)

#         # Step 2: Randomly capitalize the email domain
#         email_with_capitalized_domain = handler.random_capitalize_domain(handler.email)
#         print("Email with Randomized Capitalization:", email_with_capitalized_domain)

#         # Step 3: Check for messages and extract the verification code
#         verification_code = handler.check_messages()
#         if verification_code:
#             print("Verification Code:", verification_code)
#         else:
#             print("No verification code found.")
#     except Exception as e:
#         print("Error:", e)


# if __name__ == "__main__":
#     with open('test.html', 'r', encoding="utf-8") as file:

#         soup = BeautifulSoup(file, 'html.parser')
#         email_message_list = soup.find('div', {'id': 'email_message_list'})
#         # print(email_message_list)

#         print(soup2.text[0:6])