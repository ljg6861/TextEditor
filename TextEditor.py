#Lucas Golden

from tkinter import filedialog
from tkinter import *
import io

root=Tk("Text Editor")
text = Text(root)
check = 0
check2 = 0
#initializes the text editor
def init():
    text.grid()
    root.mainloop()

def button1_callback():
    check += 1

def button2_callback():
    check2 += 1

# saves the file as a .txt file
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

def check_save():
    toplevel = Toplevel()
    label1 = Label(toplevel, text="Would you like to save?", height=10, width=100)
    label1.pack()
    button3 = Button(toplevel, text = "Yes", command= button1_callback)
    button4 = Button(toplevel,text = "No", command =  button2_callback)
    button3.grid()
    button4.grid()
    if check > 0:
        file_save()
    else:
        pass

def file_open():
    check_save()
    filename =  filedialog.askopenfilename(initialdir = "/",
        title = "Select file",filetypes = (("jpeg files","*.jpg"),
        ("text files", "*.txt"),("all files","*.*")))
    with open(filename) as file:
        data = file.read()
        for line in data:
            text.insert(INSERT, line)

button=Button(root, text="Save", command=file_save) 
button2 = Button(root, text = "Open File", command = file_open)
button.grid()
button2.grid()


def main():
    init()

main()
