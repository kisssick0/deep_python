import typing


def gen_search_string(file: str | typing.TextIO, words: list):
    if isinstance(file, str):
        file = open(file, "r", encoding="utf8")
    lower_words = []
    words = list(set(words))
    for word in words:
        lower_words.append(word.lower())
    for string in file:
        s_words = string.lower().split()
        for word in lower_words:
            if word in s_words:
                yield string
    file.close()
