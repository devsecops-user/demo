import sqlite3

def get_user_details(user_id):
    # Connect to an SQLite database
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Unsafe SQL query construction
    query = "SELECT * FROM users WHERE id = '" + user_id + "';"
    cursor.execute(query)

    # Fetch and print all results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the database connection
    connection.close()

# Example usage with a user input that could be manipulated for SQL Injection
user_input = "1'; DROP TABLE users;--"
get_user_details(user_input)
