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
Label(root, text='Name', font=23, bg="#000", fg='#fff').place(x=50, y=100)
Label(root, text='Contact no.', font=23, bg="#000", fg='#fff').place(x=50, y=150)
Label(root, text='Age', font=23, bg="#000", fg='#fff').place(x=50, y=200)
Label(root, text='Gender', font=23, bg="#000", fg='#fff').place(x=370, y=200)
Label(root, text='Address', font=23, bg="#000", fg='#fff').place(x=50, y=250)

#entry

nameValue = StringVar()
contactValue = StringVar()
AgeValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue, width=45, bd=2, font=20)
contactEntry = Entry(root, textvariable=nameValue, width=45, bd=2, font=20)
AgeEntry = Entry(root, textvariable=nameValue, width=15, bd=2, font=20)

#gender
gender_combobox =  Combobox(root,values=['Male', 'Female'], font='arial 14', state='r', width=14)
gender_combobox.place(x=400, y=200)

nameEntry.place(x=110,y=100)
contactEntry.place(x=110,y=150)
AgeEntry.place(x=110,y=200)

root.mainloop()