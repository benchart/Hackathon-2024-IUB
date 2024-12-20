from sqlalchemy import create_engine
import urllib

def iniEngine():
    # Initialize the connection to the SQL server
    username = 'username'
    password = 'passowrd'
    server = 'hiccup-hackathon-24.database.windows.net'
    database = 'hiccup-hackathon'
    driver = 'ODBC Driver 18 for SQL Server'

    #Create the engine object
    connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={urllib.parse.quote_plus(driver)}&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30'
    contactsDB = create_engine(connection_string)
    return contactsDB

contactsDB = iniEngine()