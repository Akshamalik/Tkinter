#GUI Based Simple Calculator
from tkinter import *

win=Tk()
win.geometry("500x350")
win.title("Simple Calculator.....")
win.resizable(0,0)

#function for addition of the numbers:-
def add():
	n1=int(entn1.get())
	n2=int(entn2.get())
	res=n1+n2
	lblres.config(text="Addition = "+str(res))

#function for substraction of the numbers:-
def sub():
	n1=int(entn1.get())
	n2=int(entn2.get())
	res=n1-n2
	lblres.config(text="Difference = "+str(res))

#function for multiplication of the numbers:-
def mult():
	n1=int(entn1.get())
	n2=int(entn2.get())
	res=n1*n2
	lblres.config(text="Multiplication = "+str(res))

#function for division of the numbers:-
def div():
    n1=int(entn1.get())
    n2=int(entn2.get())
    res=n1/n2
    lblres.config(text="Division = "+str(res))



lbln1=Label(win,text="Enter First Number",font=("Arial 15 bold"),fg="black")
lbln1.place(x=10,y=30)

entn1=Entry(win,font=("Arial 15"),fg="black",bg="white", bd=5)
entn1.place(x=225,y=30)

lbln2=Label(win,text="Enter second Number",font=("Arial 15 bold"),fg="black")
lbln2.place(x=10,y=80)

entn2=Entry(win,font=("Arial 15"),fg="black",bg="white", bd=5)
entn2.place(x=225,y=80)

lblres=Label(win,text="Result",font=("Arial 15 bold"),fg="black")
lblres.place(x=10,y=130)

entn3=Entry(win,font=("Arial 15"),fg="black",bg="white", bd=5)
entn3.place(x=225,y=130)

#add button

btnadd=Button(win,text="+",font=("Arial 15 bold"),fg="black",command=add)
btnadd.place(x=50,y=180,width=60,height=40)

#add function code


#substraction button

btnsub=Button(win,text="-",font=("Arial 15 bold"),fg="black",command=sub)
btnsub.place(x=130,y=180,width=60,height=40)

btnmul=Button(win,text="*",font=("Arial 15 bold"),fg="black",command=mult)
btnmul.place(x=210,y=180,width=60,height=40)

btndiv=Button(win,text="/",font=("Arial 15 bold"),fg="black",command=div)
btndiv.place(x=290,y=180,width=60,height=40)





win.mainloop()
