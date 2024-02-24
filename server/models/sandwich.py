from typing import Any, Dict
from pydantic import BaseModel
from .price_history import Price_history
from datetime import datetime


class Sandwich(BaseModel):
    """Pydantic Class containing sandwich data"""

    name: str

    # optional sandwich description
    description: str | None = None

    # price history in a candlestick format
    price_history: Price_history | None = Price_history.generate_history(
        datetime(2020, 1, 1), datetime.now()
    )

    # total stocks
    volume: int | None = 0

    # total available
    on_sale: int | None = volume

    # latest price
    price: int | None = price_history.close[-1]

    # # TODO try to make this work with pydantic fields later
    # @property
    # def price(self) -> int:
    #     """Get latest stock price

    #     Returns:
    #         int: current stock price
    #     """
    #     # latest price
    #     return self.price_history.close[-1]

    # overwrite pydantic function to serialize price property
    # def model_dump(
    #     self,
    #     *,
    #     mode: str = "python",
    #     include: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
    #     exclude: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
    #     by_alias: bool = False,
    #     exclude_unset: bool = False,
    #     exclude_defaults: bool = False,
    #     exclude_none: bool = False,
    #     round_trip: bool = False,
    #     warnings: bool = True
    # ) -> Dict[str, Any]:
    #     d = super().model_dump(
    #         mode=mode,
    #         include=include,
    #         exclude=exclude,
    #         by_alias=by_alias,
    #         exclude_unset=exclude_unset,
    #         exclude_defaults=exclude_defaults,
    #         exclude_none=exclude_none,
    #         round_trip=round_trip,
    #         warnings=warnings,
    #     )
    #     d["price"] = self.price
    #     return d
