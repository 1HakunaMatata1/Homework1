# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

print ('Решение Задачи 1.3')
month_name = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month_count = [0,31,28,31,30,31,30,31,31,30,31,30,31]
month = int(input ('Введите номер месяца (от 1 до 12):'))
if (1 <= month <= 12):
    print('Вы выбрали',month_name[month % 12])
    print('В нем', month_count[month] ,'дней')
else:
    print('Месяца с таким номером не существует!')