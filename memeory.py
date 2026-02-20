import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO test VALUES (1, 'Aman')")

cursor.execute("SELECT * FROM test")
print(cursor.fetchall())

conn.close()
