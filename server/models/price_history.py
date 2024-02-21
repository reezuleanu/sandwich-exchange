from __future__ import annotations
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List
from random import randint, choice


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
        initial_price: int | None = 1000,
        volatility: int | None = None,
    ) -> Price_history:
        """Function which generates sandwich stock price history

        Args:
            start_date (datetime): from when to start generating
            end_date (datetime): up to what point (usually present)
            initial_price (int | None, optional): Initial stock price. Defaults to 1000.
            volatility (int | None, optional): Volatility (how much the price changes). Defaults to None.

        Returns:
            Price_history: _description_
        """

        if volatility == None:
            volatility = initial_price // 10

        indexes = int((end_date - start_date) / timedelta(minutes=15))

        # generate indexes
        x = []
        for i in range(indexes + 1):
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
        """Provide graph data, adjusted by every 15 minutes"""

        # only show data for as far back as a month when showing every 15 minutes
        # prevents the graph from being a laggy mess
        cutoff = 4 * 24 * 30

        # check if there's enough data to cut from
        if len(self.x) < cutoff * 4:
            cutoff = 0

        return dict(
            x=self.x[cutoff:],
            open=self.open[cutoff:],
            close=self.close[cutoff:],
            low=self.low[cutoff:],
            high=self.high[cutoff:],
        )

    def by_hour(self) -> dict:
        """Provide graph data, adjusted by every hour"""
        x = []
        open_list = []
        close = []
        high = []
        low = []

        # only show data for as far back as a month when showing every 15 minutes
        # prevents the graph from being a laggy mess
        cutoff = 24 * 365

        # check if there's enough data to cut from
        if len(self.x) < cutoff * 4:
            cutoff = 0

        for i in range(len(self.x) // 4):
            x.append(self.x[i * 4])
            open_list.append(self.open[i * 4])
            try:
                close.append(self.close[i * 4 + 3])
            except IndexError:
                close.append(self.close[-1])
            high.append(max([high for high in self.high[i * 4 : i * 4 + 3]]))
            low.append(min([low for low in self.low[i * 4 : i * 4 + 3]]))
        return dict(
            x=x[cutoff:],
            open=open_list[cutoff:],
            close=close[cutoff:],
            high=high[cutoff:],
            low=low[cutoff:],
        )
