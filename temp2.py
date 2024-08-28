from tkinter import *

win = Tk()
win.geometry("500x350")
win.title("Temperature Converter")
win.resizable(0, 0)

def ctof():
    n1 = int(entn1.get())
    res = (n1 * 9) / 5 + 32
    entn3.delete(0, END)  # Clear the existing text in the result textbox
    entn3.insert(0, str(res))  # Insert the result

def ftoc():
    n1 = int(entn1.get())
    res = (n1 - 32) * (5 / 9)
    entn3.delete(0, END)  # Clear the existing text in the result textbox
    entn3.insert(0, str(res))  # Insert the result

lbln1 = Label(win, text="Enter Temperature", font=("Arial 15 bold"), fg="black")
lbln1.place(x=10, y=30)

entn1 = Entry(win, font=("Arial 15"), fg="black", bg="white", bd=5)
entn1.place(x=225, y=30)

# Remove the lblres as it is not used anymore
lblres = Label(win, text="Result", font=("Arial 15 bold"), fg="black")
lblres.place(x=10, y=130)

# Update the entn3 label's position and name it more appropriately, if desired
entn3 = Entry(win, font=("Arial 15"), fg="black", bg="white", bd=5)
entn3.place(x=225, y=130)

# c_to_f button
btnctof = Button(win, text="CtoF", font=("Arial 15 bold"), fg="black", command=ctof)
btnctof.place(x=50, y=180, width=60, height=40)

# f_to_c button
btnftoc = Button(win, text="FtoC", font=("Arial 15 bold"), fg="black", command=ftoc)
btnftoc.place(x=130, y=180, width=60, height=40)

win.mainloop()
