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

entryFieldsList = []

#Add a new entry into the contacts table using a series of parameters
def addEntry(entryFieldsList):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {contactsVarList[0]} VALUES (:firstName, :lastName, :email, :username, :location, :position, :id);"
        result = connection.execute(text(queryString), {
                                        'firstName': entryFieldsList[0],
                                        'lastName': entryFieldsList[1], 
                                        'email': entryFieldsList[2], 
                                        'username': entryFieldsList[3], 
                                        'location': entryFieldsList[4],  
                                        'position': entryFieldsList[5], 
                                        'id': entryFieldsList[6] 
                                    })
        

#Store the userIDs returned by the search function and return as a combined set
def getIDSearch(query):
    contactsResults = searchContacts(query)
    productsResults = searchProducts(query)
    repoResults = searchRepo(query)
    combinedUserID = set(contactsResults) | set(productsResults) | set(repoResults)

    return combinedUserID

#Returns a 2D array containing the information for every user found in the search
def searchDB(query):
    idSet = getIDSearch(query)
    userArray = [1][7]
    for id in idSet:
       with contactsDB.connect() as connection:
        result = str(connection.execute(text(f"SELECT * FROM :contactsTable WHERE :id = {id};"), {
                                            'contactsTable': entryFieldsList[0],
                                            'id': entryFieldsList[6]
                                        }))
        userArray.append(result)
    return userArray


# with engine.connect() as connection:
#     result = connection.execute(text('SELECT user_id FROM Contacts'))
#     print(result.fetchall())
