# Напишите программу, 
# которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def hex(a):
    b = a%16
    if b > 9:
        if b == 10:
            return 'A'
        if b == 11:
            return 'B'
        if b == 12:
            return 'C'
        if b == 13:
            return 'D'
        if b == 14:
            return 'E'
        if b == 15:
            return 'F'
    else:
        return b

def func(a):
    if(a.isdigit() == True):
        a = int(a)
        number = a
        result = ''
        while a//16 > 0:
            b = hex(a)
            result = str(b) + result
            a = a//16
        result = str(hex(a)) + result
        print(f"Число {number} в 16ричной системе это: {result}")

    else:
        print("Введенное значение не явлется числом\nПовторите запрос")



func(input("Введите десятичное число:\n"))
