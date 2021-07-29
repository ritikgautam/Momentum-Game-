#import modules

from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import os
import pygame
from time import sleep
import csv
pygame.init()


gk=0
filename = "img/login/db.csv"
# tix=Label
# rix=Label


# Designing window for registration

def register():
    #global register_screen
    #register_screen = Toplevel(main_screen)
    main_screen.title("Register")
    #register_screen.geometry("300x250")

    image1 = Image.open("img/login/7f.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=-9, y=-4)

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    login_font=('Bahnschrift',15)

   
    username_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=username )
    username_entry.place(x=890,y=250+200,height=30,width=250)
    username_entry.insert(0,'Enter Username:')

    username_entry.bind("<Button-1>", click_but3)
    username_entry.bind("<Leave>", leave_but3)
        
    
    password_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=password )
    password_entry.place(x=890,y=310+200,height=30,width=250)
    password_entry.insert(0,'Enter Password:')

    password_entry.bind("<Button-1>", click_but4)
    password_entry.bind("<Leave>", leave_but4)


    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 12, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])
    

    
    
    but1=ttk.Button(text="REGISTER", style="TButton", command = preregister)
    but1.place(x=940,y=370+200)
    but2=ttk.Button(text="⌂ HOME", style="TButton", command = go_home)
    but2.place(x=940,y=420+200)

   

    
    main_screen.mainloop()
    # password_lable = Label(register_screen, text="Password * ")
    # password_lable.pack()
    # password_entry = Entry(register_screen, textvariable=password, show='*')
    # password_entry.pack()
    # Label(register_screen, text="").pack()
    # Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    #login_screen = Tk()#Toplevel(main_screen)
    #main_screen.destroy()
    main_screen.title("Login")
    #login_screen.geometry("1536x800")




    

    

    # Create a photoimage object of the image in the path
    image1 = Image.open("img/login/8f.png")
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=-9, y=-4)
    #login_screen.mainloop()
    

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    login_font=('Bahnschrift',15)

    # label2=Label(main_screen, text="Username * ")
    # label2.place(x=300, y=100)
    username_login_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font ,textvariable=username_verify)
    username_login_entry.place(x=90, y=250,height=30,width=250)
    username_login_entry.insert(0,'Enter Username:')
        
    username_login_entry.bind("<Button-1>", click_but1)
    username_login_entry.bind("<Leave>", leave_but1)
        
    
    password_login_entry = Entry(main_screen,bg='light grey' ,relief='groove' ,font=login_font , textvariable=password_verify, )
    password_login_entry.place(x=90,y=310,height=30,width=250)
    password_login_entry.insert(0,'Enter Password:')

    password_login_entry.bind("<Button-1>", click_but2)
    password_login_entry.bind("<Leave>", leave_but2)


    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 12, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])
    

    
    
    but1=ttk.Button(text="LOGIN", style="TButton", command = login_verify)
    but1.place(x=140,y=370)
    but2=ttk.Button(text="⌂ HOME", style="TButton", command = go_home)
    but2.place(x=140,y=420)

    
    main_screen.mainloop()

# call function when we click on entry box
def click_but1(*args):
    username_login_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but1(*args):
    # username_login_entry.delete(0, 'end')
    # username_login_entry.insert(0, 'Enter Username:',)
    xxx=10

def click_but2(*args):
    password_login_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but2(*args):
    # password_login_entry.delete(0, 'end')
    # password_login_entry.insert(0, 'Enter Password:',)
    xxx=10





  
# call function when we leave entry box
def leave_but3(*args):
    #username_entry.delete(0, 'end')
    #username_entry.insert(0, 'Enter Username:',)
    xxx=10

def click_but4(*args):
    password_entry.delete(0, 'end')
  
# call function when we leave entry box
def leave_but4(*args):
    #password_entry.delete(0, 'end')
    #password_entry.insert(0, 'Enter Password:',)
    xxx=10



    
# Implementing event on register button
def preregister():
    username_info = username.get()
    password_info = password.get()
    global rix
    r = csv.reader(open(filename,newline='')) # Here your csv file
    lines = list(r)

    lnf=0
    

    col_len=len(lines)

    for ele in range(col_len):
        if username_info==lines[ele][1]:
            lnf=0
            rix=Label(main_screen, text="Username exists!", fg="red", font=("calibri", 13))
            rix.place(x=925+13,y=620+50)
            break
        else:
            lnf=1
    
    if lnf==1:
        register_user()
    



