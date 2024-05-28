from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

order = 120

root=Tk()

ancho=1130
alto=600


anchoalto=str(ancho-15)+"x"+str(alto)
root.geometry(anchoalto)
root.resizable(False, False)


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
third_frame = Frame(width=700,height=700)
third_frame.place(x=300,y=20)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

cevablar=("12345ABCDEabcde")

answers = open('answers_'+str(order)+'.txt').readlines()

def myFunction(event=None):
    Dogru = 0
    Yanlis = 0
    Bos = 0

    for i in range(1,order+1):
        if questions[i-1].get() == "" or questions[i-1].get()[0] not in (cevablar) or answers[i-1][0]==" ":
            sign[i-1]['text']=""
            Bos+=1
        elif questions[i-1].get()[0] in answers[i-1]:
                sign[i-1]['text']="✔️"
                sign[i-1]['fg']="green"
                Dogru+=1
        else:
            sign[i-1]['text']="X"
            sign[i-1]['fg']="red"
            Yanlis+=1

    net = (Dogru-Yanlis/4)
    yuz = (net*100/order)
    

    root.title("Dogru = %d/%d                                Yanlis = %d/%d                                Bos = %d/%d                                NET = %.2f                                %c %.2f"%(int(Dogru),order,int(Yanlis),order,int(Bos),order,net,'%',yuz))

    if yuz < 49:
        fullscore['bg']="red"
    if yuz > 49:
        fullscore['bg']="orange"
    if yuz > 74:
        fullscore['bg']="light green"


    fullscore['text']=("Dogru = %d/%d                                \n                                NET = %.2f/%d\nYanlis = %d/%d                                \n                                %c %.2f\nBos = %d/%d                                "%(int(Dogru),order,net,order,int(Yanlis),order,'%',yuz,int(Bos),order))
    system("cls")
    print(fullscore['text'])

def key_handler(event=None):
    if (event.keysym in "abbcde12345ABCDE"):
        event.widget.tk_focusNext().focus()
    if (event.keysym == "BackSpace"):
        event.widget.tk_focusPrev().focus()
    myFunction()

root.bind('<Return>',myFunction)
root.bind('<Key>', key_handler)


fullscore = Label(third_frame,text="Dogru = /"+str(order)+"                                \n                                NET = /"+str(order)+"\nYanlis = /"+str(order)+"                                \n                                % \nBos = /"+str(order)+"                                ",fg='white',bg="black",font=("Roboto",25))
fullscore.place(x=0,y=0)

sign = []
questions = []
for i in range(1,order+1):
    sign.append(Label(second_frame,text="",fg='green',font=("Roboto",25)))
    sign[i-1].place(x=150,y=20+(i-1)*50)
    Label(second_frame,text=i,font=("Roboto",25)).place(x=20,y=20+(i-1)*50)
    questions.append(Entry(second_frame,width=2,font=('Arial 24')))
    questions[i-1].place(x=100,y=20+(i-1)*50)
    second_frame.configure(height=53*i)


second_frame.configure(height=6144.0)


root.mainloop()
