repoTable = 'Repo'
repoNameCol = 'repo_name'
userIDCol = 'user_id'
repoIDCol = 'repo_id'
query = ''

#Store the variables in an Array to be passed to the API file
repoVarList = [repoTable, repoNameCol, userIDCol, repoIDCol]

searchString = f"""
        SELECT {userIDCol}
        FROM {repoTable}
        WHERE {repoNameCol} LIKE :query 
        OR {repoIDCol} LIKE :query;
"""

def searchRepo(query):
    from databaseAPI import contactsDB
    from sqlalchemy import text

    query = f"%{query.lower()}%"
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    with contactsDB.connect() as connection:
        result = connection.execute(text(searchString), {'query': escaped_query})
    return result.fetchAll()
