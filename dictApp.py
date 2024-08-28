from tkinter import *
from PyDictionary import PyDictionary
from tkinter import messagebox

win=Tk()
win.title("Dictionary App")
win.geometry("1000x626")
win.resizable(0,0)

pd=PyDictionary()

def search():
 word=e1.get()
 meaning=pd.meaning(word)
 textarea.insert(END,meaning) 
def clear():
 e1.delete(0,END)
 textarea.delete(1.0,END)
def iexit():
 res=messagebox.askyesno("Confirm","Are your sure?")
 if res==True:
  win.destroy()
 else:
  pass
 
 
#photoimage is a class in the tkinter
bgimage=PhotoImage(file="bg.png")
lblbg=Label(win,image=bgimage)
lblbg.place(x=0,y=0)

l1=Label(win,text="ENTER WORD",font=("Arial 29 bold"),fg="red3",bg="whitesmoke")
l1.place(x=560,y=20)

e1=Entry(win,font=("Arial 23 bold"),bd=8,justify=CENTER,relief=GROOVE)
e1.place(x=500,y=100)

b1=Button(win,text="Search",font=("Arial 18 bold"),bd=5,relief=GROOVE,command=search)
b1.place(x=630,y=180)

l2=Label(win,text="MEANING",font=("Arial 29 bold"),fg="red3",bg="whitesmoke")
l2.place(x=600,y=280)

textarea=Text(win,font=("Arial 18 bold"),height=5,width=34,bd=5,relief=GROOVE)
textarea.place(x=480,y=350)

clearImg=PhotoImage(file="clear.png")
btnclear=Button(win,image=clearImg,bd=0,bg="whitesmoke",command=clear)
btnclear.place(x=600,y=520)

exitImg=PhotoImage(file="exit.png")

btnexit=Button(win,image=exitImg,bd=0,bg="whitesmoke",command=iexit)
btnexit.place(x=720,y=520)

win.mainloop()