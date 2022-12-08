import re
def check_password(password):
    """ Проверяет пароль на корректность (не менее 6 символов, есть хотя бы одна цифра,
        не состоит только из цифр, не содержит слово "password" в любом регистре)
    
        Вход: строка password
        Выход: True, если пройдены все проверки; False
    """
    return (len(password) >= 6 # Проверка длины
        and bool(re.findall(r"\d", password)) # Содержит цифру (можно было бы не преобразовывать к bool, потому что это и так сделал бы if, но раз надо по заданию False, значит bool()
        and bool(re.findall(r"\D", password)) # Содержит что-то, кроме цифры
        and not re.findall(r"[Pp][Aa][Ss]{2}[Ww][Oo][Rr][Dd]", password)) # "В любом регистре" я понял именно так

if check_password(input("Введите пароль для проверки: ")):
    print("+ Ваш пароль удовлетворяет параметрам")
else:
    print("- Ваш пароль некорректный")