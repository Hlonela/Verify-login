from tkinter import *

root = Tk()
root.title("TicketSales")
root.geometry("500x400")
root.config(bg="Pink")
root.resizable(height=False, width=False)


button1 = Button(root, text="Welcome To Ticket Sales", fg="red", borderwidth=25, bg="yellow", font=15)
button1.place(x=100, y=100)

root.mainloop()
