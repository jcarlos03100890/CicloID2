import pandas as pd
from sqlalchemy import create_engine

def insert_table(table_name,df):

    # Step 1: Read CSV File into a Pandas DataFrame
    #csv_file_path = 'your_file.csv'
    #df = pd.read_csv(csv_file_path)

    # Step 2: MySQL Database Connection Parametersd
    # MySQL connection parameters
    db_user = 'data'
    db_password = 'myd4tAUser**'
    db_host = '192.168.100.52'
    db_port = 3306
    # Database name to storage data
    db_name = 'data_analysis'


    # Step 3: Create a SQLAlchemy Engine to Connect to MySQL
    engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    # Step 4: Write DataFrame to MySQL
    df.to_sql(table_name, con=engine, index=False, if_exists='replace')  # Change 'replace' to 'append' if needed

    # Step 5: Close the Database Connection
    engine.dispose()
