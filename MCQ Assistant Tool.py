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
    first_line1=("""from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

system("del answers_"""+str(Number)+""".txt") ##If it is exist

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

A="A","a","1"
B="B","b","2"
C="C","c","3"
D="D","d","4"
E="E","e","5"

def myFunction(event=None):
    set_ans()



def key_handler(event=None):
    if event and event.keysym in (A+B+C+D+E):
        pyautogui.press("tab")
    if event.keysym=="BackSpace":
        pyautogui.hotkey('shift', 'tab')


root.bind('<Return>',myFunction)
root.bind('<Key>', key_handler)


def set_ans():""")

    f = open(file1, "w", encoding="utf-8")  # Opening file1 for writing
    f.write(first_line1)    # Writing the initial part of the code to file1
    f.close()   # Closing file1
    
    # Writing to file1: setting answers
    for A in range(1,int(Number)+1):
        with open(file1, "a",encoding='utf-8') as f:f.write("""\n    with open("answers_"""+Number+""".txt", "a") as f:f.write(s"""+str(A)+""".get().replace("a","aA1").replace("A","aA1").replace("1","aA1").replace("b","bB2").replace("B","bB2").replace("2","bB2").replace("c","cC3").replace("C","cC3").replace("3","cC3").replace("d","dD4").replace("D","dD4").replace("4","dD4").replace("e","eE5").replace("E","eE5").replace("5","eE5")+" . \\n")""")
    with open(file1, "a",encoding='utf-8') as f:
        # Adding the rest of the code to file1
        f.write("""\n
    root.destroy()
    system("cls")
    system('"correction machine ("""+str(A)+""")GUI.py"')""")
    with open(file1, "a",encoding='utf-8') as f:f.write("""\nset = Button(third_frame,text='set the ansewrs', font=("Roboto", 30),bg='green',fg="red",command=set_ans)
set.place(x=0,y=0)
""")
    for A in range(1,int(Number)+1):
        with open(file1, "a",encoding='utf-8') as f:f.write("""\nLabel(second_frame,text="""+str(A)+""",font=("Roboto",25)).place(x=20,y="""+str(A*50-30)+""")
s"""+str(A)+"""=Entry(second_frame,width=2,font=('Arial 24'))
s"""+str(A)+""".place(x=100,y="""+str(A*50-30)+""")""")
    with open(file1, "a",encoding='utf-8') as f:f.write("""\nsecond_frame.configure(height="""+str(51.2*int(Number))+""")
root.mainloop()""")
    
    
    ##---------------------------------##
    
    # Adding the initial part of the code for file2
    first_line2="""from os import system
from tkinter import *
from tkinter import ttk
try:import pyautogui
except:
    system("pip install pyautogui")
    system("cls")
    import pyautogui

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

answers = open('answers_"""+str(Number)+""".txt').readlines()

def myFunction(event=None):
    
    Dogru = 0
    Yanlis = 0
    Bos = 0\n"""
    
    
    f = open(file2, "w", encoding="utf-8")  # Opening file2 for writing
    f.write(first_line2)  # Writing the initial part of the code to file2
    f.close()  # Closing after writing the first lines file2
    
    for A in range(1,int(Number)+1):
        with open(file2, "a",encoding='utf-8') as f:
            # Writing to file2: checking answers
            f.write("""    if s"""+str(A)+""".get() == "" or s"""+str(A)+""".get()[0] not in (cevablar):
        tr"""+str(A)+"""['text']=""
        Bos+=1
    else:
        if s"""+str(A)+""".get()[0] in answers["""+str(A-1)+"""]:
            tr"""+str(A)+"""['text']="✔️"
            tr"""+str(A)+"""['fg']="green"
            Dogru+=1
        else:
            tr"""+str(A)+"""['text']="X"
            tr"""+str(A)+"""['fg']="red"
            Yanlis+=1\n""")
    
    with open(file2, "a") as f:
        # Adding the rest of the code to file2
        f.write("""    net = (Dogru-Yanlis/4)
    yuz = (net*100/"""+str(Number)+""")
    

    root.title("Dogru = %d/"""+str(Number)+"""                                Yanlis = %d/"""+str(Number)+"""                                Bos = %d/"""+str(Number)+"""                                NET = %.2f                                %c %.2f"%(int(Dogru),int(Yanlis),int(Bos),net,'%',yuz))

    if yuz < 50:
        fullscore['bg']="red"
    elif yuz >= 50 and yuz<75:
        fullscore['bg']="orange"
    else:
        fullscore['bg']="light green"


    fullscore['text']=("Dogru = %d/"""+str(Number)+"""                                \\n                                NET = %.2f/"""+str(Number)+"""\\nYanlis = %d/"""+str(Number)+"""                                \\n                                %c %.2f\\nBos = %d/"""+str(Number)+"""                                "%(int(Dogru),net,int(Yanlis),'%',yuz,int(Bos)))
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


fullscore = Label(third_frame,text="Dogru = /"""+Number+"""                                \\n                                NET = /"""+Number+"""\\nYanlis = /"""+Number+"""                                \\n                                % \\nBos = /"""+Number+"""                                ",fg='white',bg="black",font=("Roboto",25))
fullscore.place(x=0,y=0)

""")
    
    for A in range(1,int(Number)+1):
        with open(file2, "a",encoding='utf-8') as f:f.write("""\ntr"""+str(A)+""" = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr"""+str(A)+""".place(x=150,y="""+str(A*50-30)+""")""")

    with open(file2, "a",encoding='utf-8') as f:f.write("\n\n\n")
    
    for A in range(1,int(Number)+1):
        with open(file2, "a",encoding='utf-8') as f:f.write("""Label(second_frame,text="""+str(A)+""",font=("Roboto",25)).place(x=20,y="""+str(A*50-30)+""")
s"""+str(A)+"""=Entry(second_frame,width=2,font=('Arial 24'))
s"""+str(A)+""".place(x=100,y="""+str(A*50-30)+""")
second_frame.configure(height="""+str(A*53)+""")\n""")

    with open(file2, "a",encoding='utf-8') as f:f.write("""\nsecond_frame.configure(height="""+str(51.2*int(Number))+""")


root.mainloop()""")
    
    ##---------------------------------##
    
    root.destroy()  # Destroying the main tkinter window after creating the files
    system('"'+file1+'"')   # Running the first file (setting the Answers file)




# Main function to create the Tkinter window and handle input
if __name__ == '__main__':

    root=Tk()  # Creating the main Tkinter window

    root.geometry("200x100")
    root.resizable(False, False)    # Making the window non-resizable

    text=Label(text="Enter Num",font=("Roboto",20)) # Creating a label widget
    text.place(x=35,y=0)    # Placing the label at (35,0)

    num = Entry(width=8, font=('Arial 24'))  # Creating an entry widget for user input
    num.insert(0, "0")  # Inserting a default value in the entry widget
    num.place(x=0, y=60)  # Placing the entry widget at (0,60)


    start = Button(text="Start", width=4, font=('Arial 15'), bg="green", command=myFunction)  # Creating a button widget
    start.place(x=146, y=60)  # Placing the button at (146,60)

    root.bind('<Return>', myFunction)  # Binding Enter key press event to myFunction

    root.mainloop()  # Running the Tkinter event loop

