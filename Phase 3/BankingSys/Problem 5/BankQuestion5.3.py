import random

import mysql.connector
from datetime import datetime


conn = mysql.connector.connect(host="acadmysqldb001p", user="phk7955", password="TexsLAZ7Vsn@", database="phk7955")
cur = conn.cursor()

if conn.is_connected():
    print('Connected to MySQL database')

#Create new account for a Business

table_name1 = 'loan'
table_name2 = 'branch'

customerID = int(input("Enter customer ID of the Individual customer to issue loan"))
City = input("Enter City")
Branch_ID = input("Enter Branch ID")
Loan_amount = input("Enter loan amount")
random_number = random.randint(1000, 9999)
result = f"SELECT BranchName FROM {table_name2} WHERE Branch_id='Branch_ID'"
cursor = conn.cursor()
cursor.execute(result)
Branch_Name = cursor.fetchall()
print(Branch_Name)
conn.commit()
sql_query1 = f"INSERT INTO {table_name1} (LoanNumber, Branch_id, LoanAmount, BranchName) VALUES ('{random_number}', '{Branch_ID}', '{Loan_amount}', {Branch_Name})"

try:
    cursor = conn.cursor()
    cursor.execute(sql_query1)
    conn.commit()
    print("Data inserted successfully in loan!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

conn.close()