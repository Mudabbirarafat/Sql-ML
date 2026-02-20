import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
               
               
""")

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Aman", 25))
conn.commit()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
