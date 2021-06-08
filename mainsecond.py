from tkinter import *

root = Tk()
root.title("TicketSales")
root.geometry("500x400")
root.config(bg="Pink")
root.resizable(height=False, width=False)

def button_exit ():
        import sys
        sys.exit()


button1 = Button(root, text="Thank You", fg="red", borderwidth=25, bg="yellow", font=15, command=button_exit)
button1.place(x=100, y=100)

root.mainloop()
