import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk
import re


window=tk.Tk()
window.title("KIDS SWIMMING LESSONS REGISTRATION")
window.geometry('700x500')


bg = PhotoImage(file=r'C:\Users\menia\Desktop\swim.png')
background_label = Label(window,image=bg)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
Child_id=tk.StringVar()
Child_Firstname=tk.StringVar()
Child_Lastname=tk.StringVar()
Parent_Firstname=tk.StringVar()
Child_Birth_Date=tk.StringVar()
Parent_Phonenumber=tk.StringVar()
Email_adress=tk.StringVar()
pattern= "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
mch=re.search(pattern,Email_adress.get())
errorsFrame = tk.Frame(window)


def closewindow():
    for i in errorsFrame.pack_slaves():
        i.destroy()


    if len(Child_id.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter an id", fg="blue")
        ErrorLabel.pack()

    if Child_id.get().isdigit()==False:
        ErrorLabel = tk.Label(errorsFrame, text="id must be a number",fg="blue")
        ErrorLabel.pack()
    if len(Child_id.get())!=9:
        ErrorLabel = tk.Label(errorsFrame, text="id must contains exactly 9 numbers", fg="blue")
        ErrorLabel.pack()
    if len(Child_Firstname.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter a child firstname",fg="blue")
        ErrorLabel.pack()
    if len(Child_Lastname.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter a child lastname",fg="blue")
        ErrorLabel.pack()
    if len(Parent_Firstname.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter a parent firstname ",fg="blue")
        ErrorLabel.pack()
    if len(Parent_Phonenumber.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter an phone number", fg="blue")
        ErrorLabel.pack()
    if Parent_Phonenumber.get().isdigit()==False:
        ErrorLabel = tk.Label(errorsFrame, text="phone number must be a number", fg="blue")
        ErrorLabel.pack()
    if len(Parent_Phonenumber.get())!=10:
        ErrorLabel = tk.Label(errorsFrame, text="phone number must contains exactly 10 numbers", fg="blue")
        ErrorLabel.pack()
    if Parent_Phonenumber.get().startswith("05")==False:
        ErrorLabel = tk.Label(errorsFrame, text="phone number must start with 05", fg="blue")
        ErrorLabel.pack()
    if len(Email_adress.get())==0:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter a email adress", fg="blue")
        ErrorLabel.pack()
    if mch==None:
        ErrorLabel = tk.Label(errorsFrame, text="you must enter a valid email adress", fg="blue")

        ErrorLabel.pack()
    else:
        f=open("kids_list.csv","a")
        f.seek(0)
        reader=csv.reader(f)
        for i in reader:
            if i!=Child_id.get():
                f.write(f'\n{Child_id.get()},{Child_Firstname.get()},{Child_Lastname.get()},{Parent_Firstname.get()},{Parent_Phonenumber.get()},{Email_adress.get()}')
                f.close()
                window.quit()


Child_idLabel=tk.Label(window, text="Child's id:", bg="yellow")
Child_idLabel.pack()
Child_idEntry=tk.Entry(window, textvariable=Child_id)
Child_idEntry.pack()

Child_FirstnameLabel=tk.Label(window, text="Child's Firstname:")
Child_FirstnameLabel.pack()
Child_FirstnameEntry=tk.Entry(window, textvariable=Child_Firstname)
Child_FirstnameEntry.pack()

Child_LastnameLabel=tk.Label(window, text="Child's Lastname:", bg="red")
Child_LastnameLabel.pack()
Child_LastnameEntry=tk.Entry(window, textvariable=Child_Lastname)
Child_LastnameEntry.pack()

Parent_FirstnameLabel=tk.Label(window, text="Parent's Firstname:", bg="medium violet red")
Parent_FirstnameLabel.pack()
Parent_FirstnameEntry=tk.Entry(window, textvariable=Parent_Firstname)
Parent_FirstnameEntry.pack()

Parent_PhonenumberLabel=tk.Label(window, text="Parent's Phone number:", bg="dodger blue")
Parent_PhonenumberLabel.pack()
Parent_PhonenumberEntry=tk.Entry(window, textvariable=Parent_Phonenumber)
Parent_PhonenumberEntry.pack()

Email_adressLabel=tk.Label(window, text="Email adress:", bg="sky blue")
Email_adressLabel.pack()
Email_adressEntry=tk.Entry(window, textvariable=Email_adress)
Email_adressEntry.pack()

Child_Birth_DateLabel=tk.Label(window, text="Child's Birth Date:", bg="lawn green")
Child_Birth_DateLabel.pack()


langs=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
list_items=tk.StringVar
cb=ttk.Combobox(window,textvariable=list_items)
cb["values"]=langs
cb.pack()

langs=["January","February","March","April","May","June","July","August","September","October","November","December"]
list_items=tk.StringVar
cb=ttk.Combobox(window,textvariable=list_items)
cb["values"]=langs
cb.pack()

langs=["2017","2016","2015","2014","2013"]
list_items=tk.StringVar
cb=ttk.Combobox(window,textvariable=list_items)
cb["values"]=langs
cb.pack()


Lesson_BranchLabel=tk.Label(window, text="Branch:",bg="lime green")
Lesson_BranchLabel.pack()

langs=["Tel-Aviv","Netanya","Jerusalem","Beer Sheva","Haifa"]
list_items=tk.StringVar
cb=ttk.Combobox(window,textvariable=list_items)
cb["values"]=langs
cb.pack()

btn=ttk.Button(window, text="REGISTER", command=closewindow)
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', font=('Arial', 14),weight=("bold"), background='#232323', foreground='white')
style.map('TButton', background=[('active', '#ff0000')])
btn.pack()
errorsFrame.pack()
window.mainloop()
