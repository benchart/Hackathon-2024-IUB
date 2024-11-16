from Search.databaseAPI import contactsDB

contactTable = 'Contacts'
firstNameCol = 'first_name'
lastNameCol = 'last_name'
emailCol = 'email'
usernameCol= 'username'
locationCol = 'location'
positionCol = 'position'
userIDCol = 'user_id'
query = ''
searchString = ''

#Store the variables in an Array to be passed to the API file
contactsVarList = [contactTable, firstNameCol, lastNameCol, emailCol, usernameCol, locationCol, positionCol, userIDCol, searchString]

# searchString = f'"SELECT "' + userIDCol + ' FROM ' + contactTable + ' WHERE ' 
# + firstNameCol + ' LIKE ? OR '
# + lastNameCol + ' LIKE ? OR '
# + emailCol + ' LIKE ? OR '
# + usernameCol + ' LIKE ? OR '
# + locationCol + ' LIKE ? OR '
# + positionCol + ' LIKE ?;'

def searchContacts(query):
    query = str('%' + query.lower() + '%')
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    result = contactsDB.execute(searchString, (escaped_query, escaped_query, escaped_query, escaped_query, escaped_query, escaped_query))
    return result.fetchAll()

