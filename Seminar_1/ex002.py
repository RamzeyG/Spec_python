#   Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
#   Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
#   Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def func():
    a = input("Пожалуйста введите число от 2 до 100000\n")
    while int(a) < 2 or int(a) > 100000 or a.isdigit() == False:
        print("Введенные даные не корректны\nПроверьте чтобы число было в диапазоне от 2 до 100000\n")
        a = input("Пожалуйста введите число от 2 до 100000\n")

    count = 0
    a = int(a)
    for i in range(2, a):
        if a%i == 0:
            count = count + 1

    if count < 2:
        print(f"Число {a}  - это простое число")
    else:
        print(f"Число {a}  - не явлется простым числом")



func()