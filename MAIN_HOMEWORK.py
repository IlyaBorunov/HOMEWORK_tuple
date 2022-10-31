from random import randint

print('=================================================')
print('\t\t1 - TASK')
print('=================================================')

user_num = input('Please, enter your number: ')

if user_num.count('0') > 0:
    print(f'{user_num.count("0")} - The quantity of "0"')
else:
    print('There are no "0"')

print('=================================================')
print('\t\t2 - TASK')
print('=================================================')

user_num_2task = int(input('Please, enter your number:'))

counter = 0
while user_num_2task % 10 == 0:
    user_num_2task /= 10
    counter += 1
if counter > 0:
    print(f'{counter} - The quantity of "0"')
else:
    print('There are no "0" in the end.')


print('=================================================')
print('\t\t3 - TASK')
print('=================================================')

# Сгенерируем два листа с помощью рандома

first_rand_list = [randint(100, 999) for i in range(16)]
second_rand_list = [randint(0, 100) for i in range(16)]
print(f'Первый список -- {first_rand_list}')
print(f'Второй список -- {second_rand_list}')
del first_rand_list[1::2]
del second_rand_list[::2]

third_task_result = first_rand_list + second_rand_list

print(f'Результат -- {third_task_result}')

print('=================================================')
print('\t\t4 - TASK')
print('=================================================')

my_fourth_task_list = [randint(100, 999) for i in range(16)]

print(f'Original list -- {my_fourth_task_list}')

my_fourth_task_list = my_fourth_task_list[1::] + my_fourth_task_list[0:1]

print(f'New list -- {my_fourth_task_list}')

print('=================================================')
print('\t\t5 - TASK')
print('=================================================')

my_fifth_task_list = [randint(100, 999) for i in range(16)]

print(f'Original list -- {my_fifth_task_list}')

first_index_value = my_fifth_task_list.pop(0)

my_fifth_task_list.append(first_index_value)

print(f'New list -- {my_fifth_task_list}')

print('=================================================')
print('\t\t6 - TASK')
print('=================================================')

sixth_task_str = f'{randint(50, 100)} больше чем {randint(0, 49)} но меньше чем {randint(101, 200)}'

sixth_task_list = sixth_task_str.split()

counter_int = 0

for i in range(len(sixth_task_list)):
    if sixth_task_list[i].isdigit() is True:
        counter_int += int(sixth_task_list[i])



print(f'Строка: {sixth_task_str}')
print(f'{counter_int} -- СУММА')

print('=================================================')
print('\t\t8 - TASK')
print('=================================================')

eighth_task_str = input('Please enter something:')

eighth_task_list = list(eighth_task_str)

eighth_task_result = []
for i in range(0, len(eighth_task_list), 2):
    if i < len(eighth_task_list) - 1:
        eighth_task_result.append(eighth_task_list[i] + eighth_task_list[i + 1])
    else:
        eighth_task_result.append(eighth_task_list[i] + '_')

print(eighth_task_result)

print('=================================================')
print('\t\t10 - TASK')
print('=================================================')

my_tenth_task_list = ['1', '24', 3, '43', 5, '66', 7, '81', 9, 1, '2', 3, 4, '5', 6, 7, '8', 9]

new_tenth_task_list = []

for i in range(0, len(my_tenth_task_list)):
    if type(my_tenth_task_list[i]) == str:
        new_tenth_task_list.insert(i, my_tenth_task_list[i])


print(f'{my_tenth_task_list} - old list')

print(f'{new_tenth_task_list} - new list')

print('=================================================')
print('\t\t11 - TASK')
print('=================================================')

# Строка: стих Шевченко


eleventh_task_str = 'За думою дума роєм вилітає,\n' \
                    'Одна давить серце, друга роздирає,\n' \
                    'А третяя тихо, тихесенько плаче \n' \
                    'У самому серці, може, й Бог не бачить.'

print(f' СТРОКА:\n{eleventh_task_str}')
eleventh_task_str2 = 'За думою дума роєм вилітає,' \
                    ' Одна давить серце, друга роздирає,' \
                    ' А третяя тихо, тихесенько плаче У самому серці,' \
                    ' може, й Бог не бачить.'


eleventh_task_str2 = set(eleventh_task_str2)
eleventh_task_str2 = list(eleventh_task_str2)
print()
print(f'СПИСОК УНИКАЛЬНЫХ ЭЛЕМЕНТОВ СТРОКИ:\n{eleventh_task_str2}')

print('=================================================')
print('\t\t12 - TASK')
print('=================================================')

# Придумаем две строки

twelfth_task_str_1 = 'udoghegegahbvsaihhsehsa8ee'
twelfth_task_str_2 = 'rihjgtuhbdrubshlieshebiaso'
print(f' Первая строка -- {twelfth_task_str_1}')
print(f' Вторая строка -- {twelfth_task_str_2}')

twelfth_task_str_1 = set(twelfth_task_str_1)
twelfth_task_str_2 = set(twelfth_task_str_2)

twelfth_task_result = twelfth_task_str_1.intersection(twelfth_task_str_2)
twelfth_task_result = list(twelfth_task_result)
print(f' Результат -- {twelfth_task_result}')

print('=================================================')
