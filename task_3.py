# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

import fractions

# value1 = input("Введите первую дробь: ")      # Если захочется вводить дробь вручную нужно раскомментировать
# value2 = input("Введите вторую дробь: ")      # Если захочется вводить дробь вручную нужно раскомментировать

value1 = "1/2"
value2 = "1/3"


def gcd_caluclation(devider1: int, devider2: int) -> int: 
    if devider1 > devider2: 
        temp = devider2 
    else: 
        temp = devider1 
    for i in range(1, temp + 1): 
        if devider1 % i == 0 and devider2 % i == 0: 
            gcd = i 
    return gcd 

def lcm_calculation(numerator: int, devider: int) -> int : 
    if numerator > devider:
        greater = numerator
    else:
        greater = devider
    while True:
        if greater % numerator == 0 and greater % devider == 0:
            lcm = greater
            break
        greater +=1
    return lcm


value1_splition = value1.split("/")
value2_splition = value2.split("/")
value1_numerator = int (value1_splition[0])
value1_devider = int (value1_splition[1])
value2_numerator = int (value2_splition[0])
value2_devider = int (value2_splition[1])

f1 = fractions.Fraction(value1_numerator, value1_devider)
f2 = fractions.Fraction(value2_numerator, value2_devider)
print("Проверка сложения - ", f1 + f2)
print("Проверка умножения - ", f1 * f2)

# Перемножение дробей
multiplication_numerator = value1_numerator * value2_numerator 
multiplication_devider = value1_devider * value2_devider 
gcd = gcd_caluclation(multiplication_numerator,multiplication_devider)
multiplication_numerator //= gcd 
multiplication_devider //= gcd 
result_multiplication = str(multiplication_numerator), "/", str(multiplication_devider)
result_multiplication = ''.join(result_multiplication) 

# Сложение дробей
lcm = lcm_calculation (value1_devider,value2_devider)
temp_value1 = 1
temp_value2 = 1
if value1_devider != lcm:
    temp_value1 = lcm //value1_devider
    value1_devider *= temp_value1
if value2_devider != lcm:
    temp_value2 = lcm //value2_devider
    value2_devider *= temp_value2

value1_numerator_for_sum = value1_numerator * temp_value1
value2_numerator_for_sum = value2_numerator * temp_value2
common_numerator = (value1_numerator_for_sum+value2_numerator_for_sum)
common_devider = lcm
gcd_for_sum = gcd_caluclation(common_numerator,common_devider)
common_numerator//=gcd_for_sum
common_devider//=gcd_for_sum

result_sum = str(common_numerator), "/", str(common_devider)
result_sum = ''.join(result_sum) 

# print("Это НОК ", lcm)
# print("Это НОД для сложения", gcd_for_sum)
print("Результат вычесления суммы - ", result_sum)
print ("Результат умножения - ", result_multiplication)
