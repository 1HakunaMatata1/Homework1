# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    pass

print ('Решение задачи № 2.3')

number = int(input ('Введите цифру от 0 до 9: '))

def switch_it_up(number):
    digit_name = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return digit_name [number]

print ('switch_it_up', '(', number, ')', '  ->', switch_it_up(number))