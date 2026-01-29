from tkinter import *
from random import randint

screen = Tk()
screen.title("Roulette")
screen.configure(bg="#88BDF2")
screen.geometry("1000x700")

balance = 3000
bet = 100
sel_no = None
sel_type = None

r_clr = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
b_clr = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

# ----------------------------------------------------------------
def mychoice_no(n):
    global sel_no , sel_type
    sel_no = n
    sel_type = None
    s_lbl.config(text = f"Selected : {n}")

def mychoice_type(t):
    global sel_no , sel_type
    sel_no = None
    sel_type = t
    s_lbl.config(text = f"Selected : {t}")
    
# ----------------------------------------------------------------
def spin():
    global balance

    if sel_no is None and sel_type is None:
        i_lbl.config(text = "Firstly bet select kr")
        return
    
    result = randint(0,36)
    r_lbl.config(text=f"Result : {result}")

    win = False

    if sel_no is not None and result == sel_no:
       balance += bet * 36
       win = True

    elif sel_type ==  "red" and result in r_clr:
        balance += bet * 2
        win = True

    elif sel_type  == "black" and result in b_clr:
        balance += bet * 2
        win = True

    elif sel_type ==  "Odd" and result % 2 == 1:
        balance += bet * 2
        win = True

    elif sel_type == "Even" and result % 2 == 0 and result != 0:
        balance += bet * 2
        win = True

    elif sel_type == "1-18" and result <=18 :
        balance += bet * 2
        win = True

    elif sel_type ==  "19-36" and result >= 19:
        balance += bet * 2
        win = True 

    elif sel_type == "1st12" and  (result >=1 and result <= 12) :
        balance += bet * 2
        win = True

    elif sel_type == "2nd12" and (result >=13 and result <= 24):
        balance += bet * 2
        win = True

    elif sel_type == "3rd12" and  (result >= 25 and result <= 36):
        balance += bet * 2
        win = True

    else:
        balance -= bet

    b_lbl.config(text=f"Balance : {balance}")

    if win:
        i_lbl.config(text=" YOU WIN")
    else:
        i_lbl.config(text=" YOU LOSE")


# --------------------------- BUTTONS----------------------------
def f_row():
    x, y = 100, 10
    for i in range(3, 37, 3):
        clr = "red" if i in r_clr else "black"
        Button(screen,text=i,bg=clr,fg="white",width=6,height=2,font=('arial',19,'bold'),command=lambda n=i: mychoice_no(n)).place(x=x,y=y)
        x += 100

def s_row():
    x, y = 100, 85
    for i in range(2, 37, 3):
        clr = "red" if i in r_clr else "black"
        Button(screen,text=i,bg=clr,fg="white",width=6,height=2,font=('arial',19,'bold'),command=lambda n=i: mychoice_no(n)).place(x=x,y=y)
        x += 100

def t_row():
    x, y = 100, 160
    for i in range(1, 37, 3):
        clr = "red" if i in r_clr else "black"
        Button(screen,text=i,bg=clr,fg="white",width=6,height=2,font=('arial',19,'bold'),command=lambda n=i: mychoice_no(n)).place(x=x,y=y)
        x += 100

def zero():
    Button(screen,text=0,bg="green",fg="white",width=6,height=7,font=('arial',19,'bold'),command = lambda : mychoice_no(0)).place(x=5,y=10)

def bottom_buttons():
    Button(screen,text="1st12",bg="green",fg="white",width=26,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("1st12") ).place(x=104,y=242)

    Button(screen,text="2nd12",bg="green",fg="white", width=26,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("2nd12")).place(x=500,y=242)

    Button(screen,text="3rd12",bg="green",fg="white",width=26,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("3rd12")).place(x=900,y=242)

    Button(screen,text="1-18",bg="green",fg="white",width=12,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("1-18")).place(x=104,y=320)

    Button(screen,text="Even",bg="green",fg="white",width=13,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("Even")).place(x=295,y=320)

    Button(screen,bg="red",fg="white",width=13,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("red")).place(x=500,y=320)

    Button(screen,bg="black",fg="white",width=13,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("black") ).place(x=700,y=320)

    Button(screen,text="Odd",bg="green",fg="white", width=14,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("Odd")).place(x=900,y=320)

    Button(screen,text="19-36",bg="green",fg="white",width=12,height=2,font=('arial',19,'bold'),command= lambda: mychoice_type("19-36")).place(x=1109,y=320)

# ---------------------------------------------------------------------------------------------------------------------

s_lbl = Label (screen,text = "Selected : ",font = ("arial",19,"bold"), bg = "#88BDF2")
s_lbl.place(x=50,y=460)

i_lbl =Label(screen,text = "",font = ("arial",22,"bold"),bg = "#88BDF2")
i_lbl.place(x=50,y=540)

r_lbl = Label(screen,text="Result : -",font=('arial',18,'bold'),bg="#88BDF2")
r_lbl.place(x=50,y=500)

b_lbl = Label(screen,text=f"Balance : {balance}",font=('arial',20,'bold'),bg="#88BDF2")
b_lbl.place(x=50,y=420)
# ---------------------------------------------------------------------------------------------------------------------

Button(screen,text="SPIN",bg="gold", font=('arial',25,'bold'), width=10,command=spin).place(x=450,y=580)

f_row()
s_row()
t_row()
zero()
bottom_buttons()

screen.mainloop()