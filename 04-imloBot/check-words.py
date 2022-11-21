from uzwords import words
from difflib import get_close_matches

print(len(words))
print(words[0])
print(words[-1])
print(words[23233])
print('-' * 100)

print(get_close_matches("ҳато", words))
print(get_close_matches("тариҳ", words))
print(get_close_matches("хато", words))
print(get_close_matches("олма", words))
print(get_close_matches("ҳат", words))
print(get_close_matches("ҳайт", words))
print('-' * 100)

