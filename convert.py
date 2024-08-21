import pandas as pd
import sqlite3

conn = sqlite3.Connection('0.8 PornHub/base_world.sqlite')
df = pd.read_sql('SELECT * FROM actrices', conn)

df.to_csv('./base.csv')