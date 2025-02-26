import mysql.connector
from datetime import datetime

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='129.107.152.162',
    user='phk7955@%',
    password='TexsLAZ7Vsn@',
    database='phk7955'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Now you can execute your MySQL queries using the cursor

# For example:
cursor.execute("SELECT * FROM your_table;")
result = cursor.fetchall()
print(result)

# Don't forget to close the cursor and the connection when you're done
cursor.close()
conn.close()
