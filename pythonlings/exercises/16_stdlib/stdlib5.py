# I AM NOT DONE

import re

text = "Contact us at support@example.com or sales@company.org"

# Fix: find all email addresses in text using re.findall()
emails = []  # Fix: use re.findall() with a pattern matching word@word.word

# Fix: replace all digits in the string below with "X" using re.sub()
masked = "Order #12345 ref #678"  # Fix: use re.sub()

# Fix: extract the area code from a US phone number using re.search()
phone = "(555) 867-5309"
area_code = ""  # Fix: use re.search() with a capturing group to extract the digits

# DON'T EDIT THE TESTS
assert "support@example.com" in emails
assert "sales@company.org" in emails
assert len(emails) == 2

assert masked == "Order #XXXXX ref #XXX"

assert area_code == "555"
