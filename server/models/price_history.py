from pydantic import BaseModel
from datetime import datetime
from typing import List


class Price_history(BaseModel):
    """Dataclass for the history of prices (candlestick graph format)"""

    x: List[datetime]
    open: List[int]
    high: List[int]
    low: List[int]
    close: List[int]
