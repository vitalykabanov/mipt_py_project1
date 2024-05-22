import random

class TextGenerator(object):
    def __init__(self):
        self.words = []
        self.texts = []

    def get_test(self, level: str) -> str:
        if level == 'Легкий':
            word = random.choice(self.words)
            test = (word[:-1] + ' ') * 9 + word[:-1]
            return test
        if level == 'Средний':
            test = ''
            for i in range(0, 10):
                test += random.choice(self.words)[:-1]
                if i < 9:
                    test += " "
            return test
        if level == 'Сложный':
            return random.choice(self.texts[:-1])
    def from_files(self):
        with open('Слова') as words:
            while True :
                s = words.readline()
                if s == '':
                    break
                self.words.append(s)

        with open('Тексты') as texts:
            while True :
                s = texts.readline()
                if s == '':
                    break
                self.texts.append(s)
