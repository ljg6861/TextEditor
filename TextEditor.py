#Lucas Golden

from tkinter import filedialog
from tkinter import * 
import SpellCheck

root=Tk("Text Editor")
text = Text(root)

#initializes the text editor
def init(root, text):
    # button=Button(root, text="Save", command=file_save) 
    # button2 = Button(root, text = "Open File", command = open_new_window)
    # button3 = Button(root, text = "Edit")
    # button4 = Button(root, text = "Selection")
    # button5 = Button(root, text = "Find")
    # button6 = Button(root, text = "View")
    # button7 = Button(root, text = "Goto")
    # button8 = Button(root, text = "Tools")
    # button9 = Button(root, text = "Help")
    # button.grid()
    # button2.grid()
    # button3.grid()
    # button4.grid()
    # button5.grid()
    # button6.grid()
    # button8.grid()
    # button9.grid()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_new_window)
    filemenu.add_command(label="Save", command=file_save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=check_quit)
    menubar.add_cascade(label="File", menu=filemenu)
    text.grid()
    root.config(menu=menubar)
    while (True):
        text.bind("<space>", callback)
        root.update_idletasks()
        root.update()

def callback(*args):
    print(text.get("1.0", END).split(" ")[len(text.get("1.0", END).split(" "))-1])

def check_quit():
    top = Toplevel(height = 1200, width = 600)
    top.title("Quit without saving")
    msg = Message(top, text = "Would you like to save before quitting?")
    msg.pack()
    button = Button(top, text = "Yes", command = file_save)
    button.pack()
    button2 = Button(top, text = "No", command = root.quit)
    button2.pack()

# saves the file as a .txt file
def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()

def get_word(text, size):
    current = text.index(END)
    current = float(current)
    word = text.get(current - 1, current - 1 - size)
    return word

def updates(text):
    word = text.get("current")
    if word == " ":
        return True
    else:
        return False


def open_new_window():
    filename = get_file()
    root2 = Tk()
    text2 = Text(root2)
    text2.grid()
    menubar = Menu(root2)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_new_window)
    filemenu.add_command(label="Save", command=file_save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=check_quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root2.update_idletasks()
    root2.update()
    root2.config(menu=menubar)
    root2.after(1, lambda: root2.focus_force())
    file_open(filename, text2)
    root2.mainloop()

def get_file():
    #check_save()
    filename =  filedialog.askopenfilename(initialdir = "/",
        title = "Select file",filetypes = (("jpeg files","*.jpg"),
        ("text files", "*.txt"),("all files","*.*")))
    return filename

def file_open(filename, text):
    with open(filename) as file:
        data = file.read()
        for line in data:
            text.insert(INSERT, line)



def main(root, text):
    init(root, text)

main(root, text)
