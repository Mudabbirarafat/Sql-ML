import sqlite3

try:
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)

    data = [
        ("Aman", 25),
        ("Riya", 22),
        ("Rahul", 30),
        ("Neha", 27),
        ("Ali", 24)
    ]

    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("Users in database:")
    for row in rows:
        print(row)

    conn.commit()

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
    print("Connection closed")
