import sqlite3

db = 'movie_db.db'

conn = sqlite3.connect(db)
c = conn.cursor()

conn.commit()
conn.close() 