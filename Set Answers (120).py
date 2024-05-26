from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

order = 120

system("del answers_"+str(order)+".txt") ##If it is exist

root = Tk()

alto=600
ancho=1130

anchoalto=str(ancho-15)+"x"+str(alto)

root.geometry(anchoalto)
root.resizable(False,False)


main_frame = Frame(root,width=ancho,height=alto)
main_frame.place(x=0,y=0)

my_canvas = Canvas(main_frame, width=ancho, height=alto)
my_canvas.place(x=0,y=0)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.place(x=1100,y=0,height=alto)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)


second_frame = Frame(my_canvas,width=ancho,height=alto)
second_frame.place(x=0,y=0)
third_frame = Frame(width=500,height=500)
third_frame.place(x=500,y=50)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

A="Aa1"
B="Bb2"
C="Cc3"
D="Dd4"
E="Ee5"

def myFunction(event=None):
    set_ans()

def key_handler(event=None):
    if (event.keysym in "abbcde12345ABCDE"):
        event.widget.tk_focusNext().focus()
    if (event.keysym == "BackSpace"):
        event.widget.tk_focusPrev().focus()


root.bind('<Return>',myFunction)
root.bind('<Key>', key_handler)


def set_ans():
    for num in range(1,order+1):
        if variables[num-1].get() == "":
            line=""
        elif variables[num-1].get() in A:
            line = A
        elif variables[num-1].get() in B:
            line = B
        elif variables[num-1].get() in C:
            line = C
        elif variables[num-1].get() in D:
            line = D
        elif variables[num-1].get() in E:
            line = E

        with open("answers_"+str(order)+".txt", "a") as f:f.write(line+" . \n")
    
    root.destroy()
    system("cls")
    system('"correction machine ('+str(order)+')GUI.py"')

set = Button(third_frame,text='set the ansewrs', font=("Roboto", 30),bg='green',fg="red",command=set_ans)
set.place(x=0,y=0)

variables = []

for i in range(1,order+1):
    Label(second_frame,text=i,font=("Roboto",25)).place(x=20,y=20+(i-1)*50)
    variables.append(Entry(second_frame,width=2,font=('Arial 24')))
    variables[i-1].place(x=100,y=20+(i-1)*50)

second_frame.configure(height=6144.0)
root.mainloop()