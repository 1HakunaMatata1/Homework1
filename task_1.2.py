# Задача 1.2.
# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

print('')
print('Решение Задачи 1.2 (Пункт A):')
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
random_songs=random.sample(my_favorite_songs,3)
total = random_songs [0][1] + random_songs [1][1] + random_songs [2][1]
print ('Три песни звучат', round(total,2), 'минут')
print('')
print('Дополнительное задание C, три случайные песни:')
print(random_songs[0][0],random_songs[1][0],random_songs[2][0],sep='\n')


# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.
print('')
print('Решение Задачи 1.2 (Пункт B):')
import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
random_songs=random.sample(list(my_favorite_songs_dict), 3)
total = my_favorite_songs_dict[(random_songs[0])] + my_favorite_songs_dict[(random_songs[1])] + my_favorite_songs_dict[(random_songs[2])]
print ('Три песни звучат', round(total,2), 'минут')
print('')
print('Дополнительное задание C, три случайные песни:')
print(*random_songs, sep='\n')
print('')