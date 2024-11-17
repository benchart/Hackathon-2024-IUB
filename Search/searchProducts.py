from APIengine import contactsDB
from sqlalchemy import text

productsTable = 'Products'
productNameCol = 'product_name'
userIDCol = 'user_id'
productIDCol = 'product_id'

#Store the variables in an Array to be passed to the API file
productsVarList = [productsTable, productNameCol, userIDCol, productIDCol]

searchString = text(f"""
        SELECT {productsVarList[2]}
        FROM {productsVarList[0]}
        WHERE {productsVarList[1]} LIKE :query
        OR {productIDCol} LIKE :query;
""")

def searchProducts(query):
    searchTerm = f"%{query}%"
    with contactsDB.connect() as connection:
        result = connection.execute(searchString, {'query': searchTerm})
        rows = result.fetchall()
        user_ids = set(row for row in rows)
    return user_ids
