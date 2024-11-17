from APIengine import contactsDB
from sqlalchemy import text

contactTable = 'Contacts'
firstNameCol = 'first_name'
lastNameCol = 'last_name'
emailCol = 'email'
usernameCol= 'username'
locationCol = 'location'
positionCol = 'position'
userIDCol = 'user_id'

#Store the variables in an Array to be passed to the API file
contactsVarList = [contactTable, firstNameCol, lastNameCol, emailCol, usernameCol, locationCol, positionCol, userIDCol]

searchString = f"""
        SELECT {userIDCol}
        FROM {contactTable}
        WHERE {firstNameCol} LIKE :query 
        OR {lastNameCol} LIKE :query
        OR {emailCol} LIKE :query
        OR {usernameCol} LIKE :query
        OR {locationCol} LIKE :query
        OR {positionCol} LIKE :query;
"""

def searchContacts(query):
    query = f"%{query.lower()}%"
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    with contactsDB.connect() as connection:
        result = connection.execute(text(searchString), {'query': escaped_query})
    if(result == None):
        return "No results found"
    return result.fetchall()
