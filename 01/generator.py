import typing


def gen_search_string(file: str | typing.TextIO, words: list):
    if isinstance(file, str):
        file = open(file, "r", encoding="utf8")
    lower_words = []
    for word in words:
        lower_words.append(word.lower())
    for string in file:
        l_string = string.lower()
        s_words = l_string.split()
        for word in lower_words:
            if word in s_words or word == l_string:
                yield string
                break
    file.close()


# print(list(gen_search_string('mytext.txt', ['Много собак очень много собак бегут'])))
