from distutils.log import debug
from operator import inv
from re import L
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db_connection
import pymssql
from pydantic import BaseModel

#Setting up our FastAPI server. 
app = FastAPI()

#This will only allow requests from port 3000, which is our web server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Initializing our database connection. This should be changed to your local database, or the remote database on the windows remote desktop
conn = db_connection.db()
cursor = conn.cursor()
dict_cursor = conn.cursor(as_dict=True)

#This gets the maximum id of a table. However, this should not be needed if we properly add autoincrement to our database.

#Creating a structure used to store customer data when a request is ran
class CustomerInfo(BaseModel):
    first_name: str
    middle_initial : str
    last_name: str
    company_name: str
    email: str
    address: str
    zip: str
    city: str
    state: int
    country: int
    phone1: str
    phone2: Optional[str]

#Creating a new endpoint called /new_customer, that takes in customer_info, which is a JSON strucutre in format above, as a parameter
@app.post("/new_customer")
def new_customer(customer_info: CustomerInfo):
    #Getting the firstname and lastname. This would be changed in the future as customers can enter their names in different ways.
    #Getting the customer city and state. We need to create a state table, and only allow choices from entries within that table.
    #Getting all our IDS for the tables we are going to use. If we set up autoincrement, this will not be necessary


    '''
    For SQL queries, you can either use f strings
    eg. f"INSERT INTO VALUES ({customer_name}, {customer_company})" where customer_name and customer_company are variables,
    or the way I am doing it by using string interpolation, in which the %s, %s, %s are placeholders, and the placeholders are replaced
    using variables that are retrieved from cursor.execute'''
    #SQL query to insert into Customer_Info table.
    print(customer_info)
    customer_info_query = 'INSERT INTO CUSTOMER VALUES(%s, %s, %s)'
    cursor.execute(customer_info_query, (customer_info.first_name, customer_info.middle_initial, customer_info.last_name))
    customer_id = cursor.lastrowid
    print(customer_id)
    conn.commit()
    #SQL query to insert into customer contact table, which has a relationship to the customer_info table. The null value should be changed in the future.
    customer_contact_query = 'INSERT INTO Customer_Contact VALUES (%s, %s, %s, %s)'
    cursor.execute(customer_contact_query, (customer_id, customer_info.phone1, customer_info.phone2, customer_info.email))
    conn.commit()
    #SQL query to insert into customer_location table,
    customer_location_query = 'INSERT INTO Customer_Address VALUES (%s, %s, %s, %s, %s, %s)'
    print(customer_id, customer_info.address, customer_info.city, customer_info.state, customer_info.zip, customer_info.country)
    cursor.execute(customer_location_query, (customer_id, customer_info.address, customer_info.city, customer_info.state, customer_info.zip, customer_info.country))

    #After an insert, delete, alter, modify, ec SQL command is done, a conn.commit() is needed to save changes within DB
    conn.commit()
    #Returning the information
    return {
        "status": "SUCCESS",
        "data": customer_info,
        "customer_id": customer_id
    }

@app.get("/get_customer")
def show_customers(customer_name: str):
    firstname, lastname = customer_name.split()

    #Getting all customers where first name and last name match
    customer_query = '''SELECT ci.Customer_ID, ci.First_Name, ci.Last_Name, cc.Email FROM Customer ci
                     INNER JOIN Customer_Contact cc ON cc.Customer_ID = ci.Customer_Id
                     WHERE ci.First_Name = %s and ci.Last_Name = %s'''
    dict_cursor.execute(customer_query, (firstname, lastname))
    return {"customers": dict_cursor.fetchall()}

@app.get('/get_customer_id')
def get_customer_id(customer_id: int):
    customer_query = '''SELECT ci.Customer_ID, ci.First_Name, ci.Middle_Intial, ci.Last_Name, cc.Phone1, cc.Phone2, cc.Email FROM Customer ci
                     INNER JOIN Customer_Contact cc ON cc.Customer_ID = ci.Customer_Id
                     WHERE ci.Customer_ID = %s'''


