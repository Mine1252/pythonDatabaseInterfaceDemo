# Introduction

This Repo explains how to interface python with a PostgreSQL database. 

This Repo assumes you know the basics of python and its terminology.

## Basics

To interface python with a postgreSQL database we will be using the **PSYCOPG2** python library

Here are the steps to interface with a postgreSQL database in python

1. First inport the psycopg2 library
    ```
    import psycopg2
    ```
2. Next a database connection object (DCO) will need to be created. It can be done through the following code
   ```
   connection = psycopg2.connect("postgres://postgres:xxxxxxxxxx@000.000.000.000:5432/")
   ```
   The main parameter should be a string with the following format

   ```
             |Database| Password |  Database IP  |Port|
   postgres://postgres:xxxxxxxxxx@000.000.000.000:5432/
   ```
3. Next a cursor object (CO) will need to be created from the CDO. The CO will be used for all SQL query execution and data gathering. The CO can be created wit hthe collowing code
   ```
   cursor = connection.cursor()
   ```
4. Next execute any SQL queries or commands use this function
   ```
   cursor.execute("SQL Query Here")
   ```
5. Finally to retrieve any data from the database into a format that python can use you will need to use one of the fetch methods in the CO. Here is each of them and their use:
   ```
   # This will return a list of tuples containing the queried data.
   data = cursor.fetchall()

   # This will return a list of tuples containing N rows of the queried data. 
   # Repeated use will bring the next N rows
   data = cursor.fetchmany(N)

   # This will return a tuple containing 1 row of the queried data. 
   # Using this again will bring the next row of the queried data.
   data = cursor.fetchone()
   ```

For an example please refer to the *pythonPostgreSQLExample.py* file in this repo.

