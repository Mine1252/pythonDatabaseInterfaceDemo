import psycopg2
import os


pwd = os.environ["POSTGRES_PWD"]
ip = os.environ["POSTGRES_IP"]
port = os.environ["POSTGRES_PORT"]
table = os.environ["POSTGRES_TABLE"]

connection = psycopg2.connect(f"postgres://postgres:{pwd}@{ip}:{port}/")

cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {table} LIMIT 1;")

data = cursor.fetchall()

print(data)
