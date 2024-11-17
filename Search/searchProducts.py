from APIengine import contactsDB
from sqlalchemy import text

productsTable = 'Products'
productNameCol = 'product_name'
userIDCol = 'user_id'
productIDCol = 'product_id'

#Store the variables in an Array to be passed to the API file
productsVarList = [productsTable, productNameCol, userIDCol, productIDCol]

searchString = f"""
        SELECT {userIDCol}
        FROM {productsTable}
        WHERE {productNameCol} LIKE :query OR {productIDCol} LIKE :query;
"""

def searchProducts(query):
    query = f"%{query.lower()}%"
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    with contactsDB.connect() as connection:
        result = connection.execute(text(searchString), {'query': escaped_query})
    if(result == None):
        return "No results found"
    return result.fetchall()
