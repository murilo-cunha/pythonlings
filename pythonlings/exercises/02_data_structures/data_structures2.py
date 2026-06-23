"""
Dicts map keys to values. Use dict[key] = value to add or update, del dict[key]
to remove a key, and dict.get(key, default) to safely read — returning a default
instead of raising KeyError when the key is absent.

Update prices["banana"] to 0.79 and delete the "cherry" key with del prices["cherry"]; leave "apple" at 0.99. Then set mango_price = prices.get("mango", 0.0) so it safely reads the absent "mango" key and yields the default 0.0.
"""

# I AM NOT DONE


prices = {"apple": 0.99, "banana": 0.59, "cherry": 2.99}
mango_price = 0.0
