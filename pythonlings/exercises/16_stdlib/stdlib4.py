# I AM NOT DONE

import json

data = {"name": "Ada", "scores": [95, 87, 92], "active": True}

# Fix: serialize data to a JSON string (compact, no extra whitespace)
json_str = ""  # Fix: use json.dumps()

# Fix: deserialize the JSON string back to a Python dict
restored = {}  # Fix: use json.loads()

# Fix: pretty-print with 2-space indent
pretty = ""  # Fix: use json.dumps() with indent=2

# DON'T EDIT THE TESTS
assert json_str == '{"name": "Ada", "scores": [95, 87, 92], "active": true}'
assert restored == data
assert isinstance(restored["scores"], list)
assert pretty.startswith("{\n  ")