def register_user():

    username_info = username.get()
    password_info = password.get()
    global tix

    # file = open(username_info, "w")
    # file.write(username_info + "\n")
    # file.write(password_info + "\n")
    # file.write("Level 1 : NA")
    # file.close()

    

    # r = csv.reader(open(filename,newline='')) # Here your csv file
    # lines = list(r)

    # unf=0
    # pnf=0

    # col_len=len(lines)

    # for ele in range(col_len):
    #     if username_info==lines[ele][1]:
    #         username_notexist()
    
    
    
    

    
    
    fields=['nmk',username_info,password_info,'NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA']

    with open(filename, 'a',newline='') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)
                        
        # writing the fields
        csvwriter.writerow(fields)




    username_entry.delete(0, END)
    password_entry.delete(0, END)

                    

    tix=Label(main_screen, text="Registration Success!", fg="green", font=("calibri", 13))
    tix.place(x=925,y=620+50)

    gk=1

    
    

    
    

    
    #sleeper()
    
    

def click_but3(*args):
    username_entry.delete(0, 'end')
    tix.destroy()
    rix.destroy()





def sleeper():
    
    sleep(4)
    tix.destroy()
    
# Implementing event on login button 

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    r = csv.reader(open(filename,newline='')) # Here your csv file
    lines = list(r)

    unf=0
    pnf=0

    col_len=len(lines)

    for ele in range(col_len):
        if username1==lines[ele][1]:
            unf=3
            if password1==lines[ele][2]:
                pnf=3
                lines[ele][0]='mk'
                login_sucess()
            else:
                if pnf!=3:
                    pnf=1
        else:
            if unf!=3:
                unf=1

    if unf==1:
        user_not_found()
    if pnf==1:
        password_not_recognised()

    writer = csv.writer(open(filename, 'w', newline=''))
    writer.writerows(lines)

    

    # if username1 in lines:
    #     os.O_EXLOCK
    # else:
    #     user_not_found()
    # list_of_files = os.listdir()
    # if username1 in list_of_files:
    #     file1 = open(username1, "r")
    #     verify = file1.read().splitlines()
    #     if password1 in verify:
    #         login_sucess()

    #     else:
    #         password_not_recognised()

    # else:
    #     user_not_found()
    



# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(main_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(main_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(main_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups
###################################################################################




def delete_login_success():

    login_success_screen.destroy()
    main_screen.destroy()
    os.system('maingame_lev1-Copy.py')
    



######################################################################################
def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def go_home():
    main_screen.destroy()
    main_account_screen()

# Designing Main(first) window


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1536x800")
    main_screen.title("Account Login")
    
    bgrnd = PhotoImage(file="img/login/1bg.png")

    #creating canvas
    canva = Canvas(main_screen, width=1536, height=800)
    
    canva.pack(fill="both", expand=True)

    canva.create_image(-9,-4,image=bgrnd,anchor="nw")

    
    

    #STyle Buttons
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TButton", font =('century gothic', 20, 'bold'),borderwidth = '5')
    style.map("TButton", foreground = [('!active', 'white'),('pressed','green'),('active','black')],background = [('!active', 'black'),('pressed','white'),('active','white')])

    # Create Buttons
   
   # Label(text="").pack()
    but1=ttk.Button(text="LOGIN", style="TButton", command = login)
    but2=ttk.Button(text="REGISTER", style="TButton", command = register)
    
    #but1.grid(row = 0, column = 3, padx = 100)
 
    # Label(text="").pack()
    # Button(text="Register", height="2", width="30", command=register).pack()

    
    # button1 = Button( root, text = "Exit")
    # button3 = Button( root, text = "Start")
    # button2 = Button( root, text = "Reset")
 


    # Display Buttons
    button1_canvas = canva.create_window( 570, 150,anchor = "nw", window = but1)
    button2_canvas = canva.create_window( 870, 150,anchor = "nw", window = but2)
    
    # button2_canvas = canvas1.create_window( 100, 40,anchor = "nw",window = button2)
    
    # button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",window = button3)



    # root = Tk()
    # bg_image = PhotoImage(file="C:/Users/Matteo/Desktop/fisica.png")
    # Label(root, image=bg_image)
    # app = App(root,image=bg_image)
    # root.title("Fisica")
    # root.geometry("330x470")
    # root.mainloop()


   # Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    

    #1536 x 800

    main_screen.mainloop()

main_account_screen()
