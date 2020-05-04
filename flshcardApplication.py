import random
from tkinter import *
from random import randint, randrange  # This will create random integers
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Flashcard")
root.geometry("630x400")
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/FlashcardApp/icon.png"))

my_label = Label(root, text="Select any card from menu", font=("Arial, 30"))
my_label.pack(pady=120)

#####################
# Creating Function #
#####################

#################
# About Section #
#################

def about_window():
    new = Toplevel()
    new.title("About")
    new.geometry("400x400")
    new.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/FlashcardApp/about.png"))







    new.mainloop()

#################
# Close Program #
#################


def quit_app():
    response1 = messagebox.askquestion("Question", "Do you want to close the program ?")
    if response1 == "yes":
        root.quit()
    else:
        pass

######################
# Addition Operation #
######################


def add_correct(num1, num2):  # Checking the answer correct or not
    # Calculating the right answer
    correct = num1 + num2

    # Checking correct or wrong
    if int(addition_entry.get()) == correct:
        response2 = messagebox.showinfo("Result", "You are right the Correct Answer is " + str(correct) + "\n\nNow solve this next question")

    else:
        response2 = messagebox.showerror("Result", "Your Answer is Incorrect\nThe Correct Answer is " + str(correct)+" , not "+str(addition_entry.get())+"\n\nNow solve this next question")
    # Clear the answer entry box
    addition_entry.delete(0, "end")

    # Generate 2 new random numbers
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))
    addition_flash.config(text=str(num_1.get()) + " + " + str(num_2.get())+" =", font=("Arial", 32), bg="cyan", fg="black")


def addition():  # Addition Function
    hide_frames()
    addition_frame.pack(fill="both", expand=1)

    # Creating Random Integer Numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))

    # Putting the numbers on screen
    global addition_flash
    addition_flash = Label(addition_frame, text=str(num_1.get()) + " + " + str(num_2.get()) + " =", font=("Arial", 32), bg="cyan", fg="black")
    addition_flash.grid(row=0, column=0, padx=30, pady=80)

    # Creating Answer EntryBox
    global addition_entry
    addition_entry = Entry(addition_frame, font=("Arial", 32), width=8)
    addition_entry.grid(row=0, column=1, padx=5, pady=80)

    # Adding Submit Button
    submit_btn = Button(addition_frame, text="Submit", font=("Arial", 28), command=lambda: add_correct(num_1.get(), num_2.get()))
    submit_btn.grid(row=0, column=2, padx=10)

    # Creating Correct and Incorrect Label
    global add_correct_label
    add_correct_label = Label(addition_frame, text="Enter Your Answer Above", font=("TSCu_Comic", 32), bg="cyan", fg="red")
    add_correct_label.grid(row=1, column=0, columnspan=3)

#########################
# Subtraction Operation #
#########################


def subtract_correct(num1, num2):  # Checking the answer correct or not
    # Calculating the right answer
    correct = num1 - num2

    # Checking correct or wrong
    if int(subtraction_entry.get()) == correct:
        response2 = messagebox.showinfo("Result", "You are right the Correct Answer is " + str(correct) + "\n\nNow solve this next question")

    else:
        response2 = messagebox.showerror("Result", "Your Answer is Incorrect\nThe Correct Answer is " + str(correct)+" , not "+str(subtraction_entry.get())+"\n\nNow solve this next question")
    # Clear the answer entry box
    subtraction_entry.delete(0, "end")

    # Generate 2 new random numbers
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))
    subtraction_flash.config(text=str(num_1.get()) + " - " + str(num_2.get())+" =", font=("Arial", 32), bg="yellow", fg="black")


def subtract():  # Subtract Function
    hide_frames()
    subtract_frame.pack(fill="both", expand=1)

    # Creating Random Integer Numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))

    # Putting the numbers on screen
    global subtraction_flash
    subtraction_flash = Label(subtract_frame, text=str(num_1.get()) + " - " + str(num_2.get()) + " =", font=("Arial", 32), bg="yellow", fg="black")
    subtraction_flash.grid(row=0, column=0, padx=30, pady=80)

    # Creating Answer EntryBox
    global subtraction_entry
    subtraction_entry = Entry(subtract_frame, font=("Arial", 32), width=8)
    subtraction_entry.grid(row=0, column=1, padx=5, pady=80)

    # Adding Submit Button
    submit_btn = Button(subtract_frame, text="Submit", font=("Arial", 28), command=lambda: subtract_correct(num_1.get(), num_2.get()))
    submit_btn.grid(row=0, column=2, padx=10)

    # Creating Correct and Incorrect Label
    global subtract_correct_label
    subtract_correct_label = Label(subtract_frame, text="Enter Your Answer Above", font=("TSCu_Comic", 32), bg="yellow", fg="blue")
    subtract_correct_label.grid(row=1, column=0, columnspan=3)

