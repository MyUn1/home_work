# Задание 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
# with open('file_1.txt', 'w', encoding='utf-8') as file:
#     file.write(input('Введите текст: '))

# Задание 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
# my_file = open('file_2.txt', 'r', encoding='utf-8')
# content = my_file.read()
# print(f'Содержимое файла: \n{content}')
# my_file = open('file_2.txt', 'r', encoding='utf-8')
# content = my_file.readlines()
# print(f'Количество строк в файле - {len(content)}')
# my_file = open('file_2.txt', 'r', encoding='utf-8')
# content = my_file.readlines()
# for i in range(len(content)):
#     print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
# my_file = open('file_2.txt', 'r', encoding='utf-8')
# content = my_file.read()
# content = content.split()
# print(f'Общее количество слов - {len(content)}')
# my_file.close()

# Задание 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

# with open('file_3.txt', 'r', encoding='utf-8') as my_file:
#     surname = []
#     salary = []
#     my_list = my_file.read().split('\n')
#     for i in my_list:
#         i = i.split()
#         if int(i[1]) < 20000:
#             salary.append(i[0])
#             surname.append(i[1])
# print(f'Оклад меньше 20.000 - {salary}, \nСредний оклад равен {sum(map(int, surname)) / len(surname)}')

# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

# rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_file = []
# with open('file_4.txt', 'r', encoding='utf-8') as f:
#     for i in f:
#         i = i.split(' ', 1)
#         new_file.append(rus[i[0]] + ' ' + i[1])
#     print(new_file)
#
# with open('file_4_new.txt', 'w', encoding='utf-8') as f_2:
#     f_2.writelines(new_file)


# Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
# with open('file_5.txt', 'w', encoding='utf-8') as file:
#      line = input('Введите цифры через пробел: \n')
#      file.writelines(line)
#      m_numb = line.split()
#
# print(sum(map(int, m_numb)))

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
# предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
# количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

# subj = {}
# with open('file_6.txt', 'r') as f:
#     for line in f:
#         subject, lecture, practice, lab = line.split()
#         subj[subject] = int(lecture) + int(practice) + int(lab)
#     print(f'Общее количество часов по предмету - \n {subj}')


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
#
# import json
# profit = {}
# pr = {}
# prof = 0
# prof_aver = 0
# i = 0
# with open('file_7.txt', 'r') as file:
#     for line in file:
#         name, firm, earning, damage = line.split()
#         profit[name] = int(earning) - int(damage)
#         if profit.setdefault(name) >= 0:
#             prof = prof + profit.setdefault(name)
#             i += 1
#     if i != 0:
#         prof_aver = prof / i
#         print(f'Средняя прибыль:  {prof_aver:.2f}')
#     else:
#         print(f'Средняя приюыль: отсутсвует. Все работают в убыток')
#     pr = {'Средняя прибыль': round(prof_aver)}
#     profit.update(pr)
#     print(f'Прибыль каждой компании: {profit}')
#
# with open('file_7.json', 'w') as write_js:
#     json.dump(profit, write_js)
#
#     js_str = json.dumps(profit)
#     print(f'Создан файл с расширением json со следующим содержимым: \n '
#           f' {js_str}')