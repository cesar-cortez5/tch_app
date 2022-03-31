import pymssql 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
def db():
    server = 'localhost' 
    database = 'local_cis3365' 
    username = 'sa' 
    password = 'Password55!' 

    conn = pymssql.connect(server, username, password, database)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Customer_Info')
    return conn



