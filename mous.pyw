import time
from pynput import mouse

from tkinter.tix import *


class Position(object):
    def __init__(self):
        self.string_a = ''
        self.string_b = ''
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.right:
            if pressed:
                self.x1 = x
                self.y1 = y
            else:
                self.x2 = x
                self.y2 = y
                width = self.x2 - self.x1
                height = self.y2 - self.y1
                self.string_a = f'{self.x1}, {self.y1}, {width}, {height}'
                return False
        else:
            if pressed:
                self.string_b = f'{x}, {y}'
            else:
                return False

    def listen(self):
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def start(self):
        self.listen()


def click():
    m = Position()
    m.listen()
    c_time = time.strftime('%H:%M:%S', time.localtime(
        time.time()))
    text.insert(END, c_time)
    if m.string_a != '':
        text.insert(END, m.string_a)
    if m.string_b != '':
        text.insert(END, m.string_b)
    text.insert(END, '\n')
    text.see(END)
    text.update()


root = Tk()
root.geometry('300x200')
root.title('My GUI')
btn = Button(root, text='点击开始', bg='white', fg='blue', command=click)
btn.grid()
text = Listbox(root, width=40, height=10)
text.insert(END, 'mouse left for a position, right for area.')
text.grid()
root.mainloop()


