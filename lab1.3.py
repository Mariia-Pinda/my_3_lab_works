import re
print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №1 \nОбчислення функції, в залежності від введеного значення х \nВаріант 12 \n")

def is_integer(text):
    return bool(re.match(r"^[-+]{0,1}\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)

choice = ''
while choice.lower() != 'q':
    x = integer_validator("Введіть аргумент функції F(x): ")

    if x <= 3:
        print("Результат обчислення функції: ", round(-x ** 2 + 3 * x + 9, 3))
    else:
        print("Результат обчислення функції: ", round(x / (x ** 2 + 1), 3))

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')