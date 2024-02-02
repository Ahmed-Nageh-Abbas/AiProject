from tkinter import *
from tkinter import messagebox
import pygame
from copy import deepcopy


def form1(Admin):
  background ="#000000"
  framebg ="#EDEDED"
  framefg="#6666cc" 
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #insert image
  image_path = "img/pf.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")

  # Create a Label for text on the right side
  heading = Label(text='Welcome to our Game',fg=framefg,bg=background,font=('Times',25,'bold'))
  heading.place(x=510,y=50)

  #Button 1
  button = Button(width=20, pady=5, text="You Play", bg='#6666cc', fg='#000000', border=2, cursor='hand2', command=lambda:[Admin.change(2),root.destroy()],
                  font=('Times', 14, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=560, y=220)
  #Button(width=20,pady=5,text="You Play",bg='#6666cc',fg='white',border=2,cursor='hand2',font=('Arial',14,'bold')).place(x=560,y=220)
  # Button 2
  button = Button(width=20, pady=5, text="I Play", bg='#6666cc', fg='#000000', border=2, cursor='hand2',command=lambda:[Admin.change(3),root.destroy()],
                  font=('Times', 14, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=560, y=350)
  root.mainloop()