from uzwords import words
from difflib import get_close_matches


def check_words(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(set(get_close_matches(word, words)))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(set(get_close_matches(word, words)))

    return {'available': available, "matches": matches}


if __name__ == "__main__":
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

    print(get_close_matches("ҳато", words, n=5))
    print(get_close_matches("ҳато", words))
    print('-' * 100)

    print(check_words("ҳато", words))
    print(check_words("тариҳ", words))
    print(check_words("хато", words))
    print(check_words("олма", words))
    print(check_words("ҳат", words))
    print(check_words("ҳайт", words))
    print('-' * 100)
