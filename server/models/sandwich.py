from pydantic import BaseModel
from .price_history import Price_history


class Sandwich(BaseModel):
    """Pydantic Class containing sandwich data"""

    name: str

    price_history: Price_history | None = None

    @property
    def price(self) -> int:
        """Get latest stock price

        Returns:
            int: current stock price
        """

        return self.price_history.close[-1]
