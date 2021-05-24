
from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("OOP using tkinker")
root.geometry("600x600")
root.config(bg="Orange")

#The users
user_pass = {"Vuyani": "Vuya@2021", "Atheelah": "maroon17", "Ikraam": "carsthemovie", "Nathan": "blue1",
"Amanda": "@amanda28"}

#Labels
label_passname = Label(root, text="Username: ", font=12, bg="Gold")
label_passname.place(x=50, y=50)
label_password = Label(root, text="Password: ", font=12, bg="Gold")
label_password.place(x=50, y=100)

#Entry Box
Entry_passname = Entry(root)
Entry_passname.place(x=150, y=50)
Entry_password = Entry(root)
Entry_password.place(x=150, y=100)

#Clear

def button_clear():
    Entry_password.delete(0, END)
    Entry_passname.delete(0, END)
        #CLEARING THE INPUT FIELDS

#Functions
def func_verify(user, _password, user_pass):
    if user in user_pass:
        if _password == user_pass[user]:
            return 1
        else:
            return 0
    else:
            return -1

def veried():

    username = Entry_passname.get()
    password = Entry_password.get()
    print(username)
    print(password)

    x = int (func_verify(username, password, user_pass))

    if x == 1 :
        root.destroy()
        import mainsecond
    elif x == 0 or x == -1:
        messagebox.showinfo("alert","Incorrect Information" )


# Buttons
button_verify = Button (root, text="Verify", borderwidth="10", fg="Navy", bg="Gold", font=12, command=veried)
button_verify.place(x=50, y=250)
button_clear = Button (root, text="Clear", borderwidth="10", fg="Navy", bg="Gold", font=12, command=button_clear)
button_clear.place(x=150, y=250)
button_exit = Button (root, text="Exit", borderwidth="10", fg="Navy", bg="Gold", font=12)
button_exit.place(x=250, y=250)

#Getting the inputs







root.mainloop()
