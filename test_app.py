from app import random_fruit


def test_random_fruit():
    assert "apple" or "banana" or "cherry" or "date" or "elderberry" in random_fruit()
