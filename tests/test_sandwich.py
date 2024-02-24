import sys
from datetime import datetime

sys.path.append("../")
from server.models import Sandwich, Price_history


def test_sandwich() -> None:

    sandwich = Sandwich(
        name="McDonald's McRib",
        price_history=Price_history.generate_history(
            datetime(2020, 1, 1), datetime.now()
        ),
        volume=2000,
        on_sale=500,
    )

    assert sandwich.model_dump()["price"] == sandwich.price
    assert sandwich.price == sandwich.price_history.close[-1]
    assert type(sandwich.price_history.x[0]) is datetime
