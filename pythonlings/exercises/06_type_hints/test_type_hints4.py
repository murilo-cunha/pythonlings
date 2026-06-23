from typing import get_type_hints
from type_hints4 import Movie


def test_hints():
    hints = get_type_hints(Movie)
    assert hints == {"title": str, "year": int, "rating": float}

def test_usage():
    m: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
    assert m["title"] == "Inception"
    assert m["year"] == 2010
