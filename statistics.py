import time

class Statistics:

    def __init__(self):
        self.correct_presses: int = 0
        self.all_presses: int = 0
        self.start_time: int = 0

    def run_time(self):
        self.start_time = time.time()

    def increace_all_presses(self):
        self.all_presses += 1

    def increace_correct(self):
        self.correct_presses += 1

    def get_speed(self) -> float:
        return int(self.correct_presses / (int(time.time()) - int(self.start_time)) * 60) if int(time.time()) - int(self.start_time) != 0 else 0

    def get_accuracy(self) -> float:
        return self.correct_presses / self.all_presses if self.all_presses != 0 else 0
