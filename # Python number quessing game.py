# Python number quessing game

import random

number = random.randint (1,100)
usernumber = 0
attempt = 0

print(number)
print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")

while (True):
    try:
        usernumber = int(input("Введи свою догадку: "))
    except ValueError:
        print("Ошибка: пожалуйста, введите целое число!")
        continue  # Возвращаемся к началу цикла

    if usernumber == number:
        attempt+=1
        print(f"Поздравляю! Ты угадал число за {attempt} попытки.")
        choise = input("Хочешь сыграть ещё раз? (да/нет): ").lower()
        if choise == "да":
            number = random.randint (1,100)
            attempt = 0 # Сброс количества попыток
        elif choise == "нет":
            break
        else:
            while choise != "да" and choise != "нет":
                choise = input("Введите Да!/Нет: ").lower()
                if choise == "да":
                       number = random.randint (1,100)
                       attempt = 0 # Сброс количества попыток
                elif choise == "нет":
                    break


    elif usernumber > number:
        print("Загаданное число меньше, попробуй ещё раз.")
        attempt+=1

    elif usernumber < number:
        print("Загаданное число больше, попробуй ещё раз.")
        attempt+=1



# Верный код

# import random

# number = random.randint(1, 100)
# usernumber = 0
# attempt = 0

# print(number)  # Можно убрать после отладки
# print("Привет! Я загадал число от 1 до 100. Попробуй угадать!")

# while True:
#     try:
#         usernumber = int(input("Введи свою догадку: "))
#     except ValueError:
#         print("Ошибка: пожалуйста, введите целое число!")
#         continue  # Возвращаемся к началу цикла

#     if usernumber == number:
#         attempt += 1  # Увеличиваем попытки при успешной догадке
#         print(f"Поздравляю! Ты угадал число за {attempt} попытки.")
#         choice = input("Хочешь сыграть ещё раз? (да/нет): ").lower()
#         if choice == "да":
#             number = random.randint(1, 100)  # Загадываем новое число
#             attempt = 0  # Сброс количества попыток
#         elif choice == "нет":
#             break
#         else:
#             while choice != "да" and choice != "нет":
#                 choice = input("Введите да или нет: ").lower()
#             if choice == "да":
#                 number = random.randint(1, 100)
#                 attempt = 0
#             elif choice == "нет":
#                 break

#     elif usernumber > number:
#         print("Загаданное число меньше, попробуй ещё раз.")
#         attempt += 1

#     elif usernumber < number:
#         print("Загаданное число больше, попробуй ещё раз.")
#         attempt += 1