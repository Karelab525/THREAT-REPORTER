import core
from tkinter import Tk, Label, Button, filedialog
from tkinter.messagebox import showinfo
from openpyxl import workbook, load_workbook

PathToFile = 'x'
PathToFolder = 'x'


def select_file():
    global PathToFile
    filetypes = (
        ('csv file', '*.csv'),
        ('All files', '*,*')
    )
    filename = filedialog.askopenfilename(title='Otvorte súbor', filetypes=filetypes)
    PathToFile = filename
    open_file_label.config(text=filename)


def chose_directory():
    global PathToFolder
    directory = filedialog.askdirectory(title='Zvolte súbor')
    PathToFolder = directory
    directory_label.config(text=directory)


def start_core():
    core.start(PathToFile, PathToFolder)


window = Tk()
window.title('Report Generator')
window.resizable(False, False)
window.geometry('500x200')

open_file_label = Label(window, text='Otvoriť CSV súbor')

file_butt = Button(window, text='Open file', command=select_file)

directory_label = Label(window, text='Zvoliť lokáciu pre generovaný súbor')

directory_butt = Button(window, text='Zvoliť lokáciu', command=chose_directory)

gen_label = Label(window, text='Generuj IOC report')

gen_butt = Button(window, text='Generuj', command=start_core)

open_file_label.pack()
file_butt.pack()
directory_label.pack()
directory_butt.pack()
gen_label.pack()
gen_butt.pack()

window.mainloop()
