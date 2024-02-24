from __future__ import annotations
from typing_extensions import Literal
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Any, Callable, List
from random import randint, choice

from pydantic_core import PydanticUndefined


def adjust(self, intervals: str, cutoff: int) -> dict:
    """Candlestick graph index interval adjustment script. Should not
    be used outside this module"""

    x = []
    open_list = []
    close = []
    high = []
    low = []

    # define interval as amount of quarters of hour
    match intervals:
        case "hour":
            intervals = 4
        case "day":
            intervals = 4 * 24
        case "week":
            intervals = 4 * 24 * 7

    # check if there's less data then the cutoff
    if len(self.x) < cutoff * intervals:
        cutoff = 0

    # format data around the interval
    for i in range(len(self.x) // intervals):
        x.append(self.x[i * intervals])
        open_list.append(self.open[i * intervals])
        try:
            close.append(self.close[i * intervals + intervals - 1])
        except IndexError:
            close.append(self.close[-1])
        high.append(
            max([high for high in self.high[i * intervals : i * intervals + intervals]])
        )
        low.append(
            min([low for low in self.low[i * intervals : i * intervals + intervals]])
        )
    return dict(
        x=x[cutoff * -1 :],
        open=open_list[cutoff * -1 :],
        close=close[cutoff * -1 :],
        high=high[cutoff * -1 :],
        low=low[cutoff * -1 :],
    )


class Price_history(BaseModel):
    """Dataclass for the history of prices (candlestick graph format)"""

    x: List[datetime]
    open: List[int]
    high: List[int]
    low: List[int]
    close: List[int]

    @classmethod
    def generate_history(
        cls,
        start_date: datetime,
        end_date: datetime,
        initial_price: int | None = 10,
        volatility: int | None = None,
    ) -> Price_history:
        """Function which generates sandwich stock price history

        Args:
            start_date (datetime): from when to start generating
            end_date (datetime): up to what point (usually present)
            initial_price (int | None, optional): Initial stock price. Defaults to 1000.
            volatility (int | None, optional): Volatility (how much the price changes). Defaults to None.
        """

        if volatility == None:
            volatility = initial_price // 10

        indexes = int((end_date - start_date) / timedelta(minutes=15)) + 1

        # generate indexes
        x = []
        for i in range(indexes):
            x.append(start_date + timedelta(minutes=15) * i)

        # generate initial data from which to generate further
        open_list = [initial_price]
        low = [abs(initial_price - randint(0, volatility))]
        high = [initial_price + randint(0, volatility)]
        close = [abs(choice([low[0], high[0]]) + randint(volatility * -1, volatility))]

        # random price variation algorithm
        for i in range(1, indexes):
            open_list.append(close[i - 1])
            low.append(abs(open_list[i] - randint(0, volatility)))
            high.append(open_list[i] + randint(0, volatility))
            close.append(
                abs(choice([low[i], high[i]]) + randint(volatility * -1, volatility))
            )

            # some last checks
            if open_list[i] < low[i]:
                low[i] = open_list[i]
            if open_list[i] > high[i]:
                high[i] = open_list[i]

            if close[i] < low[i]:
                low[i] = close[i]
            if close[i] > high[i]:
                high[i] = close[i]

        return cls(x=x, open=open_list, low=low, high=high, close=close)

    def by_quarters(self) -> dict:
        """Provide graph data, adjusted by every 15 minutes
        There are no changes done, just provides all object data as
        a dictionary for easier use with graphs"""

        # only show data for as far back as a month when showing every 15 minutes
        # prevents the graph from being a laggy mess

        cutoff = 4 * 24 * 31  # one month

        # check if there's less data than the cutoff
        if len(self.x) < cutoff:
            cutoff = 0

        return dict(
            x=self.x[cutoff * -1 :],
            open=self.open[cutoff * -1 :],
            close=self.close[cutoff * -1 :],
            low=self.low[cutoff * -1 :],
            high=self.high[cutoff * -1 :],
        )

    def by_hour(self) -> dict:
        """Provide graph data, adjusted by every hour"""

        # cutoff of one year
        cutoff = 24 * 365

        return adjust(self, "hour", cutoff)

    def by_day(self) -> dict:
        """Provide graph data, adjusted by every day"""

        # cutoff of 5 years
        cutoff = 365 * 5

        return adjust(self, "day", cutoff)

    def by_week(self) -> dict:
        """Provide graph data, adjusted by every week"""

        # cutoff of 10 years
        cutoff = 365 // 7 * 10

        return adjust(self, "week", cutoff)
