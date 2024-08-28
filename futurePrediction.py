from tkinter import *

win=Tk()
win.title("Future Prediction App")
win.geometry("400x400")
win.resizable(0,0)

def predict():
 dob=e1.get()
 dob=dob.replace("/","0")
 n=0
 for i in dob:
  n=n+int(i)
 while n>9:
  n=n%10+n//10
 if n==1:
  future="You are a intelligent person"
 elif n==2:
  future="You are deligent"
 elif n==3:
  future="You are spiritual"
 elif n==4:
  future="You are sensitive"
 elif n==5:
  future="you are emotional"
 elif n==6:
  future="You will become millionare"
 elif n==7:
  future="You will become engineer"
 elif n==8:
  future="You will become a doctor"
 elif n==9:
  future="You will become a cardiologist"
 else:
  future="You will become an IAS Officer"
 l3.config(text=future)
 
l1=Label(win,text="Future Prediction App",font=("Arial 15 bold"),fg="blue")
l1.place(x=100,y=30)

l2=Label(win,text="Enter DOB",font=("Arial 13 bold"),fg="blue")
l2.place(x=10,y=100)

e1=Entry(win,font=("Arial 15"),fg="white",bg="red")
e1.place(x=130,y=100)

btn=Button(win,text="Predict",font=("Arial 15"),fg="blue",command=predict)
btn.place(x=150,y=150)

l3=Label(win,text="Prediction",font=("Arial 15"),fg="blue")
l3.place(x=10,y=200)
win.mainloop()
