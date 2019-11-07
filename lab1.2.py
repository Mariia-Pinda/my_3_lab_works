import re
print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №1 \nВикористання математичних формул за виконанням певних умов\n")
print("Варіант 12 \nПеревірка, чи не приводить сумування двох цілих чисел А і В до переповнення\n")

def is_integer(text):
    return bool(re.match(r"^[+-]{0,1}\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)

choice = ''
while choice.lower() != 'q':
    a = integer_validator("Введіть ціле число А: ")
    b = integer_validator("Введіть ціле число B: ")

    if (a + b) <= 32767:
        print("A + B =", a + b)
    else:
        print("Переповнення! Результат не може бути більшим ніж 32 767")

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')