import sqlite3
from file19950101 import name, magnitud_absol, potentially_hazard, velocidad,distance, body

conn = sqlite3.Connection('0.4 NASA  json/data.db')
cursor = conn.cursor()

cursor.execute('select * from `tabla1`')
cursor.execute('insert into `tabla1` values(?,?,?,?,?,?)',(name, magnitud_absol, potentially_hazard, velocidad,distance, body))
conn.commit()

print(cursor.fetchall())
conn.close()
