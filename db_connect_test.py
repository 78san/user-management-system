import mysql.connector

try:
    # Step 1: Connect to MySQL Database
    conn = mysql.connector.connect(
        host="localhost",        # MySQL server host
        user="root",             # your MySQL username
        password="dell",# your MySQL password
        database="user_management"  # database name
    )

    # Step 2: Check connection
    if conn.is_connected():
        print(" Connection successful!")
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        print(" Tables in database:", cursor.fetchall())

except mysql.connector.Error as err:
    print("Something went wrong:", err)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print(" Connection closed.")
