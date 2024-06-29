import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("select * from users")
user_data = cur.fetchall()
print(user_data)