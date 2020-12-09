import pyperclip
import random
import string

letter_upper = list(string.ascii_uppercase)
letter_lower = list(string.ascii_lowercase)
digit = list(string.digits)
punctuation = list(string.punctuation)

password = []
password.extend(letter_upper)
password.extend(letter_lower)
password.extend(digit)
password.extend(punctuation)

print(password)