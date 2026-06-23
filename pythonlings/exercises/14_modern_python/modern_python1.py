"""
f-strings support format specs after a colon: f"{value:.2f}" for 2 decimal places,
f"{name:->10}" to left-pad with dashes to width 10. Expressions work too: f"{len(items)} items".
Format spec syntax: {value:[[fill]align][width][.precision][type]}

Set formatted = f"{value:.2f}" so it equals "3.14", padded = f"{name:->10}" so it equals "-------Ada" (Ada right-aligned to width 10, dashes on the left), and count = f"{len(items)} items" so it equals "3 items".
"""

# I AM NOT DONE


name = "Ada"
value = 3.14159
items = [1, 2, 3]

formatted = f"{value}"
padded = f"{name}"
count = f"{items}"
