from guizero import *

def say_hello():
    if len(name.value) > 0:
        output.value = "Hello " + name.value + "!"
    else:
        error(title="Error", text="Please enter your name")

app = App(height=150, width=300, title="Say Hello")
Text(app, text="What's your name?")
name = TextBox(app)
button = PushButton(app, command=say_hello, text="Go")
output = Text(app, text="")

app.display()
