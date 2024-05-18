#docker run --name my-postgres -e POSTGRES_PASSWORD=my_password -d -p 5432:5432 postgres

import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, MetaData , BigInteger

# Load the CSV file into a DataFrame
df = pd.read_csv('TwitterJanMar.csv')
df.dropna(subset=['id'])

# Ensure the timestamp column is in datetime format
#df['timestamp'] = pd.to_datetime(df['date'])

# Define your PostgreSQL connection details
username = 'postgres'
password = 'password'
host = 'localhost'
port = '5432'
database = 'postgres'

# Create an SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

# Define the metadata
metadata = MetaData()

# Define the tweets table
tweets_table = Table(
    'tweets', metadata,
    Column('date', String),
    Column('id', String),
    Column('content', String),
    Column('username', String),
    Column('like_count', Integer),
    Column('retweet_count', Integer)
)

# Create the table in the database
metadata.create_all(engine)

# Insert data into the PostgreSQL table
df.to_sql('tweets', engine, if_exists='append', index=False)

print("Data has been inserted successfully.")
