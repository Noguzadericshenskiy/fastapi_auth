from os import getenv, path
from dotenv import load_dotenv


load_dotenv()

# Database
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")
DB_USER = getenv("DB_USER")
DB_PASSWORD = getenv("DB_PASSWORD")

# Authentication
SECRET_KEY = "You********secret******string****e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 * 60


HOST = "localhost"
PORT = "8000"

CURRENT_PATH = path.curdir



