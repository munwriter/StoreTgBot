from dotenv import load_dotenv
import os

def secret_keys(request: str):
    load_dotenv()
    return os.getenv(request)

