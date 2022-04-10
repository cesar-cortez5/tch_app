import pymssql 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
def db():
    server = 'cot-cis3365-03.cougarnet.uh.edu:1433' 
    database = 'InnovaDB' 
    username = 'admin' 
    password = '1234' 

    conn = pymssql.connect(server, username, password, database)
    return conn



