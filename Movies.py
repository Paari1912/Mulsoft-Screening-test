import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director) VALUES ('Varisu', 'Vijay', 'Rashmika Mandanna', 2023,'Vamshi Paidipally' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('Master', 'Vijay', 'Malavika Mohan', 2021,'Lokesh Kanagaraj' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('Thuppakki', 'Vijay', 'Kajal Aggarwal','2012','A R Murugadoss' )''')
cursor.execute('''INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)VALUES ('Beast', 'Vijay', 'Pooja Hegde', 2022,'Nelson' )''')
cursor.execute('''SELECT * from Movies''')
result = cursor.fetchall();
print(result)
connection.commit()
connection.close()
