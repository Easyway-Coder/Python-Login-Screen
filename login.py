from tkinter.messagebox import *
from tkinter import *

r = Tk()
Label(r, text="Login", font="Arial 40", fg="red", bg="blue").grid(row=0, column=0)
Label(r, text="Username: ", font="Arial 20", fg="green", bg="blue").grid(row=1, column=0)
u = Entry(r, font="Arial 20")
u.grid(row=1, column=1)
Label(r, text="Password: ", font="Arial 20", fg="green", bg="blue").grid(row=2, column=0)
p = Entry(r, font="Arial 20", show="*")
p.grid(row=2, column=1)


def login():
    user = u.get()
    passw = p.get()
    if user == "User1" and passw == "just_a_password":
        showinfo("Login Success", "Login Success!")
        r.quit()
    elif user == "" or passw == "":
        showinfo("Blank Input", "Sorry! Blank Input Is Not Accepted!")
    else:
        showinfo("Login Failed!", "Login Unsuccessful! Username or Password is Incorrect!")


Button(r, text="Login", font="Arial 20", command=login).grid(row=3, column=1)


def toggle():
    if c.get() == 1:
        p.config(show="")
    else:
        p.config(show="*")


c = IntVar(value=0)
Checkbutton(r, text="Show Password", bg="blue", font="Arial 20", onvalue=1, offvalue=0, variable=c, command=toggle).grid(row=0, column=1)
r.title("Login Screen")
r.geometry("600x400")
r.configure(bg="blue")
r.mainloop()
