import sqlite3

conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()

#таблицы через sql

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
''')

conn.commit()

# данные

users = ['Karim', 'Ali', 'John', 'Anna', 'Sara']

for user in users:
    cursor.execute('INSERT INTO users (name) VALUES (?)', (user,))

movies = [
    ('Inception', 'Sci-Fi'),
    ('Titanic', 'Drama'),
    ('Avengers', 'Action'),
    ('Joker', 'Drama'),
    ('Interstellar', 'Sci-Fi')
]

for movie in movies:
    cursor.execute('INSERT INTO movies (title, genre) VALUES (?, ?)', movie)

reviews = [
    (1, 1, 9),
    (1, 2, 8),
    (2, 1, 10),
    (2, 3, 7),
    (3, 4, 9),
    (3, 5, 4),
    (4, 2, 6),
    (4, 3, 8),
    (5, 1, 7),
    (5, 5, 2)
]

for review in reviews:
    cursor.execute(
        'INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)',
        review
    )

conn.commit()

#проверка

print('\nUser + Movie + Rating:')

cursor.execute('''
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
''')

for row in cursor.fetchall():
    print(row)

print('\nALL MOVIES (даже без отзывов):')

cursor.execute('''
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
''')

for row in cursor.fetchall():
    print(row)



print('\nAVERAGE RATING:')
cursor.execute('SELECT AVG(rating) FROM reviews')
print(cursor.fetchone())

print('\nMAX RATING:')
cursor.execute('SELECT MAX(rating) FROM reviews')
print(cursor.fetchone())

print('\nMIN RATING:')
cursor.execute('SELECT MIN(rating) FROM reviews')
print(cursor.fetchone())

conn.close()
