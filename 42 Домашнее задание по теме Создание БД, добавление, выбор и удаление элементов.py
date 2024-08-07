# not_telegram.db
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)',
                   (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

connection.commit()

# input()  # check Database
cursor.execute('SELECT COUNT(*) FROM Users')
for i in range(1, cursor.fetchall()[0][0], 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?',
                   (500, i))
connection.commit()

# input()  # check Database
cursor.execute('SELECT COUNT(*) FROM Users')
for i in range(1, cursor.fetchall()[0][0]+1, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

connection.commit()

result = cursor.execute('SELECT username, email,age, balance FROM Users WHERE age <> ?',(60,))
for i in result:
    print(f'Имя: {i[0]} | Почта: {i[1]} | Возраст: {i[2]}  | Баланс: {i[3]} ')


connection.close()
