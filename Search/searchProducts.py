from Search.databaseAPI import contactsDB

productsTable = 'Products'
productNameCol = 'product_name'
userIDCol = 'user_id'
productIDCol = 'product_id'
query = ''

#Store the variables in an Array to be passed to the API file
productsVarList = [productsTable, productNameCol, userIDCol, productIDCol]

searchString = f'"SELECT "' + userIDCol + ' FROM ' + productsTable + ' WHERE ' 
+ productNameCol + ' LIKE ? OR '
+ productIDCol + ' LIKE ?;'

def searchProducts(query):
    query = str('%' + query.lower() + '%')
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    result = contactsDB.execute(searchString, (escaped_query, escaped_query))
    return result.fetchAll()
