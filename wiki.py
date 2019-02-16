from tkinter import *
from PIL import ImageTk,Image

import wikipedia
root=Tk()
root.title('WIKIPEDIA')
root.config(bg='gray21')
root.geometry('1500x700')
 
#############################


#################

def about():
	 
	t1 = Toplevel(root)
	t1.config(bg="chocolate2")
	t1.title("About")
	about = Label(t1, text='About',bg="chocolate1",relief=SUNKEN,font=("Courier",40,'bold'))
	about.pack(padx=10, pady=10,fill=BOTH)	
	text_widget = Text(t1,bg="chocolate1",height=35,width=60,relief=GROOVE,font=("Courier",10,'bold'))
	text_widget.insert(END,"This is a very simple program to demonstrate the use of wikipedia api and tkinter library \n Make sure you are connected to the internet!!!  ")
	text_widget.pack(padx=10,pady=10,fill=BOTH)
	text_widget.config(state=DISABLED)
		

############################
def click():
	display.config(state=NORMAL)
	display.delete(0.0,END)
	text = entry.get()
	
	a=wikipedia.summary(text)
	display.insert(END,a )
	display.config(state=DISABLED)


	 
 
############################
# creates a grid 50 x 50 in the main window




c=0
while c < 300:
    root.columnconfigure(c,weight=2)
    root.rowconfigure(c,weight=2)
    c += 1

 

Label(root,text='WIKIPEDIA',font=('Courier',50,'bold'),fg='gray18',relief=GROOVE).grid(row=100,column=150)
entry = Entry(root,bg="chocolate1")
entry.grid(row=110,column=150)
button = Button(root,text='search',fg='gray18',relief=GROOVE,command= lambda:click())
button.grid(row=119,column=150)
 

#button=Button(root,text='SUBMIT',font=####('arial',10),fg='gray18',relief=RIDGE,command= lambda :click()).grid#(row=16,column=280)

 

 
###########
menubar = Menu(root)
filemenu = Menu(menubar)

 
menubar.add_command(label="Exit",command=root.quit)
 

menubar.add_command(label="About",command=about)
root.config(menu=menubar)
###################
 



################

display=Text(root,height=30,width=105,relief=SUNKEN,bg="chocolate3",font=("Verdena",10,'bold'),wrap="word")

display.grid(row=120,column=60)
 

 

img = ImageTk.PhotoImage(Image.open("img.png"))
Label(root,image=img).grid(row=120,column=150)

display.config(state=DISABLED)

root.mainloop()
