from random import choice
from string import printable

status = False
while not status:
    long = int(input("Ответ запишите числом. Введите длину пароля: "))
    if long < 7 or long > 20:
        print("Длина не подходит. Пароль должен быть от 7-20 символов. Попробуйте ещё раз")
    else:
        print("Длина подходит. Начинаю генерировать")
        status = True
while status:
    password = "".join([choice(list(printable.strip())) for number in range(long)])
    print(f"Пароль: {password}")
    answer = input("Нравится полученный пароль? ")
    if answer == "да":
        print(f"Отлично! Твой новый пароль: {password}")
        status = False
    elif answer == "нет":
        print("Генерирую новый пароль...")
        continue
    else:
        print("Ошибка")
        break