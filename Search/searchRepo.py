from APIengine import contactsDB
from sqlalchemy import text

repoTable = 'Repo'
repoNameCol = 'repo_name'
userIDCol = 'user_id'
repoIDCol = 'repo_id'

#Store the variables in an Array to be passed to the API file
repoVarList = [repoTable, repoNameCol, userIDCol, repoIDCol]

searchString = f"""
        SELECT {repoVarList[2]}
        FROM {repoVarList[0]}
        WHERE {repoVarList[1]} LIKE :query 
        OR {repoVarList[3]} LIKE :query;
"""

def searchRepo(query):
    searchTerm = f"%{query}%"
    with contactsDB.connect() as connection:
        result = connection.execute(searchString, {'query': searchTerm})
    return result.fetchall()
