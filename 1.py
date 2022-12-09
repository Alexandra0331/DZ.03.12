# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001

# out
# 8.988
 
a = float(input("Введите число: ")) # 9
n = int(input("Введите количество знаков после запятой: ")) # 0.000001  6 знаков
template = '{:.' + str(n) + 'f}'
print(template.format(a))



# не понятно, как Decimal работает (((
from decimal import Decimal
x = Decimal(input("Ввведите число: ")) # 8.98785
print(x)           
print(Decimal(str(x)[:8]))   #  8.987