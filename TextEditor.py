#Lucas Golden

from tkinter import filedialog
from tkinter import * 



#initializes the text editor
def init(root, text, char_count):
    global word_count
    word_count = 0
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_new_window)
    filemenu.add_command(label="Save", command=file_save)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=check_quit)
    menubar.add_cascade(label="File", menu=filemenu)
    text.grid()
    wordCount = Label(root, textvariable = char_count)
    wordCount.grid()
    root.config(menu=menubar)
    while (True):
        char_count.set(str(len(text.get("1.0", 'end-1c'))))
        text.bind("<space>", word_callback)
        root.update_idletasks()
        root.update()

def word_callback(*args):
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

def open_new_window():
    filename = get_file()
    root2 = Tk()
    text2 = Text(root2)
    var = IntVar()
    init(root2, text2, var)
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



def main():
    root=Tk("Text Editor")
    text = Text(root)
    char_count = IntVar()
    init(root, text, char_count)

main()
