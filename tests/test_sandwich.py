import sys
from datetime import datetime

sys.path.append("../")
from server.models import Sandwich, Price_history


def test_sandwich() -> None:
    price_history = Price_history(
        x=["2024-02-01", "2024-02-02", "2024-02-03", "2024-02-04"],
        open=[110, 120, 135, 130],
        high=[150, 125, 140, 135],
        low=[100, 105, 110, 100],
        close=[120, 110, 130, 115],
    )

    sandwich = Sandwich(name="McDonald's McRib", price_history=price_history)

    assert sandwich.price == 115
    assert type(sandwich.price_history.x[0]) is datetime
