from os import system  # Importing system module from the os library
from tkinter import *  # Importing all classes from the tkinter module
from tkinter import ttk  # Importing ttk class from tkinter module


# Function to handle setting answers
def myFunction(event=None):
    Number=num.get() # Extracting the input number from the entry widget
    
    if(int(Number)<5 or int(Number)>655):# Check if the input number is within the specified range
        return 0


    # Creating filenames based on the input number for writing
    file1="Set Answers ("+Number+").py"   # Filename for set answers

    f = open(file1, "a")# Opening the file for appending
    
    
    file2="Correction Machine ("+Number+")GUI.py"   # Filename for correction machine GUI
    f = open(file2, "a")# Opening the file for appending
    
    ##---------------------------------##
    
    # Adding the initial part of the code for file1
    SetAnswersCode=("""from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

order = """+str(Number)+"""
                 

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

        with open("answers_"+str(order)+".txt", "a") as f:f.write(line+" . \\n")
    
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
root.mainloop()""")

    f = open(file1, "w", encoding="utf-8")  # Opening file1 for writing
    f.write(SetAnswersCode)    # Writing the initial part of the code to file1
    f.close()   # Closing file1
    
    
    
    ##---------------------------------##
    
    # Adding the initial part of the code for file2
    CorrectionMachineCode="""from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

order = """+str(Number)+"""


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


    fullscore['text']=("Dogru = %d/%d                                \\n                                NET = %.2f/%d\\nYanlis = %d/%d                                \\n                                %c %.2f\\nBos = %d/%d                                "%(int(Dogru),order,net,order,int(Yanlis),order,'%',yuz,int(Bos),order))
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


fullscore = Label(third_frame,text="Dogru = /"+str(order)+"                                \\n                                NET = /"+str(order)+"\\nYanlis = /"+str(order)+"                                \\n                                % \\nBos = /"+str(order)+"                                ",fg='white',bg="black",font=("Roboto",25))
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

"""
    
    
    f = open(file2, "w", encoding="utf-8")  # Opening file2 for writing
    f.write(CorrectionMachineCode)  # Writing the initial part of the code to file2
    f.close()  # Closing after writing the first lines file2
    
    ##---------------------------------##
    
    root.destroy()  # Destroying the main tkinter window after creating the files
    system('"'+file1+'"')   # Running the first file (setting the Answers file)




# Main function to create the Tkinter window and handle input
if __name__ == '__main__':

    root=Tk()  # Creating the main Tkinter window

    root.geometry("200x100")
    root.resizable(False, False)    # Making the window non-resizable

    text=Label(text="Enter Number",font=("Roboto",20)) # Creating a label widget
    text.place(x=15 ,y=0)    # Placing the label at (35,0)

    num = Entry(width=8, font=('Arial 24'))  # Creating an entry widget for user input
    num.insert(0, "0")  # Inserting a default value in the entry widget
    num.place(x=0, y=60)  # Placing the entry widget at (0,60)


    start = Button(text="Start", width=4, font=('Arial 15'), bg="green", command=myFunction)  # Creating a button widget
    start.place(x=146, y=60)  # Placing the button at (146,60)

    root.bind('<Return>', myFunction)  # Binding Enter key press event to myFunction

    root.mainloop()  # Running the Tkinter event loop