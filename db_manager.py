import mysql.connector
from exceptions import UserExistsError, UserNotFoundError, InvalidCredentialsError

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="dell",
        database="user_management"
    )

def register_user(name, username, password, address):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    if cursor.fetchone():
        raise UserExistsError("Username already exists!")

    query = "INSERT INTO users (name, username, password, address) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, username, password, address))
    conn.commit()

    conn.close()
    return " Registration successful!"

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    conn.close()

    if not user:
        raise InvalidCredentialsError("Invalid username or password!")

    return user

def update_address(user_id, new_address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET address = %s WHERE id = %s", (new_address, user_id))
    conn.commit()
    conn.close()
    return " Address updated successfully!"

def update_password(user_id, new_password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE id = %s", (new_password, user_id))
    conn.commit()
    conn.close()
    return " Password updated successfully!"

def delete_account(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    conn.close()
    return " Account deleted successfully!"
