# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.


def func(a, b):
    a = a.split('/')
    b = b.split('/')
    def func1(a, b):
        c = [0, 0]
        c[0] = int(a[0]) * int(b[0])
        c[1] = int(a[1]) * int(b[1])

        print(f"{a[0]}/{a[1]} * {b[0]}/{b[1]} = {c[0]}/{c[1]}")
    def func2(a, b):
        c = [0, 0]
        y = 1
        while((int(a[1])*y)%int(b[1]) != 0):
            y = y + 1
        x = y * int(a[1]) / int(b[1])
        c[1] = y * int(a[1])
        c[0] = int(a[0])*y + int(b[0])*x
        print(f"{a[0]}/{a[1]} + {b[0]}/{b[1]} = {int(c[0])}/{c[1]}")




    func1(a, b)
    func2(a, b)

    # print(a, b)




func("1/3", "3/8")
func("15/63", "18/76")