import tkinter as tk
import random
import time

# Maxim Chopivskyy
# 118364841

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.score = 0
        self.first_press = True
        self.createLabel()
        self.createCanvas()
        self.createStart()

        self.grid()

    def createLabel(self):
        self.lab = tk.Label(self, text='score: ' + str(self.score))
        self.lab.pack()

    def createCanvas(self):
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

    def createStart(self):
        self.but = tk.Button(self, text="Start", command=self.start)
        self.but.pack()

    def start(self):
        self.score = 0

        if self.first_press:
            rand_x1, rand_y1 = random.randint(1, 350), random.randint(1, 350)
            self.shape = self.canvas.create_rectangle(rand_x1, rand_y1, rand_x1 + 50, rand_y1 + 50, fill='red')  # put shape in random place
            self.canvas.tag_bind(self.shape, "<Button-1>", self.press)
            self.start_time = time.time()
            self.first_press = False

        else:
            rand_x1, rand_y1 = random.randint(1, 350), random.randint(1, 350)
            self.canvas.coords(self.shape, rand_x1, rand_y1, rand_x1 + 50, rand_y1 + 50)

            self.lab.configure(text='score: ' + str(self.score))

            self.start_time = time.time()

    def press(self, shape):
        elapsed = time.time() - self.start_time
        print(elapsed)

        if elapsed < 2:
            self.score += 1
        rand_x1, rand_y1 = random.randint(1, 350), random.randint(1, 350)
        self.lab.configure(text='score: ' + str(self.score))

        self.canvas.coords(self.shape, rand_x1, rand_y1, rand_x1 + 50, rand_y1 + 50)

        self.start_time = time.time()

app = Application()
app.master.title('GUI application')
app.mainloop()