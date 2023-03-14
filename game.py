from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("Rock-Paper-Scissors")
root.configure(background="black")

rock_i = ImageTk.PhotoImage(Image.open("rock_i.jpg"))
pap_i = ImageTk.PhotoImage(Image.open("pap_i.jpg"))
sciss_i = ImageTk.PhotoImage(Image.open("scis_i.jpg"))

user_label = Label(root,image=rock_i,bg="black")
user_label.grid(row=1,column=0)
comp_label = Label(root,image=rock_i,bg="black")
comp_label.grid(row=1,column=4)


rock = Button(root,width=20,height=2,text="ROCK",bg="black",fg="white").grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="black",fg="white").grid(row=2,column=2)
sciss = Button(root,width=20,height=2,text="SCISSORS",bg="black",fg="white").grid(row=2,column=3)


root.mainloop()
