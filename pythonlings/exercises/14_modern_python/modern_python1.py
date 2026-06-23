"""
f-strings support format specs after a colon: f"{value:.2f}" for 2 decimal places,
f"{name:-<10}" to left-pad with dashes to width 10. Expressions work too: f"{len(items)} items".
Format spec syntax: {value:[[fill]align][width][.precision][type]}

Fix formatted, padded, and count to produce the expected strings.
"""

# I AM NOT DONE


name = "Ada"
value = 3.14159
items = [1, 2, 3]

formatted = f"{value}"
padded = f"{name}"
count = f"{items}"
