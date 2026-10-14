#todo: Напишите лямбду функцию которая возвращает максимальное число
# из 2 переданных чисел
max_num = lambda a, b: a if a > b else b
print(f"test lambda (a = 10, b = 20) max = {max_num(10, 20)}")
print("________________________________________")

# #todo: Для каждого значения из списка mass получите
# # список проверок(True или False) вхождений значений в диапазон от 1 до 130
mass = [122, 23, 1425, 23, 768, 4, 67, 998, 4, 6, 867]
print(mass)
print(list(map(lambda x: 1<=x<=130, mass)))
print("________________________________________")

#todo: Отсортируйте список с помощью функции filter()
# и получите итоговый список только нечетных значений
list_ = [ 10, 11, 14, 25, 33, 36, 100, 101 ]
print(list(filter( lambda val:  val%2 != 0,  list_ )))
print("________________________________________")


#todo: Отсортируйте список по расширению ".mp3"
files = ['file.txt', 'file2.mp3', 'file.pdf', 'file3.mp3', '.mp3le.doc']
print(files)
print(list(filter(lambda file: file.endswith('.mp3'), files)))

