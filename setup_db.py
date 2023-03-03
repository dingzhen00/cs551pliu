import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('app/movie.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS moive')
print("table dropped successfully");
conn.execute('DROP TABLE IF EXISTS imdbmoive')
print("table dropped successfully");

# drop the data from the table so that if we rerun
conn.execute('CREATE TABLE movie6 ( movie_time TEXT , movie_title TEXT PRIMARY KEY, movie_budget TEXT, domestic_gross TEXT, worldwide_gross TEXT)')
print("table 1 created successfully");
conn.execute('CREATE TABLE imdbmovie6 ( link TEXT PRIMARY KEY, movie_title TEXT, movie_year TEXT,movie_certificate TEXT, movie_time TEXT, movie_genre TEXT, movie_imdbrating TEXT, movie_overview TEXT, meta_score TEXT, director TEXT, star1 TEXT, star2 TEXT, star3 TEXT, star4 TEXT, no_of_notes TEXT, gross TEXT, FOREIGN KEY(movie_title) REFERENCES movie6(movie_title))')

print("table 1 created successfully");



with open('app/dataset/imdb_top_1000.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)
        link = row[0]
        movie_title = row[1]
        movie_year = row[2]
        movie_certificate = row[3]
        movie_time = row[4]
        movie_genre = row[5]
        movie_imdbrating = row[6]
        movie_overview = row[7]
        meta_score = row[8]
        director = row[9]
        star1 = row[10]
        star2 = row[11]
        star3 = row[12]
        star4 = row[13]
        no_of_notes = row[14]
        gross = row[15]
        cur.execute('REPLACE INTO imdbmovie6 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', (link, movie_title, movie_year, movie_certificate, movie_time, movie_genre, movie_imdbrating, movie_overview, meta_score, director, star1, star2, star3, star4, no_of_notes, gross))
        conn.commit()


with open('app/dataset/top_4000_movies_data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)
        movie_time = row[0]
        movie_title = row[1]
        movie_budget = row[2]
        domestic_gross = row[3]
        worldwide_gross = row[4]
        cur.execute('REPLACE INTO movie6 VALUES(?,?,?,?,?)', (movie_time, movie_title, movie_budget, domestic_gross, worldwide_gross))
        conn.commit()


conn.close()