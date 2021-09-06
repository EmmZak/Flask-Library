import os

user = "postgres"
password = "postgres"
host = "postgres"
database = "flask_library"
port = 5432

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'