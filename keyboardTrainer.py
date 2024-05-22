import statistics
import textGenerator

class KeyboardTrainer(object):

    def __init__(self):
        self.level: str = 'Легкий'
        self.stat: statistics = statistics.Statistics()
        self.generator: textGenerator = textGenerator.TextGenerator()
        self.generator.from_files()

    def start_training(self):
        self.stat = statistics.Statistics()
        self.stat.run_time()

    def correct_key_pressed(self):
        self.stat.increace_correct()

    def key_pressed(self):
        self.stat.increace_all_presses()


    def setLevel(self, level: str):
        self.level = level

    def get_speed(self) -> float:
        return self.stat.get_speed()

    def get_accuracy(self) -> float:
        return self.stat.get_accuracy()

    def get_test(self) -> str:
        return self.generator.get_test(self.level)
