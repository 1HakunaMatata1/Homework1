# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    pass

print ('Решение задачи № 2.4 (A):')
s = input ('Введите предложение с восклицательными знаками: ')  
def remove_exclamation_marks(s):
    return s.replace("!" , "")
print ('(', s, ')', '   ->  ', remove_exclamation_marks(s))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass

print ('Решение задачи № 2.4 (B):')
s = input ('Введите предложение с восклицательным знаком в конце: ') 
def remove(s: str):
    return s.rstrip("!")
print ('(', s, ')', '   ->  ', remove(s))