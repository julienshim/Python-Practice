import sqlite3
conn = sqlite3.connect("users.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)"
u = input("username: ")
p = input("password: ") # ' OR 1=1-- # end quote and -- to comment out extra quote
c = conn.cursor()

# UNSAFE
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"

# SAFE(R)
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query,(u,p))

result = c.fetchone()
if(result):
	print("welcome")
else:
	print("failed login")

conn.commit()
conn.close()

