# todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм,
#  4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M в этих единицах (вещественное число).
#  Вывести массу данного тела в килограммах

unit = int(input("unit = "))
m = float(input("m = "))

if unit == 1:
    print(m)
elif unit == 2:
    print(m * 1e-6)
elif unit == 3:
    print(m * 1e-3)
elif unit == 4:
    print(m * 1e3)
elif unit == 5:
    print(m * 1e2)
else:
    print("error")
