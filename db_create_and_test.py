import sqlite3

db = 'movie_db.db'

conn = sqlite3.connect(db)
c = conn.cursor()
c.execute("""
select * from movies
""")

movies = c.fetchmany(10)
for i in movies:
    print(i)

conn.commit()
conn.close() 