from APIengine import iniEngine
from sqlalchemy import text

contactTable = 'Contacts'
firstNameCol = 'first_name'
lastNameCol = 'last_name'
emailCol = 'email'
usernameCol= 'username'
locationCol = 'location'
positionCol = 'position'
userIDCol = 'user_id'
contactsDB = iniEngine()

#Store the variables in an Array to be passed to the API file
contactsVarList = [contactTable, firstNameCol, lastNameCol, emailCol, usernameCol, locationCol, positionCol, userIDCol]

searchString = text(f"""
        SELECT {contactsVarList[7]}
        FROM {contactsVarList[0]}
        WHERE {contactsVarList[1]} LIKE :query 
        OR {contactsVarList[2]} LIKE :query
        OR {contactsVarList[3]} LIKE :query
        OR {contactsVarList[4]} LIKE :query
        OR {contactsVarList[5]} LIKE :query
        OR {contactsVarList[6]} LIKE :query;
""")

def searchContacts(query):
    searchTerm = f"%{query}%"
    with contactsDB.connect() as connection:
        result = connection.execute(searchString, {'query': searchTerm})
        rows = set(result.fetchall())
        user_ids_contact = {row[0] for row in rows}
    return user_ids_contact

