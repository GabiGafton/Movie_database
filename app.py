from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
local_db = 'movie_db.db'

@app.route('/')
@app.route('/home')
def home_page():
    movie_data = query_movies()
    return render_template('home.html', movie_data = movie_data)

@app.route('/add')
def add_movie():
    return render_template('add_movie.html')

def query_movies():
    conn = sqlite3.connect(local_db)
    c = conn.cursor()
    c.execute("""
    SELECT * FROM movies
    """)
    movies = c.fetchall()
    return movies

if __name__ == '__main__':
    app.run()
