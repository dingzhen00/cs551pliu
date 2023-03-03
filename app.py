import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# database details - to remove some duplication
db_name = 'movie.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movie')
def movie():
    conn = sqlite3.connect('movie.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute("select * from movie6")
    rows = cur.fetchall()
    conn.close()
    return render_template('movie.html', rows=rows)


@app.route('/imdbmovie')
def imdbmovie():
    conn = sqlite3.connect('movie.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from orders
    cur.execute("select * from imdbmovie6")
    rows = cur.fetchall()
    conn.close()
    return render_template('imdbmovie.html', rows=rows)
