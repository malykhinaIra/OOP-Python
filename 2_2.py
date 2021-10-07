from nltk.tokenize import sent_tokenize


class Text:
    def __init__(self, name):
        self.name = name
        with open(self.name) as file:
            text = file.read()
        self.symbols = len(text)
        self.words = len(text.split())
        self.sentences = len(sent_tokenize(text))

    def get_result(self):
        return f'{self.symbols} symbols, {self.words} words, {self.sentences} sentences'


a = Text('text.txt')
print(a.get_result())

