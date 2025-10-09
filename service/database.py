import pyodbc

#Some other example server values are
#Server = 'localhost\sqlexpress' # for a named instance
#Server = 'myserver,port' # to specify an alternate port
server = 'tpc:myserver.database.windows.net'
database = 'mydb'
username = 'myusername'
password = 'mypassword'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()