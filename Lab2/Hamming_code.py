msg = [int(i) for i in input()]
s1 = (msg[2] + msg[4] + msg[6]) % 2
s2 = (msg[2] + msg[5] + msg[6]) % 2
s3 = (msg[4] + msg[5] + msg[6]) % 2
wrong = 0
if s1 != msg[0]:
    wrong += 1
if s2 != msg[1]:
    wrong += 2
if s3 != msg[3]:
    wrong += 4
if wrong > 0:
    print(f'Ошибка в {wrong} бите')
    if msg[wrong - 1] == 0:
        msg[wrong - 1] = 1
    else:
        msg[wrong - 1] = 0
else:
    print('Ошибок нет')
print("Правильные биты(информационные биты):", end="")
for i in range(len(msg)):
    if i != 0 and i != 1 and i != 3:
        print(msg[i], end='')