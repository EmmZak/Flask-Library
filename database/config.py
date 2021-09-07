import os

LOCAL = True

user = "postgres"
password = "postgres"
host = "0.0.0.0" if LOCAL else "flask_library_docker"
database = "flask_library"
port = 5432

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'