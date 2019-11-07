import re
print("Пінда Марія Володимирівна \nГрупа КМ-92 \nЛабораторна робота №2 \n")
print("Програмування циклічних алгоритмів \nОрганізація циклу за допомогою оператора while \n")
print("Варіант 12\n")

def is_integer(text):
    return bool(re.match(r"^[-+]{0,1}\d+$", text))

def integer_validator(prompt):
    var = input(prompt)
    while not is_integer(var):
        var = input(prompt)
    return int(var)

def get_integer_greater_than(prompt, number):
    digit = integer_validator(prompt)
    while digit <= number:
        digit = integer_validator(prompt)
    return digit

choice = ''
while choice.lower() != 'q':
    dividend = get_integer_greater_than("Введіть ділене (ціле додатне число): ", 0)
    divider = get_integer_greater_than("Введіть дільник (ціле додатне число): ", 0)

    quotient = 0

    if dividend < divider:
        print("частка = 0", "остача = " + str(dividend))
    while dividend >= divider:
        dividend = dividend - divider
        quotient = quotient + 1
        modulo = dividend
    print("частка = ", str(quotient), "остача = ", str(modulo))

    choice = input("Для виходу з програми натисніть Q, а для продовження іншу клавішу: ")
    if choice.lower() != "q":
        print('\n', 'Наступна спроба: ', '\n')