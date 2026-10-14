def caesar_cipher(line, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''

    for char in line:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index - shift) % len(alphabet)
            new_char = alphabet[new_index]

            if char.isupper():
                new_char = new_char.upper()

            result += new_char
        else:
            result += char

    return result