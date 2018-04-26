#Lucas Golden

from tkinter import filedialog
from tkinter import *

root=Tk("Text Editor")
text = Text(root)
#initializes the text editor
def init():
    text.grid()
    root.mainloop()

# saves the file as a .txt file
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

def file_open():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"), ("text files", "*.txt"),("all files","*.*")))
    with open(root.filename, "r") as f:
        Label(root, text=f.read()).pack()

button=Button(root, text="Save", command=file_save) 
button2 = Button(root, text = "Open File", command = file_open)
button.grid()
button2.grid()


def main():
    init()

main()
