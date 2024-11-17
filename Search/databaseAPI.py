from flask import Flask, request, jsonify
from APIengine import contactsDB    
from sqlalchemy import create_engine , text
from searchContacts import contactsVarList , searchContacts, contactTable
from searchProducts import productsVarList , searchProducts
from searchRepo import repoVarList , searchRepo
import urllib

app = Flask(__name__)
query = ''


entryFieldsList2 = []

#Add a new entry into the contacts table using a series of parameters
def addEntry(entryFieldsList):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {contactTable} VALUES (:firstName, :lastName, :email, :username, :location, :position, :id);"
        connection.execute(text(queryString), {
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
    combinedUserID = contactsResults | productsResults | repoResults

    return combinedUserID

#Returns a 2D array containing the information for every user found in the search
def searchDB(query):
    idSet = getIDSearch(query)
    userArray = []
    for id in idSet:
       with contactsDB.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {contactsVarList[0]} WHERE {contactsVarList[7]} = :id;"), {
                                                'id': id
                                            })
        userArray.extend(result.fetchall())
    
    return userArray

#print(searchDB("Jacob"))

# entryFieldsList2 = ['Ben', 'Hartman', 'benchartman@iu.edu', 'benchartman', 'Bloomington', 'Student', '4']
# addEntry(entryFieldsList2)
# print(searchDB('ben'))

print(searchDB("Dummy product"))