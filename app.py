from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk
import openpyxl ,xlrd
from openpyxl import workbook
import pathlib

root=Tk()
root.title("Data Entry")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg='#326273') #cor de fundo

#edit icon
icon_image=PhotoImage(file="cogumelo.png")
root.iconphoto(False,icon_image)

#heading or header
Label(root, text="Please, Complete full this form", font="arial 14", bg="#fff", fg="#000").place(x=20,y=20)

#label


root.mainloop()