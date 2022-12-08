flag = True

def fibonacci(n):
    """
        Принимает: порядковый номер числа Фибоначчи (нумерация с нуля)
        Возвращает: число Фибоначчи
    """
    try: # Проверка того, что передано функции (потому что ввод с консоли). К сожалению, NameError при вызове fibonacci(имя необъявленной функции или переменной) из консоли я обработать не могу. Если это возможно, подскажите, как это можно сделать
        n = int(n)
        if n < 0: raise IndexError
    except:
        print("Ошибка: Порядковый номер числа должен быть целым неотрицательным числом")
        return fibonacci(input("Введите порядковый номер еще раз: "))
    
    global flag
    if flag:
        print(n, "`е число Фибоначчи = ", end = "", sep = "")
        flag = False
    
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2) # Более оптимальный вариант

#Примеры вызова функции:
#fibonacci(4)
#fibonacci(-1)
#fibonacci(0)
#fibonacci("str")