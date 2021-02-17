
import sqlite3

# подключаемся к базе данных начало
conn = sqlite3.connect("users.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
# подключаемся к базе данных конец

# добавляем пользователя начало
# Вставляем множество данных в таблицу используя безопасный метод "?"
users = [('Петрова Ирина3', '0987678', '24.12.1999', 'Женский')]

cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
conn.commit()
# добавляем пользователя конец

# удаляем пользователя начало
sql = "DELETE FROM users WHERE name = 'Петрова Ирина3'"
 
cursor.execute(sql)
conn.commit()
# удаляем пользователя конец