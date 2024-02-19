from pydantic import BaseModel


class Sandwich(BaseModel):
    """Pydantic Class containing sandwich data"""

    name: str
    price: int

    # TODO implement price history
    price_data: object | None = None
