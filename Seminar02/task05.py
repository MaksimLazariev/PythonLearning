"""Задание №5"""
# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a = 5
b = 6
c = 9

discriminant = b**2 - 4 * a* c
print('D = ',discriminant)
x1 = (-b + discriminant ** 0.5)/ 2 * a
x2 = (-b - discriminant ** 0.5)/ 2 * a

print( x1, x2, type(x1), type(x2))