import sqlite3

try:
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
