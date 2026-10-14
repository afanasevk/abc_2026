#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.

# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

def numbers_to_letters(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for item in text.split():
        if item.isdigit():
            number = int(item)

            if number == 0:
                result.append(' ')
            elif 1 <= number <= 26:
                result.append(alphabet[number - 1])
            else:
                result.append(item)
        else:
            result.append(item)

    return ''.join(result)


text = input()
print(numbers_to_letters(text))
