from pydantic import BaseModel
from .price_history import Price_history


class Sandwich(BaseModel):
    """Pydantic Class containing sandwich data"""

    name: str

    # optional sandwich description
    description: str | None = None

    # price history in a candlestick format
    price_history: Price_history | None = None

    # total stocks
    volume: int | None = 0

    # total available
    on_sale: int | None = volume

    @property
    def price(self) -> int:
        """Get latest stock price

        Returns:
            int: current stock price
        """

        return self.price_history.close[-1]
