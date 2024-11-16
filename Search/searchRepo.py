repoTable = 'Repo'
repoNameCol = 'repo_name'
userIDCol = 'user_id'
repoIDCol = 'repo_id'
query = ''
searchString = ''

#Store the variables in an Array to be passed to the API file
repoVarList = [repoTable, repoNameCol, userIDCol, repoIDCol, searchString]

# searchString = f'"SELECT "' + userIDCol + ' FROM ' + repoTable + ' WHERE ' 
# + repoNameCol + ' LIKE ? OR '
# + repoIDCol + ' LIKE ?;'

def search(query):
    query = str('%' + query.lower() + '%')
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    cursor.execute(searchString, (query, query))
    return result.fetchAll()
