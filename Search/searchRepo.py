repoTable = 'Repo'
repoNameCol = 'repo_name'
userIDCol = 'user_id'
repoIDCol = 'repo_id'
query = ''

searchString = f'"SELECT "' + userIDCol + ' FROM ' + repoTable + ' WHERE ' 
+ repoNameCol + ' LIKE ? OR '
+ repoIDCol + ' LIKE ?;'

def search(query):
    query = str('%' + query.lower() + '%')
    escaped_query = query.replace('%', '\\%').replace('_', '\\_')
    cursor.execute(searchString, (query, query))
    return result.fetchAll()

searchRepoResult = search(query)