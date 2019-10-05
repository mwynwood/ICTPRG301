from tkinter import *
from tkinter import messagebox

mainForm = Tk()
mainForm.geometry("300x100")
mainForm.title("Hello World!")

def hello():
   messagebox.showinfo("Hello", "Hello World")

lblIntro = Label(mainForm, text="Select an option:")
lblIntro.pack()

btnHello = Button(mainForm, text="Hello", command=hello)
# btnHello.place(x=35, y=50)
btnHello.pack()

btnQuit = Button(mainForm, text="Quit", command=quit)
# btnQuit.place(x=35, y=100)
btnQuit.pack()

mainForm.mainloop()