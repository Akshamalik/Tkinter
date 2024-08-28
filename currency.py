#GUI based currency converter in python

from tkinter import *
from tkinter import Tk,ttk
from PIL import Image,ImageTk
from currency_converter import CurrencyConverter

cor0="#e8f48c"
cor1="#b2ec5d"
cor2="#bf00ff"
cor3="#100c08"

win=Tk()
win.geometry("300x320")
win.title("CurrencyConverter")
win.resizable(0,0)

top=Frame(win,width=300,height=60,bg=cor0)
top.grid(row=0,column=0)

main=Frame(win,width=300,height=260,bg=cor1)
main.grid(row=1,column=0)

icon=Image.open("icon.png")
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)

app_name=Label(top,image=icon,text="Currency Converter",compound=LEFT,bg=cor2,fg=cor3,font=("Arial 16 bold"),padx=20,pady=10)
app_name.place(x=0,y=0)

win.mainloop()