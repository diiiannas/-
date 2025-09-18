a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))
p = (a + b + c) / 2
s = ( p * (p - a) * (p - b) * (p - c)) ** 0.5
print(f'Площадь треугольника равна:  {s:.2f} ')

