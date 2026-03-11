# regex_basics.py
# Demonstrating basic regular expressions in Python

import re

# Email pattern
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

emails = [
    "user@example.com",
    "partner.dev@gmail.com",
    "invalid-email@",
    "test@domain"
]

for email in emails:
    if re.match(pattern, email):
        print(email, "-> Valid Email ")
    else:
        print(email, "-> Invalid Email ")