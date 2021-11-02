import re


def main(case):
    pattern = '8<{P'
    res = len(re.findall(pattern, case))
    return res


tests_main = ['test number 1:8<{P, 8<{P, 8<{O', '8<{P8<{P8<{P8<{P8<{P8<{P', '8<x{P 8x<{P 8<x{P 8<{xP',
              ':-( ;<) X-{O 8<{| 8<{P', 'somerandomwords8<{Psmile']
for i in range(len(tests_main)):
    print(f'Тест №{i + 1}:', tests_main[i])
    print('Результат:', main(tests_main[i]))
    print()

print()
print('-' * 50)
print()


###################################### Доп задание 1
def additional_1(case):
    pattern = '(?:(?:([01]?\d|2[0-3]):):?([0-5]?\d)):?([0-5]?\d)'
    res = re.sub(pattern, '(TBD)', case)
    return res


tests_additional1 = [
    'Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже точно кончится.',
    '23.10.2021 15:00 - начало урока', "00:02:20 - событие", "Конец концерта в 10:00am", "Sun Jun 20 23:21:05 1993"]
for i in range(len(tests_additional1)):
    print(f'Тест №{i + 1}:', tests_additional1[i])
    print('Результат:', additional_1(tests_additional1[i]))
    print()

print()
print('-' * 50)
print()


###################################### Доп задание 2
def func_3x2_5(match):
    return str(3 * (int(match[0]) ** 2) + 5)


def additional_2(case):
    pattern = '\d{1,}'
    res = re.sub(pattern, func_3x2_5, case)
    return res


tests_additional2 = ['20 + 22 = 42', 'пароль состоит из 25 чисел', "ответ к заданию - 33", "кодовое число - 5021",
                     'перевести в 10-ую систему счисления']

for i in range(len(tests_additional2)):
    print(f'Тест №{i + 1}:', tests_additional2[i])
    print('Результат:', additional_2(tests_additional2[i]))
    print()
