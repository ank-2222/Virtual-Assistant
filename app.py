from tkinter import *
# import tkinter.font
from turtle import width 
# from tkinter.ttk import *
# from turtle import onclick
    
# writing code needs to
# create the main window of 
# the application creating 
# main window object named root
root = Tk()
  
# giving title to the main window
root.title("ChatBot")

# Label is what output will be 
# show on the window
# helv36 = tk.Font(family="Helvetica",size=36,weight="bold")

label = Label(root, text ="Hey am Winsey!!!", font=("ubuntu",30), fg="#900C3F", pady=250, padx=50).pack()
  
img = PhotoImage(file='pics/1.png')

 
main_button = Button(root, image=img, width=70, height=70, fg="white", bg="#F0F0F0", bd=0)
main_button.place(relx=0.5, rely=0.8, anchor=CENTER)
user_name = Label(root, text = "Username").place(x = 40, y = 60)
# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying 
root.mainloop()

