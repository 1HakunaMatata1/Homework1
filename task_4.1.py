# Задача 4.1.
# Домашнее задание на SQL

print ('Решение Задачи 4.1:', '\n')

import sqlite3

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student (Student_Id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM Students JOIN School ON Students.School_Id = School.School_Id WHERE Student_Id = ?'
    cursor.execute(sqlquery, (Student_Id,))
    student_info = cursor.fetchall()
    print ('\n', "Данные по студенту:")
    for row in student_info:
      print ("ID Студента:", row[0])
      print ("Имя Студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", row[4], '\n')

    close_connection(con)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка вида ", error)

x = int(input('Введи ID Студента от 201 до 204:  '))
if x in (201,202,203,204):
    get_student(x)
else: print ('Студента с таким ID нет в списке!')