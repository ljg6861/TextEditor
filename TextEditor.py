#Lucas Golden

from tkinter import filedialog
from tkinter import *

root=Tk("Text Editor")
text = Text(root)
#function that uses the input stream from open_file to
#write to the editor
#stream - the stream of input from open_file
def init():
    text.grid()
    root.mainloop()

#def save():
    #t = text.get("1.0", "end-1c")
    #root.savelocation=filedialog.asksaveasfilename()
    #file1=open(savelocation, "+")
    #file1.write(t)
    #file1.close()

def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()


button=Button(root, text="Save", command=file_save) 
button.grid()


def main():
    init()

main()
