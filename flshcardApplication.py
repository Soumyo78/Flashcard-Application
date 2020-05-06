import random
import webbrowser
from tkinter import *
from random import randint, randrange  # This will create random integers
from tkinter import messagebox
from PIL import ImageTk, Image


root = Tk()
root.title("Flashcard")
root.geometry("630x400")
root.resizable(0, 0)
root.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/FlashcardApp/icons/icon.png"))

# Add String Variable
current_status = StringVar()
current_status.set("Select any option")

#####################
# Creating Function #
#####################

################################################
# Creating Callback function to open hyperlink #
################################################

def callback(url):
    webbrowser.open_new(url)

#################
# About Section #
#################

def about_window():
    root.iconify()
    about = Toplevel()
    about.title("About")
    about.geometry("500x450")
    about.iconphoto(True, PhotoImage(file="/home/soumyo/PycharmProjects/FlashcardApp/icons/about.png"))

    # Creating About Frame
    about_frame = Frame(about, width=400, height=400)
    about_frame.pack(fill="both", expand=1)

    # Adding Developer Image
    dev_img = Image.open("/home/soumyo/PycharmProjects/FlashcardApp/images/about_profile_pic.jpg")
    dev_img = dev_img.resize((150, 151), Image.ANTIALIAS)
    DEV_IMG = ImageTk.PhotoImage(dev_img)
    dev_img_label = Label(about_frame, image=DEV_IMG)
    dev_img_label.grid(row=0, column=0, pady=30, padx=10, rowspan=2)

    # Creating About Label
    about_label1 = Label(about_frame, text="Soumyo Roy", font=("Noto Sans Medium", 20))
    about_label1.grid(row=0, column=1, padx=10, sticky=W)

    about_label2 = Label(about_frame, text="Student\nLoves to develop software and game.\nKrishnanagar, India.", font=("Noto Sans Medium", 12), justify=LEFT)
    about_label2.grid(row=1, column=1, padx=10, columnspan=2, sticky=W)

    about_label3 = Label(about_frame, text="Profiles :-", font=("Noto Sans Medium", 20))
    about_label3.grid(row=2, column=0, sticky=W)

    # Adding profile icons
    fb_icon = Image.open("/home/soumyo/PycharmProjects/FlashcardApp/icons/fb.png")
    fb_icon = fb_icon.resize((40, 40), Image.ANTIALIAS)
    FB_ICON = ImageTk.PhotoImage(fb_icon)
    fb_icon_label = Label(about_frame, image=FB_ICON, justify=LEFT, cursor="hand2")
    fb_icon_label.grid(row=3, column=0, sticky=W, padx=40, pady=30)
    fb_icon_label.bind("<Button-1>", lambda e: callback("https://www.facebook.com/soumyo.roy.31"))  # Creating Hyperlink

    twitter_icon = Image.open("/home/soumyo/PycharmProjects/FlashcardApp/icons/twitter.png")
    twitter_icon = twitter_icon.resize((60, 60), Image.ANTIALIAS)
    TWITTER_ICON = ImageTk.PhotoImage(twitter_icon)
    twitter_icon_label = Label(about_frame, image=TWITTER_ICON, justify=LEFT, cursor="hand2")
    twitter_icon_label.grid(row=3, column=1, sticky=W, padx=10)
    twitter_icon_label.bind("<Button-1>", lambda e: callback("https://twitter.com/RoySoumyo"))  # Creating Hyperlink

    github_icon = Image.open("/home/soumyo/PycharmProjects/FlashcardApp/icons/github3png")
    github_icon = github_icon.resize((64, 58), Image.ANTIALIAS)
    GITHUB_ICON = ImageTk.PhotoImage(github_icon)
    github_icon_label = Label(about_frame, image=GITHUB_ICON, justify=LEFT, cursor="hand2")
    github_icon_label.grid(row=3, column=2, sticky=W)
    github_icon_label.bind("<Button-1>", lambda e: callback("https://github.com/Soumyo78"))  # Creating Hyperlink

    # Creating Close About Window Function
    def close_about():
        root.deiconify()
        about.destroy()

    # Adding Close Button
    close_btn = Button(about_frame, text="Close", font=("Arial", 10), command=close_about)
    close_btn.grid(row=4, column=0, columnspan=3, pady=40)



    about.mainloop()

#################
# Close Program #
#################


