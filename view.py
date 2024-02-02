from tkinter import *
from tkinter import messagebox
import pygame
from copy import deepcopy

def form3(Admin):
  background ="#000000"
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #frame = Frame(root,width=950,height=650)
  #insert image 2
  image_path = "img/ppy.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")
  # enter id 
  def on_enter(e):
    code.delete(0,'end')

  def on_leave(e):
    name = code.get()
    if name == '':
      code.insert(0,'ID')

  code = Entry(width=25,fg='#333366',border=0,bg='black',font=('Times',16,'bold'))
  code.place(x=640,y=130)
  code.insert(0,'ID')
  code.bind('<FocusIn>',on_enter)
  code.bind('<FocusOut>',on_leave)
  Frame(width=200,height=1,bg='#333366').place(x=625,y=160)

  #Button 1
  button = Button(width=17, pady=4, text="Solution 1", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,1,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=200)

  #Button 2
  button = Button(width=17, pady=4, text="Solution 2", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,2,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=270)

  #Button 3
  button = Button(width=17, pady=4, text="Solution 3", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,3,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=340)

  #Button 4
  button = Button(width=17, pady=4, text="Solution 4", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,4,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=410)

    #Button 5
  button = Button(width=17, pady=4, text="Solution 5", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,5,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=480)



  root.mainloop()

def form2(Admin):
  background ="#000000"
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #insert image 2
  image_path = "img/iio.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")

  # Create a Label for text on the right side
  heading = Label(text='Choose Level',fg="#990066",bg=background,font=('Times',25,'bold'))
  heading.place(x=580,y=100)

  #Button 1
  button = Button(width=15, pady=4, text="Level 1", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(111),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=190)

  #Button 2
  button = Button(width=15, pady=4, text="Level 2", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(222),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=290)
  #Button 3

  button = Button(width=15, pady=4, text="Level 3", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(333),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=390)

  # Create a Label for id 1
  heading = Label(text='ID = 111',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=190)

  # Create a Label for id 2
  heading = Label(text='ID = 222',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=290)

    # Create a Label for id 3
  heading = Label(text='ID = 333',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=390)
  root.mainloop()

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