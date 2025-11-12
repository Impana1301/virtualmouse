import warnings
warnings.filterwarnings('ignore') # suppress import warnings

import os
from tkinter import filedialog
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

def dos():
    os.system('python C:/Users/impan/Desktop/Virtual-Mouse-using-Hand/controllerfinal.py')





def main():
    print('Started')
    window = Tk()
    window.title("Virtual Mouse")
    window.geometry('300x300')  
    a = Button(text="Start Application", height=2, width=30,command=dos)
    a.place(relx=0.5, rely=0.5, anchor=CENTER)
    window.mainloop()

if __name__ == '__main__': main()