######################
# Division Operation #
######################


def division_correct(num1, num2):  # Checking the answer correct or not
    # Calculating the right answer
    correct_float = num1 / num2
    correct = int(correct_float)

    # Checking correct or wrong
    if int(division_entry.get()) == correct:
        response2 = messagebox.showinfo("Result", "You are right the Correct Answer is " + str(correct) + "\n\nNow solve this next question")

    else:
        response2 = messagebox.showerror("Result", "Your Answer is Incorrect\nThe Correct Answer is " + str(correct)+" , not "+str(division_entry.get())+"\n\nNow solve this next question")
    # Clear the answer entry box
    division_entry.delete(0, "end")

    # Generate 2 new random numbers
    num_1.set(randint(1, 100))
    if num_1.get() % 2 == 0:
        num_2.set(2)
    if num_1.get() % 3 == 0:
        num_2.set(3)
    if num_1.get() % 5 == 0:
        num_2.set(5)
    if num_1.get() % 7 == 0:
        num_2.set(7)
    if num_1.get() % 11 == 0:
        num_2.set(11)
    if num_1.get() % 13 == 0:
        num_2.set(13)
    if num_1.get() % 17 == 0:
        num_2.set(17)
    if num_1.get() % 19 == 0:
        num_2.set(19)
    if num_1.get() % 23 == 0:
        num_2.set(23)
    if num_1.get() % 29 == 0:
        num_2.set(29)
    if num_1.get() % 31 == 0:
        num_2.set(31)
    if num_1.get() % 37 == 0:
        num_2.set(37)
    if num_1.get() % 41 == 0:
        num_2.set(41)
    if num_1.get() % 43 == 0:
        num_2.set(43)
    if num_1.get() % 47 == 0:
        num_2.set(47)
    if num_1.get() % 53 == 0:
        num_2.set(53)
    if num_1.get() % 59 == 0:
        num_2.set(59)
    if num_1.get() % 61 == 0:
        num_2.set(61)
    if num_1.get() % 67 == 0:
        num_2.set(67)
    if num_1.get() % 71 == 0:
        num_2.set(71)
    if num_1.get() % 73 == 0:
        num_2.set(73)
    if num_1.get() % 79 == 0:
        num_2.set(79)
    if num_1.get() % 83 == 0:
        num_2.set(83)
    if num_1.get() % 89 == 0:
        num_2.set(89)
    if num_1.get() % 97 == 0:
        num_2.set(97)
    division_flash.config(text=str(num_1.get()) + " / " + str(num_2.get())+" =", font=("Arial", 32), bg="green", fg="black")

def divide():  # Divide Function
    hide_frames()
    divide_frame.pack(fill="both", expand=1)

    # Creating Random Integer Numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(1, 100))
    if num_1.get() % 2 == 0:
        num_2.set(2)
    if num_1.get() % 3 == 0:
        num_2.set(3)
    if num_1.get() % 5 == 0:
        num_2.set(5)
    if num_1.get() % 7 == 0:
        num_2.set(7)
    if num_1.get() % 11 == 0:
        num_2.set(11)
    if num_1.get() % 13 == 0:
        num_2.set(13)
    if num_1.get() % 17 == 0:
        num_2.set(17)
    if num_1.get() % 19 == 0:
        num_2.set(19)
    if num_1.get() % 23 == 0:
        num_2.set(23)
    if num_1.get() % 29 == 0:
        num_2.set(29)
    if num_1.get() % 31 == 0:
        num_2.set(31)
    if num_1.get() % 37 == 0:
        num_2.set(37)
    if num_1.get() % 41 == 0:
        num_2.set(41)
    if num_1.get() % 43 == 0:
        num_2.set(43)
    if num_1.get() % 47 == 0:
        num_2.set(47)
    if num_1.get() % 53 == 0:
        num_2.set(53)
    if num_1.get() % 59 == 0:
        num_2.set(59)
    if num_1.get() % 61 == 0:
        num_2.set(61)
    if num_1.get() % 67 == 0:
        num_2.set(67)
    if num_1.get() % 71 == 0:
        num_2.set(71)
    if num_1.get() % 73 == 0:
        num_2.set(73)
    if num_1.get() % 79 == 0:
        num_2.set(79)
    if num_1.get() % 83 == 0:
        num_2.set(83)
    if num_1.get() % 89 == 0:
        num_2.set(89)
    if num_1.get() % 97 == 0:
        num_2.set(97)
    # Putting the numbers on screen
    global division_flash
    division_flash = Label(divide_frame, text=str(num_1.get()) + " / " + str(num_2.get()) + " =", font=("Arial", 32), bg="green", fg="black")
    division_flash.grid(row=0, column=0, padx=30, pady=80)

    # Creating Answer EntryBox
    global division_entry
    division_entry = Entry(divide_frame, font=("Arial", 32), width=8)
    division_entry.grid(row=0, column=1, padx=5, pady=80)

    # Adding Submit Button
    submit_btn = Button(divide_frame, text="Submit", font=("Arial", 28), command=lambda: division_correct(num_1.get(), num_2.get()))
    submit_btn.grid(row=0, column=2, padx=10)

    # Creating Correct and Incorrect Label
    global divide_correct_label
    divide_correct_label = Label(divide_frame, text="Enter Your Answer Above", font=("TSCu_Comic", 32), bg="green", fg="yellow")
    divide_correct_label.grid(row=1, column=0, columnspan=3)


