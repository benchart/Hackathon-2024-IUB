from flask import Flask, request, jsonify
from sqlalchemy import create_engine , text
from searchContacts import contactsVarList
import urllib

app = Flask(__name__)


username = 'huntjac'
password = 'Nn39khnr!'
server = 'hiccup-hackathon-24.database.windows.net'
database = 'hiccup-hackathon'
driver = 'ODBC Driver 18 for SQL Server'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={urllib.parse.quote_plus(driver)}&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30'
contactsDB = create_engine(connection_string)


# with engine.connect() as connection:
#     result = connection.execute(text('SELECT user_id FROM Contacts'))
#     print(result.fetchall())
