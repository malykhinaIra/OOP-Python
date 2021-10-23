import os.path
import re
import string

from nltk.tokenize import sent_tokenize, word_tokenize


class Text:
    """Class that performs statistical processing of a text file"""
    def __init__(self, name):
        if not os.path.isfile(name):
            raise OSError("File does not exist")
        self.name = name

    def __str__(self):
        return f'File consists of {self.symbols()} symbols, {self.words()} words and {self.sentences()} sentences'

    def symbols(self):
        """Returns the amount of symbols in the file"""
        result = 0
        with open(self.name, 'r') as file:
            for st in file:
                result += len(st)
        file.close()
        return result

    def words(self):
        """Returns the amount of words in the file"""
        result = 0
        with open(self.name, 'r') as file:
            for st in file:
                for i in string.punctuation:
                    st = st.replace(i, ' ')
                result += len(word_tokenize(st))
        file.close()
        return result

    def sentences(self):
        """Returns the amount of sentences in the file"""
        result = 0
        with open(self.name, 'r') as file:
            for st in file:
                if not re.findall(r'[A-Za-z]', st):
                    continue
                st = re.sub(r'[?!.]+(\s+[?!.]+)+', '. ', st)
                result += len(sent_tokenize(st))
        file.close()
        return result


a = Text('text.txt')
print(a)
