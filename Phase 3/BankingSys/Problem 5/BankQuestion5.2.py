# Question 5.2
import mysql.connector
from datetime import datetime


conn = mysql.connector.connect(host="acadmysqldb001p", user="phk7955", password="TexsLAZ7Vsn@", database="phk7955")
cur = conn.cursor()

if conn.is_connected():
    print('Connected to MySQL database')

#Create new account for a Business

table_name1 = 'account'
table_name2 = 'owned_by'

customerID = int(input("Enter customer ID of the Individual customer to create a new account"))
Acc = input("Enter account number")
acc_type = input("Enter account type(Checking/Savings)")
current_date = datetime.now().date()
sql_query1 = f"INSERT INTO {table_name1} (AccountNumber, Balance, LastAccessDate, AccountType) VALUES ('{Acc}', '{1000}', '{current_date}', '{acc_type}')"

try:
    cursor = conn.cursor()
    cursor.execute(sql_query1)
    conn.commit()
    print("Data inserted successfully in account!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

sql_query2 = f"INSERT INTO {table_name2} (Customer_ID, AccountNumber) VALUES ('{customerID}', '{Acc}')"

try:
    cursor = conn.cursor()
    cursor.execute(sql_query2)
    conn.commit()
    print("Data inserted successfully in owned_by!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

conn.close()