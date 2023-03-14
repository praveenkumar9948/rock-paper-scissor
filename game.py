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

root.mainloop()
