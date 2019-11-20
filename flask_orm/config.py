import os

PG_USER = os.environ.get('PG_USER', "valia")
PG_PASSWORD = os.environ.get('PG_PASSWORD', "password")
PG_HOST = os.environ.get('PG_HOST', "localhost")
PG_PORT = os.environ.get('PG_PORT', 5432)
DB_NAME = os.environ.get('PG_NAME', "ormdb")

