#todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# Для этого считайте список всех строк при помощи метода readlines().

# #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.


source_text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""
with open("inverted_sort.txt", mode="w", encoding="utf-8") as file:
    file.write(source_text)


with open("inverted_sort.txt", mode="r", encoding="utf-8") as file:
    lines = file.readlines()

reversed_lines = lines[::-1]

with open("inverted_sort.txt", mode="a", encoding="utf-8") as file:
    file.write("\n")
    for line in reversed_lines:
        file.write(line.strip() + "\n")