############################
# Multiplication Operation #
############################


def multiplication_correct(num1, num2):  # Checking the answer correct or not
    # Calculating the right answer
    correct = num1 * num2

    # Checking correct or wrong
    if int(multiplication_entry.get()) == correct:
        response2 = messagebox.showinfo("Result", "You are right the Correct Answer is " + str(correct) + "\n\nNow solve this next question")

    else:
        response2 = messagebox.showerror("Result", "Your Answer is Incorrect\nThe Correct Answer is " + str(correct)+" , not "+str(multiplication_entry.get())+"\n\nNow solve this next question")
    # Clear the answer entry box
    multiplication_entry.delete(0, "end")

    # Generate 2 new random numbers
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))
    multiplication_flash.config(text=str(num_1.get()) + " x " + str(num_2.get())+" =", font=("Arial", 32), bg="red", fg="black")


def multiply():  # Multiply Function
    hide_frames()
    multiply_frame.pack(fill="both", expand=1)

    # Creating Random Integer Numbers
    global num_1
    global num_2
    num_1 = IntVar()
    num_2 = IntVar()
    num_1.set(randint(0, 100))
    num_2.set(randint(0, 100))

    # Putting the numbers on screen
    global multiplication_flash
    multiplication_flash = Label(multiply_frame, text=str(num_1.get()) + " x " + str(num_2.get()) + " =", font=("Arial", 32), bg="red", fg="black")
    multiplication_flash.grid(row=0, column=0, padx=30, pady=80)

    # Creating Answer EntryBox
    global multiplication_entry
    multiplication_entry = Entry(multiply_frame, font=("Arial", 32), width=8)
    multiplication_entry.grid(row=0, column=1, padx=5, pady=80)

    # Adding Submit Button
    submit_btn = Button(multiply_frame, text="Submit", font=("Arial", 28), command=lambda: multiplication_correct(num_1.get(), num_2.get()))
    submit_btn.grid(row=0, column=2, padx=10)

    # Creating Correct and Incorrect Label
    global multiply_correct_label
    multiply_correct_label = Label(multiply_frame, text="Enter Your Answer Above", font=("TSCu_Comic", 32), bg="red", fg="yellow")
    multiply_correct_label.grid(row=1, column=0, columnspan=3)

########################
# Hide Frame Operation #
########################


def hide_frames():  # Creating a Hide Frame Function
    addition_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()
    my_label.pack_forget()


##################
# Menu Operation #
##################

# Defining Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Creating Menu Items
# Creating Math menu
math_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Math Cards", menu=math_menu)
# Creating General Knowledge Menu
gk_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="General Knowledge Cards", menu=gk_menu)
# Creating Help Menu
help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=help_menu)
# Creating About Menu
about_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=about_menu)

# Creating About submenu
about_menu.add_command(label="About Developer", command=about_window)

# Creating Math submenu
math_menu.add_command(label="Addition", command=addition)
math_menu.add_command(label="Subtract", command=subtract)
math_menu.add_command(label="Divide", command=divide)
math_menu.add_command(label="Multiply", command=multiply)
math_menu.add_separator()
math_menu.add_command(label="Exit", command=quit_app)

###################
# Creating Frames #
###################

# Creating Math Frames
addition_frame = Frame(root, width=400, height=400, bg="cyan")
subtract_frame = Frame(root, width=400, height=400, bg="yellow")
multiply_frame = Frame(root, width=400, height=400, bg="red")
divide_frame = Frame(root, width=400, height=400, bg="green")

root.mainloop()
