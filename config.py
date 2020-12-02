import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
URL_ADMIN = os.getenv("URL_ADMIN")
URL_PROM = os.getenv("URL_PROM")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_NAME = os.getenv("PG_NAME")
PG_HOST = os.getenv("PG_HOST")
