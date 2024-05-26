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

answers = open('answers_120.txt').readlines()

def myFunction(event=None):
    Dogru = 0
    Yanlis = 0
    Bos = 0

    for i in range(1,order+1):
        if questions.get() == "" or questions.get()[0] not in (cevablar):
            sign[i]['text']=""
            Bos+=1
        elif questions.get().get()[0] in answers[0]:
                sign[i]['text']="✔️"
                sign[i]['fg']="green"
                Dogru+=1
        else:
            sign[i]['text']="X"
            sign[i]['fg']="red"
            Yanlis+=1

    net = (Dogru-Yanlis/4)
    yuz = (net*100/120)
    

    root.title("Dogru = %d/120                                Yanlis = %d/120                                Bos = %d/120                                NET = %.2f                                %c %.2f"%(int(Dogru),int(Yanlis),int(Bos),net,'%',yuz))

    if yuz < 49:
        fullscore['bg']="red"
    if yuz > 49:
        fullscore['bg']="orange"
    if yuz > 74:
        fullscore['bg']="light green"


    fullscore['text']=("Dogru = %d/120                                \n                                NET = %.2f/120\nYanlis = %d/120                                \n                                %c %.2f\nBos = %d/120                                "%(int(Dogru),net,int(Yanlis),'%',yuz,int(Bos)))
    system("cls")
    print(fullscore['text'])

def key_handler(event=None):
    if event and event.keysym in (cevablar):
        pyautogui.press("tab")
    if event.keysym=="BackSpace":
        pyautogui.hotkey('shift', 'tab')
    myFunction()

root.bind('<Return>',myFunction)
root.bind('<Key>', key_handler)


fullscore = Label(third_frame,text="Dogru = /120                                \n                                NET = /120\nYanlis = /120                                \n                                % \nBos = /120                                ",fg='white',bg="black",font=("Roboto",25))
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