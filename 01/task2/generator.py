import typing


def gen_search_string(file: str | typing.TextIO, words: list):
    if isinstance(file, str):
        file = open(file, "r", encoding="utf8")
    lower_words = []
    words = list(set(' '.join(words).split()))
    print(words)
    yield_strings = []
    for word in words:
        lower_words.append(word.lower())
    for string in file:
        s_words = string.lower().split()
        for word in lower_words:
            if word in s_words:
                if string not in yield_strings:
                    yield string
                    yield_strings.append(string)
    file.close()


# print(list(gen_search_string('mytext.txt', ['Много собак очень много собак бегут'])))
