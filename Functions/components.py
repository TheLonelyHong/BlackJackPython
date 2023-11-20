from tkinter import *

def container(y , padx , pady):
    frame = Frame(
        highlightbackground="red",
        highlightthickness=1,
        height=y
    )

    frame.pack(fill=X , padx= padx , pady=pady)
    return frame


class label:
    def __init__(self , master:Frame , word , size , bg , position):
        self.master = master
        self.word = word
        self.width = size[0]
        self.height = size[1]
        self.bg = bg
        self.x_position = position[0]
        self.y_position = position[1]
    
    def create(self):
        label = Label(
            master = self.master,
            text=f" {self.word} ",
            width=self.width,
            height=self.height,
            bg=f"{self.bg}"
        )

        label.place(x = self.x_position , y = self.y_position)
        return label


class button:
    def __init__(self , master:Frame , word , size , bg , position):
        self.master = master
        self.word = word
        self.width = size[0]
        self.height = size[1]
        self.bg = bg
        self.x_position = position[0]
        self.y_position = position[1]
    
    def create(self , command):
        button = Button(
            master=self.master,
            text=f" {self.word} ",
            width=self.width,
            height=self.height,
            bg=self.bg,
            command=command,
        )

        button.place(x = self.x_position , y = self.y_position)
    
    
        