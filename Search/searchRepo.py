from APIengine import contactsDB
from sqlalchemy import text

repoTable = 'Repo'
repoNameCol = 'repo_name'
userIDCol = 'user_id'
repoIDCol = 'repo_id'

#Store the variables in an Array to be passed to the API file
repoVarList = [repoTable, repoNameCol, userIDCol, repoIDCol]

searchString = f"""
        SELECT {userIDCol}
        FROM {repoTable}
        WHERE {repoNameCol} LIKE :query 
        OR {repoIDCol} LIKE :query;
"""

def searchRepo(query):
    query = f"%{query.lower()}%"
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    with contactsDB.connect() as connection:
        result = connection.execute(text(searchString), {'query': escaped_query})
    if(result == None):
        return "No results found"
    return result.fetchall()
