from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def converter_10(number, base_now):
    res = 0
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number.find('.') == -1:
        number = number[::-1]
        for i in range(len(number)):
            res += alphabet.find(number[i]) * (int(base_now) ** i)
    else:
        number_int, number_fract = number.split('.')
        number_int = number_int[::-1]
        for i in range(len(number_int)):
            res += alphabet.find(number_int[i]) * (int(base_now) ** i)
        for i in range(len(number_fract)):
            res += alphabet.find(number_fract[i]) * (int(base_now) ** (-1 * (i + 1)))
    return res


def converter(number, base_now, base_new):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    if int(base_now) != 10:
        number = str(converter_10(number, base_now))
    if number.find('.') == -1:
        number_del = int(number)
        while number_del > 0:
            remain = number_del % int(base_new)
            number_del //= int(base_new)
            res.append(alphabet[remain])
        res.reverse()
    else:
        number_int, number_fract = [int(i) for i in number.split('.')]
        if number_int == 0:
            res.append('0')
        while number_int > 0:
            remain = number_int % int(base_new)
            number_int //= int(base_new)
            res.append(alphabet[remain])
        res.reverse()
        res.append(',')
        fract = float('0.' + str(number_fract))
        i = 0
        while fract != 0 and i < 5:
            fract = str(fract * float(base_new))
            fract = fract.split('.')
            res.append(alphabet[int(fract[0])])
            fract = '0.' + fract[1]
            fract = float(fract)
            i += 1
    return res


def fib(n):
    if n <= 1:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))


def fib_converter(number, base_now, base_new):
    if base_now == 'fib':
        number = list(number)
        number.reverse()
        res = 0
        for i in range(len(number)):
            res += int(number[i]) * fib(i + 1)
        if base_now == 10:
            return list(str(res))
        else:
            return converter(str(res), 10, base_new)
    else:
        pass


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fact_converter(number, base_now, base_new):
    if base_new == '!':
        if base_now != 10:
            if base_now == 'fib':
                number = int(''.join(fib_converter(number, base_now, 10)))
            elif base_now == 'berg':
                pass
            else:
                number = converter_10(number, base_now)
        pos = 1
        while True:
            factorial = fact(pos)
            if factorial > int(number):
                pos -= 1
                break
            pos += 1
        res = []
        number = int(number)
        for i in range(pos, 0, -1):
            factorial = fact(i)
            res.append(str(number // factorial))
            number = number % factorial
        return res
    else:
        res = 0
        number = list(number)
        for i in range(len(number)):
            res += int(number[i]) * fact(len(number) - i)
        if base_new == 10:
            return list(str(res))
        else:
            return converter(str(res), 10, base_new)


while True:
    number = input(
        "Введите число( . -разделение между дробной и целой частью, факториальная - '!', фибоначчиева - 'fib', Бергмана - 'berg')\nВыйти - exit\n>> ")
    if number == 'exit':
        break
    base_now = input('Его систему счисления\n>> ')
    base_new = input('Систему счисление для перевода\n>> ')
    print('Ответ: ', end="")

    if base_new == 'fib':
        print(''.join(fib_converter(number, base_now, base_new)))
    elif base_new == '!':
        print(''.join(fact_converter(number, base_now, base_new)))
    elif base_now == 'fib':
        print(''.join(fib_converter(number, base_now, base_new)))
    elif base_now == '!':
        print(''.join(fact_converter(number, base_now, base_new)))
    elif int(base_new) == 10:
        print(converter_10(number, base_now))
    else:
        print(''.join(converter(number, base_now, base_new)))
    print()
    input('Нажмите любую клавишу...')
    clear()
