from currency_converter import CurrencyConverter
import tkinter as tk
# a=currency_converter()
# print(a.convert(12,"USD","INR"))
a=CurrencyConverter()
win=tk.Tk()
win.geometry("500x360")
win.title("Currency Converter")

def clicked():
    amount=int(e1.get())
    curr1=e2.get()
    curr2=e3.get()
    data=a.convert(amount,curr1,curr2)
    l5=tk.label(win,text=data).place(x=230,y=290)

l1=tk.Label(win,text="Currency Converter",font="Times 25 bold").place(x=100,y=30)
l2=tk.Label(win,text="Enter the amount here:",font="Times 18 bold").place(x=50,y=80)
e1=tk.Entry(win)
l3=tk.Label(win,text="Enter currency:",font="Times 18 bold").place(x=50,y=130)
e2=tk.Entry(win)
l4=tk.Label(win,text="Enter req currency:",font="Times 18 bold").place(x=50,y=180)
e3=tk.Entry(win)
b1=tk.Button(win,text="click",command=clicked).place(x=230,y=240)
e1.place(x=300,y=90)
e2.place(x=300,y=140)
e3.place(x=300,y=190)

win.mainloop()

