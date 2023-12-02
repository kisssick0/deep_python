from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


def url_handler(url, k):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text_set = text.split()
    counter = Counter(text_set)
    most_occur = dict(counter.most_common(k))
    return json.dumps(most_occur)
