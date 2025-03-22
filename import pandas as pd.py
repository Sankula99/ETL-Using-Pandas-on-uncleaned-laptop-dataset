import pandas as pd
from sqlalchemy import create_engine
from config import DB_CONFIG

connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@" \
                    f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

engine = create_engine(connection_string)
#read file
csv_file = r"C:\Users\shish\Downloads\archive\laptopData.csv"
df= pd.read_csv(csv_file)

#Missing Value checker for each column
#missing_values = data.isnull().sum()
#print(missing_values)
#print(data.isnull().sum().sort_values(ascending=False))

#Data Cleaning
df.dropna(inplace=True)
missing_values = df.isnull().sum()
print(missing_values)
print(df.isnull().sum().sort_values(ascending=False))

#Data Loading
df.to_sql('TestDBX',con=engine, if_exists='replace',index=False)
query = 'SELECT * FROM "TestDBX" LIMIT 5;'
result = pd.read_sql(query, con=engine)
print(result)