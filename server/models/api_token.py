from __future__ import annotations
from uuid import UUID, uuid4, uuid5
from pydantic import BaseModel


# todo change this so it can be used to authentificate users on the web app as well
class Token(BaseModel):
    """Data class for API tokens (currently only used by the web app, could implement a way
    to let people create their own tokens and make their own tools and websites with the
    almighty sanwich API)"""

    token: UUID

    # !Right now this is useless!
    @classmethod
    def generate(cls, username: str) -> Token:
        """Class method to generate a token object

        Args:
            username (str): username of account generating it

        Returns:
            Token: generated token
        """

        namespace = uuid4()
        token = uuid5(namespace, username)
        return cls(token=token)
