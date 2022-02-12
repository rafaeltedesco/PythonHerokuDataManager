import os

from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION = {
    'database': os.getenv('DATABASE'),
    'connection_string': os.getenv('CONNECTION_STRING').replace('postgres://', 'postgresql://', 1)
}
