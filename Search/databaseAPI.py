from flask import Flask, request, jsonify
from APIengine import contactsDB
from sqlalchemy import create_engine , text
from searchContacts import contactsVarList , searchContacts, contactTable
from searchProducts import productsVarList , searchProducts, productsTable
from searchRepo import repoVarList , searchRepo, repoTable
import urllib

app = Flask(__name__)



#Add a new entry into the contacts table using a series of parameters
def addContactEntry(entryFieldsList):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {contactTable} ({contactsVarList[1]}, {contactsVarList[2]}, {contactsVarList[3]}, {contactsVarList[4]}, {contactsVarList[5]}, {contactsVarList[6]}, {contactsVarList[7]}) VALUES (:firstName, :lastName, :email, :username, :location, :position, :id);"
        connection.execute(text(queryString), {
                        'firstName': entryFieldsList[0],
                        'lastName': entryFieldsList[1], 
                        'email': entryFieldsList[2], 
                        'username': entryFieldsList[3], 
                        'location': entryFieldsList[4],  
                        'position': entryFieldsList[5], 
                        'id': entryFieldsList[6] 
                        })
        
        connection.commit()

#Add a new entry into the repo table using a series of parameters
def addRepoEntry(user_id, repo_id, repo_name):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {repoTable} ({repoVarList[3]}, {repoVarList[2]}, {repoVarList[1]}) VALUES (:repo_id, :user_id, :repo_name);"
        connection.execute(text(queryString), {
                        'repo_id': repo_id,
                        'user_id': user_id, 
                        'repo_name': repo_name, 
                        })
        
        connection.commit()


#Add a new entry into the products table using a series of parameters
def addProductEntry(user_id, product_id, product_name):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {productsTable} ({productsVarList[3]}, {productsVarList[2]}, {productsVarList[1]}) VALUES (:product_id, :user_id, :product_name);"
        connection.execute(text(queryString), {
                        'product_id': product_id,
                        'user_id': user_id, 
                        'product_name': product_name, 
                        })
        
        connection.commit()




#Remove an entry from the database with the matching paraeters
def removeEntry(id):
    with contactsDB.connect() as connection:

        #Delete matching entries from Contacts
        queryString = f"DELETE FROM {contactTable} WHERE {contactsVarList[7]} = :id;"
        connection.execute(text(queryString), {
                        'id': id 
                        })
        
        #Delete matching entries from Products
        queryString = f"DELETE FROM {productsTable} WHERE {contactsVarList[7]} = :id;"
        connection.execute(text(queryString), {
                        'id': id 
                        })
        
        #Delete matching entries from Repo
        queryString = f"DELETE FROM {repoTable} WHERE {contactsVarList[7]} = :id;"
        connection.execute(text(queryString), {
                        'id': id
                        })
        
        connection.commit()
        

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

#returns the entry corresponding with the provided ID. intended to be used to verify administrative access
def getByID(id):
    with contactsDB.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {contactsVarList[0]} WHERE {contactsVarList[7]} = :id;"), {
                                                'id': id
                                            })
        return result.fetchall()

# entryFieldsList2 = ['Ben', 'Hartman', 'benchartman@iu.edu', 'benchartman', 'Bloomington', 'Student', '4']
# addEntry(entryFieldsList2)

print(searchDB("a"))
print(getByID(1))