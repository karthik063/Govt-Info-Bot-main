#pip install mysql-connector-python

import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 25))

# Commit the changes
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
