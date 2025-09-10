"""
Module to manage environment variables using python-dotenv.
"""

import os

from dotenv import load_dotenv


class Config:
    """
    Class to manage environment variables.
    Uses python-dotenv to load variables from a .env file into the environment.
    """

    def __init__(self):
        """
        Load environment variables from a .env file and initialize the Config class.
        """

        load_dotenv()

    @staticmethod
    def get(key: str) -> str | None:
        """
        Get the value of an environment variable.
        Args:
            key (str): The key of the environment variable to retrieve.
        Returns:
            str | None: The value of the environment variable, or None if it is not set
        """

        return os.getenv(key)

    @staticmethod
    def set(key: str, value: str):
        """
        Set the value of an environment variable.
        Args:
            key (str): The key of the environment variable to set.
            value (str): The value to set the environment variable to.
        Returns:
            None
        """

        os.environ[key] = value
