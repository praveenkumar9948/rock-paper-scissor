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



uscore = Label(root,text=0,font=100,bg="black",fg="white")
uscore.grid(row=1,column=1)
cscore = Label(root,text=0,font=100,bg="black",fg="white")
cscore.grid(row=1,column=3)

user_indica =  Label(root,font=50,text="YOU",bg="black",fg="white")
user_indica.grid(row=0,column=1)
comp_indica =  Label(root,font=50,text="BOT",bg="black",fg="white")
comp_indica.grid(row=0,column=3)

msg = Label(root,font=50,bg="black",fg="white")
msg.grid(row=3,column=2)
// added labels and score.

rock = Button(root,width=20,height=2,text="ROCK",bg="black",fg="white").grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="black",fg="white").grid(row=2,column=2)
sciss = Button(root,width=20,height=2,text="SCISSORS",bg="black",fg="white").grid(row=2,column=3)



def upmsg(i):
	msg['text']=i

def upuserscore():
	sc=int(uscore["text"])
	sc+=1
	uscore["text"]=str(sc)
def upcompscore():
	sc=int(cscore["text"])
	sc+=1
	cscore["text"]=str(sc)

def wim(x,y):
	if x==y:
		upmsg("Tie!")
	elif x==0:
		if y==1:
			upmsg("LOST!")
			upcompscore()
		elif y==2:
			upmsg("WON!")
			upuserscore()
	elif x==1:
		if y==0:
			upmsg("WON!")
			upuserscore()
		elif y==2:
			upmsg("LOST!")
			upcompscore()
	elif x==2:
		if y==0:
			upmsg("WON!")
			upuserscore()
		elif y==1:
			upmsg("LOST!")
			upcompscore()



def func(x):
	y=random.randint(0,2)
	if y==0:
		comp_label.configure(image=rock_ci)
	elif y==1:
		comp_label.configure(image=pap_ci)
	elif y==2:
		comp_label.configure(image=sciss_ci)
	
	if x==0:
		user_label.configure(image=rock_i)
	elif x==1:
		user_label.configure(image=pap_i)
	elif x==2:
		user_label.configure(image=sciss_i)
	wim(x,y)

rock = Button(root,width=20,height=2,text="ROCK",bg="black",fg="white",command=lambda:func(0)).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="black",fg="white",command=lambda:func(1)).grid(row=2,column=2)
sciss = Button(root,width=20,height=2,text="SCISSORS",bg="black",fg="white",command=lambda:func(2)).grid(row=2,column=3)



root.mainloop()
