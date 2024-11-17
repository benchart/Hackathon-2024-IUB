from APIengine import contactsDB
from sqlalchemy import text
from searchContacts import contactsVarList, searchContacts, contactTable
from searchProducts import productsVarList, searchProducts, productsTable
from searchRepo import repoVarList, searchRepo, repoTable


#Determines the current user_id value using the number of rows in the contact table
def __getCurrentID__():
    with contactsDB.connect() as connection:
        queryString = f"SELECT COUNT({contactsVarList[6]}) FROM {contactTable};"
        result = connection.execute(text(queryString))
        currentID = result.scalar()
        return currentID




#Add functions, adds data to the database



#Add a new entry into the contacts table using a series of parameters
def addContactEntry(entryFieldsList):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {contactTable} ({contactsVarList[1]}, {contactsVarList[2]}, {contactsVarList[3]}, {contactsVarList[4]}, {contactsVarList[5]}, {contactsVarList[6]}) VALUES (:name, :email, :username, :location, :position, :id);"
        connection.execute(text(queryString), {
                        'name': entryFieldsList[0], 
                        'email': entryFieldsList[1], 
                        'username': entryFieldsList[2], 
                        'location': entryFieldsList[3],  
                        'position': entryFieldsList[4], 
                        'id': __getCurrentID__()+1 
                        })
        connection.commit()


#Add a new entry into the repo table using a series of parameters
def addRepoEntry(user_id, repo_name):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {repoTable} ({repoVarList[3]}, {repoVarList[2]}, {repoVarList[1]}) VALUES (:repo_id, :user_id, :repo_name);"
        connection.execute(text(queryString), {
                        'repo_id': abs(hash(repo_name.lower())),
                        'user_id': user_id, 
                        'repo_name': repo_name, 
                        })
        
        connection.commit()


#Add a new entry into the products table using a series of parameters
def addProductEntry(user_id, product_name):
    with contactsDB.connect() as connection:
        queryString = f"INSERT INTO {productsTable} ({productsVarList[3]}, {productsVarList[2]}, {productsVarList[1]}) VALUES (:product_id, :user_id, :product_name);"
        connection.execute(text(queryString), {
                        'product_id': abs(hash(product_name.lower())),
                        'user_id': user_id, 
                        'product_name': product_name, 
                        })
        
        connection.commit()


#Remove an entry from the database with the matching paraeters
def removeEntry(id):
    with contactsDB.connect() as connection:

        #Delete matching entries from Contacts
        queryString = f"DELETE FROM {contactTable} WHERE {contactsVarList[6]} = :id;"
        connection.execute(text(queryString), {
                        'id': id 
                        })
        
        #Delete matching entries from Products
        queryString = f"DELETE FROM {productsTable} WHERE {contactsVarList[6]} = :id;"
        connection.execute(text(queryString), {
                        'id': id 
                        })
        
        #Delete matching entries from Repo
        queryString = f"DELETE FROM {repoTable} WHERE {contactsVarList[6]} = :id;"
        connection.execute(text(queryString), {
                        'id': id
                        })
        
        connection.commit()
        


#Search functions, returns information from the database


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

    #Protect against empty queries
    if(query == ''):
        return userArray
    
    for id in idSet:
       with contactsDB.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {contactsVarList[0]} WHERE {contactsVarList[6]} = :id;"), {
                                                'id': id
                                            }) 
        rows = result.fetchall()
        for row in rows:
            userArray.append(row)
    
    return userArray

#returns the entry corresponding with the provided ID. Intended to be used to verify administrative access
def getByID(id):
    with contactsDB.connect() as connection:
        result = connection.execute(text(f"SELECT * FROM {contactsVarList[0]} WHERE {contactsVarList[6]} = :id;"), {
                                                'id': id
                                            })
        return result.fetchall()

#Returns the specified entry's position given an ID. Intended to be used to verify administrative access
def getPositionByID(id):
    with contactsDB.connect() as connection:
        result = connection.execute(text(f"SELECT {contactsVarList[5]} FROM {contactsVarList[0]} WHERE {contactsVarList[6]} = :id;"), {
                                                'id': id
                                            })
        return result.fetchall()

#entryFields = ['Jacob Hunt', 'huntjac@iu.edu', 'huntjac', 'Bloomington', 'Student']
print(searchDB(""))