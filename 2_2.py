import nltk
from nltk.tokenize import sent_tokenize


class Text:
    def __init__(self, name):
        self.name = name

    def counting(self):
        with open(self.name) as file:
            text = file.read()
        return f'{len(text)} symbols, {len(text.split())} words, {len(sent_tokenize(text))} sentences'


a = Text('test.txt')
print(a.counting())

