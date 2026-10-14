#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.


text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for shift in range(26):
    result = ''

    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char

    print(shift, result)

# при сдвиге 6 (although that way may not be obvious at first unless you're dutch.)
