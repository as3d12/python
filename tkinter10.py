from tkinter import *
import tkinter.messagebox

top = Tk()
top.title("Dialog Box")
top.geometry('250x100')

lb1 = Label(top, text = "First Name")
lb1.grid(row=0, column=0, padx=5, pady=5)
fName = Entry(top, width = 20)
fName.grid(row = 0, column=1, padx=5, pady=5)
lb2 = Label(top, text = "Last Name")
lb2.grid(row=1, column=0, padx=5, pady=5)
lName = Entry(top, width = 20)
lName.grid(row = 1, column=1, padx=5, pady=5)

def Get_name():
    if fName.get() and lName.get():
        full_name = f'Your name is: {fName.get().title()} {lName.get().title()}'
        tkinter.messagebox.showinfo("Full Name", full_name)
    else:
        tkinter.messagebox.showerror("Error", 
						'All fields are required !!')

b1 = Button(top, text="Full Name", command= Get_name)
b1.grid(row=2, column=1, sticky='W', pady=5)
b2 = Button(top, text="Quit", command= top.destroy)
b2.grid(row=2, column=1, sticky='E')

top.mainloop()

