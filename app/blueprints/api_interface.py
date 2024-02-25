import requests
from server.models import Sandwich
from flask import abort
from dotenv import load_dotenv
from os import getenv


class API:
    """Class that serves as an interface between the server and the web app"""

    def __init__(self) -> None:
        # self.url = "http://127.0.0.1:2727/"
        load_dotenv("../.env")
        self.url = str(getenv("FASTAPI_URL"))

    def get_sandwich_by_id(self, sandwich_id: str) -> Sandwich:
        """get sandwich from the api via id"""
        response = requests.get(f"{self.url}sandwich/{sandwich_id}")

        return Sandwich(**response.json())

    def get_sandwich_by_name(self, sandwich_name: str) -> dict[str, str]:
        """Search by name

        Args:
            sandwich_name (str): sandwich name

        Returns:
            dict[id,sandwich name]: query results
        """

        response = requests.get(f"{self.url}sandwiches/search/{sandwich_name}")

        return response.json()

    def post_sandwich(self, sandwich: Sandwich) -> bool:

        response = requests.post(f"{self.url}sandwich/", json={**sandwich.model_dump()})

        if response.status_code == 200:
            return True
        else:
            abort(500)

    def update_sandwich(self, sandwich_id: str, sandwich: Sandwich) -> bool:
        """update sandwich via the api

        Args:
            sandwich_id (str): sandwich id
            sandwich (Sandwich): sandwich data

        Returns:
            bool: return code
        """

        response = requests.put(
            f"{self.url}sandwich/{sandwich_id}", json={**sandwich.model_dump()}
        )
        if response.status_code == 200:
            return True
        else:
            abort(500)

    def delete_sandwich(self, sandwich_id: str) -> bool:
        """Delete sandwich via api

        Args:
            sandwich_id (str): sandwich id

        Returns:
            bool: return code
        """

        response = requests.delete(f"{self.url}sandwich/{sandwich_id}")

        if response.status_code == 200:
            return True
        else:
            abort(500)

    def get_all_sandwiches(self) -> dict:
        """get all the sandwiches from the api"""

        response = requests.get(f"{self.url}sandwiches/all")

        return response.json()

    def get_top_5(self) -> list[Sandwich]:
        """Get the data for the top 5 sandwiches

        Returns:
            list[Sandwich]: top 5 sandwiches data
        """

        response = requests.get(f"{self.url}sandwiches/top5")

        list = response.json()

        # convert sandwich data back into sandwich objects
        for i in range(len(list)):
            list[i] = Sandwich(**list[i])

        return list
