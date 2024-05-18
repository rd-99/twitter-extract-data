import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('TwitterJanMar.csv')

# Display the first few rows of the DataFrame
print(df.head())
print(type(df.iloc[0]["date"]))
print(len(df))

print(isinstance(df.iloc[0]['id'], str) , isinstance(df.iloc[0]['date'], str) ,isinstance(df.iloc[0]['content'], str) , isinstance(df.iloc[0]['like_count'], float) , isinstance(df.iloc[0]['retweet_count'], float))
print(type(df.iloc[0]['id']) , type(df.iloc[0]['date']) ,type(df.iloc[0]['content']) , type(df.iloc[0]['like_count']) , type(df.iloc[0]['retweet_count']))

for i in range(500035):
    if(isinstance(df.iloc[i]['id'],str)):
        print( 'id')
    if(isinstance(df.iloc[i]['date'] , str)):
        print( 'date' , df.iloc[i]['date'] , type(df.iloc[i]['date']))
    if(isinstance(df.iloc[i]['content'] , str)):
        print( 'content' , df.iloc[i]['content'] , type(df.iloc[i]['content']))
    if(isinstance(df.iloc[i]['like_count'] , float)):
        print( 'LC' ,df.iloc[i]['like_count'] , type(df.iloc[i]['like_count'] ) )
    if(isinstance(df.iloc[i]['retweet_count'],float)):
        print( "RC" , df.iloc[i]['retweet_count'] , type(df.iloc[i]['retweet_count']))