class InvoiceEquipment(BaseModel):
    bench_number: str
    invoice_date: str
    invoice_status_id: int
    loginuser: str
    loginpassword: str
    encryption: str
    brand: str
    model: str
    operatingsystem: str
    serialnumber: str
    customer_id: int
    pin: str
@app.get("/update_status")
def update_status(invoice_id: int, invoice_status_id: int):
    print(invoice_id, invoice_status_id)
    query = ''' UPDATE Invoice SET Invoice_Status_ID = %s WHERE Invoice_ID = %s  '''
    cursor.execute(query, (invoice_status_id, invoice_id))
    conn.commit()

@app.post("/new_invoice")
def new_invoice(invoice_equipment: InvoiceEquipment):
    new_invoice_query = '''
    INSERT INTO Invoice (Customer_ID, Bench_Number, Invoice_Date, Invoice_Status_ID) VALUES (%s, %s, %s, %s)
    '''
    cursor.execute(new_invoice_query, (invoice_equipment.customer_id, invoice_equipment.bench_number, invoice_equipment.invoice_date, invoice_equipment.invoice_status_id))
    invoice_id = cursor.lastrowid
    conn.commit()
    new_equipment = '''
    INSERT INTO Equipment VALUES (%s, %s, %s, %s ,%s, %s, %s, %s, %s)
    '''
    cursor.execute(new_equipment, (invoice_id, invoice_equipment.encryption, invoice_equipment.brand, invoice_equipment.loginuser, invoice_equipment.loginpassword, invoice_equipment.model, invoice_equipment.operatingsystem, invoice_equipment.pin, invoice_equipment.serialnumber))
    equipment_id = cursor.lastrowid
    conn.commit()
    return {"invoice_id": invoice_id,
            "equipment_id": equipment_id}

@app.get("/status_types")
def status_types():
    dict_cursor.execute("SELECT * FROM Invoice_Status")
    return {"statuses": dict_cursor.fetchall()}
@app.get("/invoices")
def current_invoices(customer_id: int):
    invoice_query = '''
    SELECT Invoice.Invoice_ID, e.Equipment_ID, e.Brand, Invoice.Bench_Number, Invoice_Status.Status_Name FROM Invoice 
    INNER JOIN Customer ON Customer.Customer_ID = Invoice.Customer_ID
    INNER JOIN Equipment e ON e.Invoice_ID = Invoice.Invoice_ID
    LEFT JOIN Invoice_Status ON Invoice_Status.Status_ID = Invoice.Invoice_Status_ID
    WHERE Invoice.Customer_ID = %s
    '''
    dict_cursor.execute(invoice_query, customer_id)
    return {"invoices": dict_cursor.fetchall()}

@app.get('/states')
def states():
    dict_cursor.execute('SELECT * From States')
    return {"states": dict_cursor.fetchall()}

@app.get('/countries')
def countries():
    dict_cursor.execute('SELECT * FROM Countries')
    return {"countries": dict_cursor.fetchall()}

class AdminLogin(BaseModel):
    username: str
    password: str
    
@app.post('/new_admin_login')
def new_admin_login(admin_login: AdminLogin):
    query = '''
    INSERT INTO Admin_Login (username, password) VALUES (%s, %s)
    '''
    cursor.execute(query, (admin_login.username, admin_login.password))
    conn.commit()
    
@app.post('/admin_login')
def admin_login(admin_login:AdminLogin):
    query = '''SELECT * FROM Admin_Login WHERE username = %s AND password = %s'''
    cursor.execute(query, (admin_login.username, admin_login.password))
    exist = cursor.fetchone()
    if exist:
        return {"authorized": True}
    else:
        return {"authorized": False}

@app.post('/employee_login')
def employee_login(admin_login:AdminLogin):
    #change later
    query = '''SELECT * FROM Admin_Login WHERE username = %s AND password = %s'''
    cursor.execute(query, (admin_login.username, admin_login.password))
    exist = cursor.fetchone()
    if exist:
        return {"authorized": True}
    else:
        return {"authorized": False}


if __name__ == "__main__":
    #Uvicorn is a python library used to easily test endpoints. When you run this, you can visit localhost:5001/docs, and see and test all the endpoints
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5001, debug=True)
