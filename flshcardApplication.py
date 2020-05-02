from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Flashcard")
root.geometry("600x400")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/FlashcardApp/icon.png"))


# Creating Function
def add():  # Addition Function
    pass


def subtract():  # Subtract Function
    pass


def divide():  # Divide Function
    pass


def multiply():  # Multiply Function
    pass


# Defining Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating Menu Items
math_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Math Cards", menu=math_menu)

# Creating Math submenu
math_menu.add_command(label="Add", command=add)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
