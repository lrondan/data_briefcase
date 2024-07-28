import sqlite3
import pandas as pd

conn = sqlite3.Connection('0.8 SQL_for_analyst/DB/retailDB.sqlite')
cursor = conn.cursor()

df_brands = pd.read_sql('select * from `brands`', conn)
df1_brands = pd.DataFrame(data=df_brands)

df_finance = pd.read_sql('select * from `finance`',conn)
df2_finance = pd.DataFrame(data=df_finance)

df_info = pd.read_sql('select * from `info`',conn)
df3_info = pd.DataFrame(data=df_info)

print(df3_info)

conn.close()