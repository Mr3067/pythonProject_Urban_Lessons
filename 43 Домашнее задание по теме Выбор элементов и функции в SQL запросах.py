"""
Для задания 43 Выбор элементов и функции в SQL запросах использовалась база not_telegram1.db

"""

import sqlite3

connection = sqlite3.connect("not_telegram1.db")
cursor = connection.cursor()

cursor.execute('DELETE FROM Users WHERE id = ?',(6,))
connection.commit()
cursor.execute('SELECT COUNT(*) FROM Users')
count_database = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
sum_database = cursor.fetchone()[0]
cursor.execute('SELECT AVG(balance) FROM Users')
avg_database = cursor.fetchone()[0]
# print(count_database,sum_database,avg_database)
print(avg_database)
connection.close()
