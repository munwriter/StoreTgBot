import os

from dotenv import load_dotenv


def secret_keys(request: str):
    load_dotenv()
    return os.getenv(request)

