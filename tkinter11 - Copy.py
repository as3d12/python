from tkinter import *

app = Tk()
app.title('Check Button')
app.geometry('250x200')

lbl = Label(text='What courses would you like to take?')
lbl.grid(row=0, column=0, padx=5, pady=5)
chk1 = BooleanVar()
#هان عشان تكون محطوط عليها صح
chk1.set(True)
chkButton1 = Checkbutton(app, text='Python', var=chk1)
chkButton1.grid(row=1, column=0, sticky= 'W', padx=5, pady=5)

chk2 = BooleanVar()
chkButton2 = Checkbutton(app, text='Data Science', var=chk2)
chkButton2.grid(row=2, column=0, sticky= 'W', padx=5, pady=5)

chk3 = BooleanVar()
chkButton3 = Checkbutton(app, text='Cyber Security', var=chk3)
chkButton3.grid(row=3, column=0, sticky= 'W', padx=5, pady=5)
def get_courses():
    if chk1.get() == True:
        print("Python is selected")
    if chk2.get() == True:
        print("Data Science is selected")
    if chk3.get() == True:
        print("Data Mining is selected")

b1 = Button(app, text="Get My Courses", command= get_courses)
b1.grid(row=4, column=0, sticky= 'W', padx=5, pady=5)

app.mainloop()