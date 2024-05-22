import keyboardlayout as kl
import keyboardlayout.tkinter as klt
import tkinter.font as tkf

class KeyboardInterface:
    def __init__(self, root):
        key_size = 60
        self.key_info_dict = {
            "margin": 5,
            "txt_color": "black",
            "txt_font": tkf.Font(family='Arial', size=key_size // 4),
            "txt_padding": (key_size // 6, key_size // 10)
        }
        key_info = kl.KeyInfo(**self.key_info_dict, color="grey")

        self.keyboard_layout = klt.KeyboardLayout(
            kl.LayoutName.QWERTY,
            kl.KeyboardInfo(position=(0, 0), padding=2),
            (key_size, key_size),  # width, height,
            key_info,
            master=root
        )

    @staticmethod
    def KeyboardMap(char) -> kl.Key:
        return kl.Key.SPACE if char == ' ' else kl.Key(char)

    def draw_key(self, char: chr):
        key_info_red = kl.KeyInfo(**self.key_info_dict, color="red")
        self.keyboard_layout.update_key(key=KeyboardInterface.KeyboardMap(char), key_info=key_info_red)

    def grey(self, char: str):
        key_info_grey = kl.KeyInfo(**self.key_info_dict, color="grey")
        self.keyboard_layout.update_key(key=KeyboardInterface.KeyboardMap(char), key_info=key_info_grey
