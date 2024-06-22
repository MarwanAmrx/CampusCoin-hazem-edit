import  sqlite3

conn = sqlite3.connect("hazem.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS TEST (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
                
                )    ;""")


c.execute(""" 
INSERT INTO TEST (name) VALUES (?)
""" ,(['hazem']) )


conn.commit()

conn = sqlite3.connect("hazem.db")

c = conn.cursor()
data =c.execute(""" 
select * from TEST 
"""  ).fetchall()

print(data)
