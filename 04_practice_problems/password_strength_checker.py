#checking password strength using loops and conditions

password = "Arpita@123"

has_upper=False
has_lower=False
has_digit=False
has_special=False

special_chars = "!@#$%^&*()_+-="

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit=True
    elif ch in special_chars:
        has_special=True

strength = 0
if has_upper:
    strength += 1
if has_lower:
    strength += 1
if has_digit:
    strength += 1
if has_special:
    strength += 1

if strength >=3:
    print("Strong password...")
else:
    print("weak password...")