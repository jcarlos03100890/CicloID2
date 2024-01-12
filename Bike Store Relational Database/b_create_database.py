import mysql.connector

def create_database():
    # MySQL connection parameters
    db_user = 'data'
    db_password = 'myd4tAUser**'
    db_host = '192.168.100.52'

    # Database name to be created
    db_name = 'data_analysis'

    # Connect to MySQL server
    connection = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host
    )

    # Create a MySQL cursor
    cursor = connection.cursor()

    # Check if the database already exists
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
    exists = cursor.fetchone()
    
    # Drop the database if it exists
    if exists:
        # Drop the database if it exists
        cursor.execute(f"DROP DATABASE {db_name}")
        print(f"Database '{db_name}' dropped.")
   
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")
    exists = cursor.fetchone()
    
    if not exists:
        #Create the database if it does not exist
        # Create the database
        cursor.execute(f"CREATE DATABASE {db_name}")
        print(f"Database '{db_name}' created successfully.")
    else:
        print(f"Database '{db_name}' already exists.")

    # Close cursor and connection
    cursor.close()
    connection.close()
