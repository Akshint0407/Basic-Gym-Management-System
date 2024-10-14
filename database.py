import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="GymManagement"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def add_member(full_name, email, phone, join_date, subscription_type):
    connection = create_connection()
    if connection is None:
        print("Failed to create connection to the database.")
        return

    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO Members (full_name, email, phone, join_date, subscription_type) VALUES (%s, %s, %s, %s, %s)",
        (full_name, email, phone, join_date, subscription_type)
    )
    connection.commit()
    cursor.close()
    connection.close()

def retrieve_members(search_query=""):
    connection = create_connection()
    if connection is None:
        print("Failed to create connection to the database.")
        return []

    cursor = connection.cursor()
    if search_query:
        cursor.execute("SELECT * FROM Members WHERE full_name LIKE %s", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT * FROM Members")
    
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_member(member_id, full_name, email, phone, join_date, subscription_type):
    connection = create_connection()
    if connection is None:
        print("Failed to create connection to the database.")
        return

    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE Members 
        SET full_name = %s, email = %s, phone = %s, join_date = %s, subscription_type = %s 
        WHERE id = %s
        """,
        (full_name, email, phone, join_date, subscription_type, member_id)
    )
    connection.commit()
    cursor.close()
    connection.close()

def delete_member(member_id):
    connection = create_connection()
    if connection is None:
        print("Failed to create connection to the database.")
        return

    cursor = connection.cursor()
    cursor.execute("DELETE FROM Members WHERE id = %s", (member_id,))
    connection.commit()
    cursor.close()
    connection.close()