#import the required packages
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import edit_menu
import format_menu
import help_menu


#creating window

root = Tk()

#geometry 
root.title("Text Editor")
root.minsize(height=400,width= 400)

#to enter text
text = ScrolledText(root , state='normal', height=400 , width = 400 , wrap = "word" , padx = 3 , pady = 2 , undo = True)
text.pack(fill = Y , expand = 1)
text.focus_set()

#creating menubar
menubar = Menu(root)
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)

root.mainloop()
