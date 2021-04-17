from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x600")
Label(root,text = "Which Country you want to travel in?", font ="lucidia 19 bold").pack()

country = ["Australia","Japan","India","England","Spain","Italy","U.S.A","Germany","Tunisia","Moroco","Egypt","Qatar","Saudi"]

var = StringVar()
new_var = var.set("nonwhere")
def travel():
    tmsg.showinfo("Let's Travel",f"So, we are booking your flight to{var.get()}\n We wish you a happy journey. Thanks for booking with us")

for x in range(len(country)):
    Radiobutton(root, text = country[x], variable = var, value = country[x]).pack()
    
Button(root, text="Let's Travel",command=travel).pack()
root.mainloop()