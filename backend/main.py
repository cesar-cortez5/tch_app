from distutils.log import debug
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db_connection
import pymssql
from pydantic import BaseModel
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


server = 'localhost' 
database = 'local_cis3365' 
username = 'sa' 
password = 'Password55!' 

conn = pymssql.connect(server, username, password, database)
cursor = conn.cursor()
dict_cursor = conn.cursor(as_dict=True)


def get_max_id(table: str, column_name: str, cursor) -> int:
    '''
    Autogeneration in SQL Server is funky, so using this in the meantime. 
    Might change later when autogeneration is set up. MYSQL > SQL SERVER
    '''
    print(table, column_name)
    max_id_query = f'SELECT MAX({column_name}) FROM {table}'
    #max_id_query = "SELECT * FROM Customer_Info"
    cursor.execute(max_id_query)
    index = cursor.fetchone()[0]
    print(index)
    if index is None:
        index = 0
    
    return index + 1

class CustomerInfo(BaseModel):
    customer_name: str
    company_name: str
    email: str
    address: str
    citystate: str
    zip: str
    phone1: str
    phone2: Optional[str]


@app.post("/new_customer")
def new_customer(customer_info: CustomerInfo):
    print('test')
    customer_firstname, customer_lastname = customer_info.customer_name.split()
    customer_city, customer_state = customer_info.citystate.split(",")

    customer_info_id = get_max_id('Customer_Info', 'Customer_Id', cursor)
    customer_contact_id = get_max_id('Customer_Contact', 'Contact_ID', cursor)
    customer_location_id =  get_max_id('Customer_Location', 'Customer_Location_ID', cursor)
    customer_info_query = 'INSERT INTO Customer_Info VALUES(%d, %s, %s)'
    
    cursor.execute(customer_info_query, (customer_info_id, customer_firstname, customer_lastname))

    customer_contact_query = 'INSERT INTO Customer_Contact VALUES (%d, %s, %s, null, %s, %d)'
    cursor.execute(customer_contact_query, (customer_contact_id, customer_info.phone1, customer_info.phone2, customer_info.email, customer_info_id))
    
    customer_location_query = 'INSERT INTO Customer_Location VALUES (%d, %s, %s, %s, %d)'
    cursor.execute(customer_location_query, (customer_location_id, customer_city, customer_state, customer_info.zip, customer_info_id))
    conn.commit()
    return {
        "status": "SUCCESS",
        "data": customer_info,
        "customer_id": customer_info_id
    }

@app.get("/get_customer")
def show_customers(customer_name: str):
    firstname, lastname = customer_name.split()

    customer_query = '''SELECT ci.Customer_ID, ci.First_Name, ci.Last_Name, cc.Customer_Email FROM Customer_Info ci
                     INNER JOIN Customer_Contact cc ON cc.Customer_ID = ci.Customer_Id
                     WHERE ci.First_Name = %s and ci.Last_Name = %s'''
    dict_cursor.execute(customer_query, (firstname, lastname))
    return {"customers": dict_cursor.fetchall()}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5001, debug=True)