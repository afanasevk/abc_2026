from helpers.io import logger
from helpers.crypt import caesar_cipher

logger('Проверка логера')

text = 'Привет, мир!'
encrypted = caesar_cipher(text, 1)

print('Исходный текст:', text)
print('Зашифрованный текст:', encrypted)