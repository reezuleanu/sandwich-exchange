import sys
from datetime import datetime

sys.path.append("../")

from server.models import Price_history

history = None
startdate = datetime(2020, 1, 1)
enddate = datetime.now()


def test_generate_history() -> None:
    global history
    history = Price_history.generate_history(startdate, enddate)

    assert type(history) is Price_history


def test_adjust_quarters() -> None:
    assert history.by_quarters()["close"][-1] == history.model_dump()["close"][-1]


# def test_adjust_hour() -> None:
#     adjusted = history.by_hour()
#     assert (
#         adjusted["close"][-1]
#         == history.model_dump()["close"][(len(adjusted["x"]) // 4 + 3) * -1]
#     )


# def test_adjust_day() -> None:
#     # assert history.by_day()["close"][-1] == history.model_dump()["close"][-4]
#     assert history.by_day()["close"][-1] == history.close[-25]
