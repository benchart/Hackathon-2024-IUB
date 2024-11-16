from flask import Flask, request, jsonify
from sqlalchemy import create_engine , text
from searchContacts import contactsVarList , searchContacts
from searchProducts import productsVarList , searchProducts
from searchRepo import repoVarList , searchRepo
import urllib

app = Flask(__name__)
query = ''


# Initialize the connection to the SQL server
username = 'huntjac'
password = 'Nn39khnr!'
server = 'hiccup-hackathon-24.database.windows.net'
database = 'hiccup-hackathon'
driver = 'ODBC Driver 18 for SQL Server'

#Create the engine object
connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={urllib.parse.quote_plus(driver)}&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30'
contactsDB = create_engine(connection_string)

#Store the userIDs returned by the search function and return as a combined set
def searchDB(query):
    contactsResults = searchContacts(query)
    productsResults = searchProducts(query)
    repoResults = searchRepo(query)
    combinedUserID = set(contactsResults) | set(productsResults) | set(repoResults)

    return combinedUserID



# with engine.connect() as connection:
#     result = connection.execute(text('SELECT user_id FROM Contacts'))
#     print(result.fetchall())
