#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

a = int(input())
b = int(input())
c = int(input())

ac = abs(a - c)
bc = abs(b - c)

print(f"ac = {ac}")
print(f"bc = {bc}")

print(f"sum = {ac + bc}")