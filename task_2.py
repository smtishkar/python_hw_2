# Напишите программу, которая получает целое число и возвращает его 
# шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.

num = 234987324
proc_num = num
HEX_DIV = 16 
remainder_of_division = 0
list_of_remains = []

hex_values_dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}


def hex_additiona_numbers_receive (remainder_of_division):
    for key in hex_values_dict:
        if key == remainder_of_division:
            return hex_values_dict[key]


while proc_num > 0:
    temp_remains = proc_num % 16
    proc_num = proc_num // 16
    if temp_remains > 9:
        remainder_of_division = hex_additiona_numbers_receive(temp_remains)
    else:
        remainder_of_division = temp_remains
    list_of_remains.append(remainder_of_division)

hex_num_reversed = ''.join(str(el) for el in list_of_remains)[::-1]
hex_verification = hex(num)


print("Это значение получено при помощи расчета - ", hex_num_reversed)
print("-"*100)
print("Это значение получено при помощи функции - ", hex_verification)