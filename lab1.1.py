import re
print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №1 \nОбчислення в математичних задачах \nВаріант 12 \nЗмінення значень змінних\n")

def is_float(text):
    return bool(re.match(r"^[-+]?(\d*[.])?\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_float(var):
        var = input(prompt)
    return float(var)

choice = ''
while choice.lower() != 'q':
    a = integer_validator("Введіть число a: ")
    b = integer_validator("Введіть число b: ")
    c = integer_validator("Введіть число с: ")

    q = a  # Вводимо допоміжні змінні
    w = b
    e = c
    print("a =", a + b)  # Округлюємо результат до тисячних
    a = q
    print("b =", c - a)
    b = w
    print("c =", a + b + c)
    c = e

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')