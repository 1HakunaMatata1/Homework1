# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

print ('Решение Задачи 3.1:', '\n')

print('Введите число колонок матрицы: ')
x = int(input())
print('Введите число строк матрицы: ')
y = int(input())

class Matrix:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.data = [[None for _ in range(columns)] for _ in range(rows)]
    
    def set_value(self,row,column,value):   # Функция принятия новых значений и замена существующих
        self.data[row][column] = value

    def get_value(self,row,column):         # Функция вывода значения нужной ячейки по индексам
        return self.data[row][column]
    
    def print_size(self):                   # Функция печати числа строк и столбцов матрицы
        print('\n','Размер матрицы:', 'строк -', self.rows, 'колонок -', self.columns)        

matrix = Matrix(y,x) #задаем размер матрицы по введенным значениям

matrix.print_size() #выводим размер матрицы

print('\n','Введите номер колонки ячейки, значение которой хотите поменять от 0 до', int(x), ':')
s = int(input())-1
print('Введите номер строки этой ячейки от 0', 'до', int(y), ':')
p = int(input())-1
print('Введите новое значение этой ячейки :')
q = int(input())

matrix.set_value(p, s, q)

print('Проверяем! Новое значение ячейки в строке', (p+1), 'колонки', (s+1), 'равно', matrix.get_value(p,s))