def quit_app():
    response1 = messagebox.askquestion("Question", "Do you want to close the program ?")
    if response1 == "yes":
        root.quit()
    else:
        pass

#######################
# Start Page Function #
#######################


def start():
    hide_frames()
    start_frame.pack(fill="both", expand=1)
    current_status.set("Select any option")

    # Creating labels
    start_label = Label(start_frame, text="Welcome to Flash Card Application\nPlease choose any card option", font=("Arial", 19))
    start_label.grid(row=0, column=0, pady=40, padx=100, columnspan=2)  # This is start frame label

    mathcard_label = Label(start_frame, text="Math Cards\n__________", font=("Times New Roman", 12))
    mathcard_label.grid(row=1, column=0, pady=20, sticky=W, padx=100)

    gkcard_label = Label(start_frame, text="General Knowledge Cards\n__________________________", font=("Times New Roman", 12))
    gkcard_label.grid(row=1, column=1, pady=20)

    # Add Integer Variable Function
    global v
    v = IntVar()
    v.set(1)

    # Creating Radio Buttons
    rbutton1 = Radiobutton(start_frame, text="Addition", variable=v, value=1).grid(row=2, column=0, sticky=W, padx=100)
    rbutton2 = Radiobutton(start_frame, text="Subtraction", variable=v, value=2).grid(row=3, column=0, sticky=W, padx=100)
    rbutton3 = Radiobutton(start_frame, text="Multiplication", variable=v, value=3).grid(row=4, column=0, sticky=W, padx=100)
    rbutton4 = Radiobutton(start_frame, text="Division", variable=v, value=4).grid(row=5, column=0, sticky=W, padx=100)
    rbutton5 = Radiobutton(start_frame, text="State Capitals", variable=v, value=5).grid(row=2, column=1, sticky=W, padx=100)
    rbutton6 = Radiobutton(start_frame, text="Country Capitals", variable=v, value=6).grid(row=3, column=1, sticky=W, padx=100)

    # Creating Go Button
    go_btn = Button(start_frame, text="Go", font=("Arial", 28), command=radio)
    go_btn.grid(row=6, column=0, columnspan=2)


##################################
# Creating Radio Button Function #
##################################


def radio():
    if v.get() == 1:
        addition()
    if v.get() == 2:
        subtract()
    if v.get() == 3:
        multiply()
    if v.get() == 4:
        divide()

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
    current_status.set("Solve Addition Problems")

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
    current_status.set("Solve Subtraction Problems")

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
    current_status.set("Solve Division Problems")

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
    current_status.set("Solve Multiplication Problems")

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
    for widget in addition_frame.winfo_children():
        widget.destroy() # Destroying all the children under addition frame
    for widget in subtract_frame.winfo_children():
        widget.destroy()
    for widget in divide_frame.winfo_children():
        widget.destroy()
    for widget in multiply_frame.winfo_children():
        widget.destroy()
    for widget in start_frame.winfo_children():
        widget.destroy()

    start_frame.pack_forget()
    addition_frame.pack_forget()
    subtract_frame.pack_forget()
    multiply_frame.pack_forget()
    divide_frame.pack_forget()


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

# Creating General Knowledge submenu
gk_menu.add_command(label="State Capitals")
gk_menu.add_command(label="Country Capitals")


# Creating Math submenu
math_menu.add_command(label="Addition", command=addition)
math_menu.add_command(label="Subtraction", command=subtract)
math_menu.add_command(label="Division", command=divide)
math_menu.add_command(label="Multiplication", command=multiply)
math_menu.add_separator()
math_menu.add_command(label="Start Page", command=start)
math_menu.add_command(label="Exit", command=quit_app)

###################
# Creating Frames #
###################

# Creating Math Frames
addition_frame = Frame(root, width=400, height=400, bg="cyan")
subtract_frame = Frame(root, width=400, height=400, bg="yellow")
multiply_frame = Frame(root, width=400, height=400, bg="red")
divide_frame = Frame(root, width=400, height=400, bg="green")

# Creating Start Frame
start_frame = Frame(root, width=400, height=400)

########################
# Calling Start Screen #
########################

start()

######################
# Creating StatusBar #
######################

# Add Status Label
my_status = Label(root, textvariable=current_status, bd=2, relief="sunken", width=100, anchor=SW)
my_status.pack(side=BOTTOM)


root.mainloop()
