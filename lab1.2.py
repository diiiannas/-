def conv(rast, ed1, ed2):
    zam = {
        "km": 1000,
        "m": 1,
        "sm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "yd": 0.9144,
    }
    meters = rast * zam[ed1]
    result = meters / zam[ed2]
    return result
rast = float(input("Введите расстояние: "))
ed1 = input("Введите исходную единицу измерения (km, m, sm, mm, mi, yd): ")
ed2 = input("Введите целевую единицу измерения (km, m, sm, mm, mi, yd): ")

itog = conv(rast, ed1, ed2)
print(f"{rast} {ed1} = {itog:.2f} {ed2}")