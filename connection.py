import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection string
conn_string = "postgresql+psycopg2://postgres:Sushant28$@localhost:5432/cba"

# Create the database engine
db = create_engine(conn_string)
conn = db.connect()

# Read the Excel file (use the correct Pandas function for Excel files)
df = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\jupyter pandas\commbank_tweets.csv")  # Changed from read_csv to read_excel

# Print dataframe info
print(df.info())

# Write the dataframe to SQL
df.to_sql('commbank_tweets', con=conn, if_exists='replace', index=False)

# Close the connection
conn.close()
