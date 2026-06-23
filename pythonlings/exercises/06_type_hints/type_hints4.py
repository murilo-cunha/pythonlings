# I AM NOT DONE

from typing import TypedDict


class Movie(TypedDict):
    # Fix: add three fields with correct types:
    #   title: str
    #   year: int
    #   rating: float
    pass


# DON'T EDIT THE TESTS
from typing import get_type_hints

hints = get_type_hints(Movie)
assert hints == {"title": str, "year": int, "rating": float}

m: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
assert m["title"] == "Inception"
assert m["year"] == 2010
