from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData

# Define the metadata
metadata = MetaData()

# Define the tweets table
tweets_table = Table(
    'tweets', metadata,
    Column('date', String),
    Column('id', Integer, primary_key=True),
    Column('content', String),
    Column('username', String),
    Column('like_count', Integer),
    Column('retweet_count', Integer)
)

# Create the table in the database
metadata.create_all(engine)
