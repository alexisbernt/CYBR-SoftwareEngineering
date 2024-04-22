# MIT Licensed. Copyright (c) 2017
import pyodbc
# cnxn = pyodbc.connect("Driver={SQL Server};"
#                       "Server=LAPTOP-3JNM76RU;"
#                       "Database=LoperSlamdUNKDB;"
#                       "Trusted_Connection=yes;")
# #Another note: we will have to put a username and password on here when we make it accessible via the Internet.

# cursor = cnxn.cursor()
# import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.engine import URL

# Setup our connection to the database

connection_string = (
    "Driver={SQL Server};"
    "Server=LAPTOP-3JNM76RU;"
    "Database=LoperSlamdUNKDB;"
    "Trusted_Connection=yes;"
)
connection_url = URL.create(
    "mssql+pyodbc", 
    query={"odbc_connect": connection_string}
)

engine = create_engine(connection_url, use_setinputsizes=False)
Base = automap_base()
Base.prepare(engine, reflect=True)

#NOTE!!: Find words "engine" and "Base" throughout other files. Ensure proper replacements are made for conversion from SQLite to pyodbc...