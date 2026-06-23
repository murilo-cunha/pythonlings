"""
re.findall(pattern, text) returns all non-overlapping matches as a list.
re.sub(pattern, repl, text) replaces every match with repl.
Use a capturing group (...) with re.search(...).group(1) to extract a part of a match.

Fix emails (findall), masked (sub replacing digits with X), and area_code (search with group).
"""

# I AM NOT DONE

import re

text = "Contact us at support@example.com or sales@company.org"

emails = []

masked = "Order #12345 ref #678"

phone = "(555) 867-5309"
area_code = ""
