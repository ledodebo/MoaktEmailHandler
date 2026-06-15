# Moakt Email Handler

A lightweight Python wrapper for interacting with **Moakt** temporary email inboxes.

## Features

* 📧 Generate a random disposable email address
* 📥 Retrieve the generated inbox automatically
* 🔍 Parse incoming emails using BeautifulSoup
* 🔗 Extract verification links from received messages
* 🎲 Randomize email domain capitalization for testing email validation edge cases
* 🍪 Maintains a persistent session for seamless inbox access

## Installation

```bash
pip install requests beautifulsoup4
```

## Usage

```python
from moakt import MoaktEmailHandler

handler = MoaktEmailHandler()

handler.create_random_email()
print(handler.email)

link = handler.check_messages()
print(link)
```

## Methods

### `create_random_email()`

Creates a new temporary email address and stores it in `handler.email`.

### `fetch_email()`

Fetches the currently assigned inbox email.

### `random_capitalize_domain(email)`

Returns the same email address with randomly capitalized domain characters.

Example:

```
john@TeMl.NeT
```

Useful for testing applications that incorrectly perform case-sensitive email validation.

### `check_messages()`

Checks the inbox for incoming emails and extracts the target verification link from supported messages.

## Requirements

* Python 3.8+
* requests
* beautifulsoup4

## Disclaimer

This project is intended for educational purposes, automated testing, and development workflows. Ensure your use complies with the Terms of Service of any websites or services you interact with.
