
#1. Задание

my_list = [10, None, 'Hello', -52, True, 14.3]
print(list(map(type, my_list)))

#2.Задание

list1 = input("Введите произвольные элементы через пробел: ").split()
list1[:-1:2], list1[1::2] = list1[1::2], list1[:-1:2]
print(list1)

#3.Задание

seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")


#4. Задание

my_str = input('Введите несколько слов. Разделите слова пробелом : ')

for n, word in enumerate(my_str.split()):
    print(n + 1, (word, word[:11])[len(word) > 10])

#5. Задание.

my_list = [7, 5, 3, 3, 2]
number = int(input("Введите число: "))
a = my_list.count(number)
for element in my_list:
   if a> 0:
        b = my_list.index(number)
        my_list.insert(b+a, number)
        break
    else:
        if number > element:
            c = my_list.index(element)
            my_list.insert(c, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)

#6 Задание. В блоке analitics почему-то выдает ошибку с "единицей измерения".
# Помогите разобраться что не так.

goods = int(input("Введите общее количество товара "))
n = 1
my_dict = []
my_list = []

while n <= goods:
    my_dict = dict(
        {'название': input('Ввведите название товара: '),
        'цена': input('Введите цену товара: '),
        'количество': input('Введите количество данного товара: '),
        'eдиница измерения': input('Введите единицу измерения: ')}
    )
    my_list.append((n, my_dict))
    n += 1

analitics = {
    'название': [],
    'цена': [],
    'количество': [],
    'единица измерения': set()
}

for _, item in my_list:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['количество'].append(item['количество'])
    analitics['единица измерения'].add(item['единица измерения'])

print(my_list)
print(analitics)


