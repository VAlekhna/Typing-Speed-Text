import time
import tkinter
from tkinter import Tk, Label, Entry, Button, Frame
import threading
import random

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#2a3069"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 400


# ---------------------------- LOGIC ------------------------------- #


class SpeedTextGui:
    def __init__(self):
        self.window = Tk()
        self.window.title('Typing Speed Text App')
        self.window.config(bg=GREEN)
        self.window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{WINDOW_WIDTH // 2}+{WINDOW_HEIGHT // 2}')

        self.frame = Frame(self.window)

        self.texts = open("text", "r").read().split("\n")
        self.text_label = Label(self.frame, text=random.choice(self.texts), font=('Arial', 15))
        self.text_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = Entry(self.frame, width=50, font=('Arial', 15))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = Label(self.frame, text="Speed: \n0.00 WPS\n0.00 WPM", font=('Arial', 15))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.reset_button = Button(self.frame, text='Reset', highlightthickness=0, command=self.reset,
                                   font=('Arial', 17))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.frame.pack(expand=1)

        self.count = 0
        self.started = False

        self.window.mainloop()

    def start(self, event):
        if not self.started:
            if event.keycode not in [16, 17, 18]:
                self.started = True
                t = threading.Thread(target=self.timer)
                t.start()
        if not self.text_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg=RED)
        else:
            self.input_entry.config(fg=BLUE)
        if self.input_entry.get() == self.text_label.cget('text'):
            self.started = False
            self.input_entry.config(fg=GREEN)

    def timer(self):
        while self.started:
            time.sleep(0.1)
            self.count += 0.1
            wps = len(self.input_entry.get().split(" ")) / self.count
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{wps:.2f} WPS\n{wpm:.2f} WPM")

    def reset(self):
        self.started = False
        self.count = 0
        self.speed_label.config(text=f"Speed: \n0.00 WPS\n0.00 WPM")
        self.text_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tkinter.END)


SpeedTextGui()
