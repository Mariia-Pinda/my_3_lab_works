import re
print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №2 \n")
print("Програмування циклічних алгоритмів \nОрганізація циклу за допомогою оператора for \n")
print("Варіант 12\n")

def is_integer(x):
    return bool(re.match(r"^[-+]{0,1}\d+$", x))


def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)


def get_integer_greater_than(prompt, number):
    n = integer_validator(prompt)

    while n < number:
        n = integer_validator(prompt)

    return n

choice = ''
while choice.lower() != 'q':
    x = integer_validator("Введіть x (ціле число): ")
    n = get_integer_greater_than("Введіть значення верхньої межі суми n(≥1): ", 1)

    sum = 0
    for i in range(0, n + 1):
        sum += i ** 2 - x ** 2
    print("Результат виконання операції сумування: ", sum)

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')