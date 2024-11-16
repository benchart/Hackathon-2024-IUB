productsTable = 'Products'
productNameCol = 'product_name'
userIDCol = 'user_id'
productIDCol = 'product_id'
query = ''
searchString = ''

# searchString = f'"SELECT "' + userIDCol + ' FROM ' + productsTable + ' WHERE ' 
# + productNameCol + ' LIKE ? OR '
# + productIDCol + ' LIKE ?;'

def search(query):
    query = str('%' + query.lower() + '%')
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    cursor.execute(searchString, (query, query))
    return result.fetchAll()

searchProductsResult = search(query)