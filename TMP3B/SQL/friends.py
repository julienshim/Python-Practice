import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

# execute some sql
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends 
# 					VALUES ('Merriwether', 'Lewis', 7)'''

# form_first = "Dana"
# DO NOT DO THE FOLLOWING QUERY
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
# BETTER QUERY
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))

data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)

# BULK ADD
# for person in people: # instead of data, pulling
# 	c.execute("INSERT INTO friends VALUES (?,?,?)", person)

# QUERY
# c.executie('QUERY')
# for result in c:
#     print(c)

# print(c.fetchone())
# print(c.fetchall())

# commit changes
conn.commit()
conn.close()



