import keyboardLayout
from tkinter import *

import keyboardTrainer

class Interface :

    def __init__(self):
        self.trainer = keyboardTrainer.KeyboardTrainer()
        self.root = Tk()
        self.root.geometry("250x150")
        self.start_btn = Button(text='Старт', command=self.start)
        self.start_btn.pack()

        self.test = StringVar()
        self.test_label = Entry(width=100, textvariable=self.test)


        position = {"padx":6, "pady":6, "anchor":NW}
        self.easy_btn = Radiobutton(text='Легкий', value='Легкий', command=lambda: self.trainer.setLevel('Легкий'))
        self.easy_btn.pack(position)
        self.medium_btn = Radiobutton(text='Средний', value='Средний', command=lambda: self.trainer.setLevel('Средний'))
        self.medium_btn.pack(position)
        self.hard_btn = Radiobutton(text='Сложный', value='Сложный', command=lambda: self.trainer.setLevel('Сложный'))
        self.hard_btn.pack(position)

        self.time_label = Label(text='')
        self.accuracy_label = Label(text='')
        self.show_stat()

        self.keyboard_inter = None
        self.root.mainloop()

    def show_stat(self):
        timer = self.trainer.get_speed()
        accuracy = self.trainer.get_accuracy()
        self.time_label.config(text='Скорость: ' + str(timer))
        self.accuracy_label.config(text='Точность: ' + str(accuracy))
        self.time_label.after(1000, self.show_stat)

    def start(self):

        self.trainer.start_training()
        self.time_label.pack()
        self.accuracy_label.pack()
        self.root.bind_all('<Key>', lambda _: self.trainer.key_pressed())
        self.test_label.pack()
        if self.keyboard_inter == None:
            self.keyboard_inter = keyboardLayout.KeyboardInterface(self.root)
        elif self.test.get():
            self.keyboard_inter.grey(self.test.get()[0])
        self.test.set(self.trainer.get_test())
        self.keyboard_inter.draw_key(self.test.get()[0])
        self.root.bind(Interface.map_char(self.test.get()[0]), lambda _: self.correct_key_pressed())

    @staticmethod
    def map_char(char: chr) -> chr:
        return "<space>" if char == ' ' else char

    def correct_key_pressed(self):
        self.trainer.correct_key_pressed()
        self.root.bind(Interface.map_char(self.test.get()[0]), lambda _: None)
        self.keyboard_inter.grey(self.test.get()[0])
        self.test.set(self.test.get()[1:])
        if self.test.get():
            self.root.bind(Interface.map_char(self.test.get()[0]), lambda _: self.correct_key_pressed())
            self.keyboard_inter.draw_key(self.test.get()[0])
        else:
            self.test.set(self.trainer.get_test())
            self.keyboard_inter.draw_key(self.test.get()[0])
            self.root.bind(Interface.map_char(self.test.get()[0]), lambda _: self.correct_key_pressed())
