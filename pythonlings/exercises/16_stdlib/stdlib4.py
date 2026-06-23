"""
json.dumps(obj) serialises Python to a JSON string. json.loads(s) parses it back.
Python True/False/None become JSON true/false/null automatically.
Add indent=2 to json.dumps() for human-readable pretty-printed output.

Fix json_str, restored, and pretty using json.dumps() and json.loads().
"""

# I AM NOT DONE

import json

data = {"name": "Ada", "scores": [95, 87, 92], "active": True}

json_str = ""
restored = {}
pretty = ""
