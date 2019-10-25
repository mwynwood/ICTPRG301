from tkinter import *
from tkinter import messagebox

main_form = Tk()
main_form.geometry("300x100")
main_form.title("Hello World!")

def hello():
   messagebox.showinfo("Hello", "Hello World")

label_intro = Label(main_form, text="Select an option:")
label_intro.pack()

button_hello = Button(main_form, text="Hello", command=hello)
# button_hello.place(x=35, y=50)
button_hello.pack()

button_quit = Button(main_form, text="Quit", command=quit)
# button_quit.place(x=35, y=100)
button_quit.pack()

main_form.mainloop()