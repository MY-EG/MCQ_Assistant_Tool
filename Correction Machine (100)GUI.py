from os import system
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

answers = open('answers_100.txt').readlines()

def myFunction(event=None):
    
    Dogru = 0
    Yanlis = 0
    Bos = 0
    if s1.get() == "" or s1.get()[0] not in (cevablar):
        tr1['text']=""
        Bos+=1
    else:
        if s1.get()[0] in answers[0]:
            tr1['text']="✔️"
            tr1['fg']="green"
            Dogru+=1
        else:
            tr1['text']="X"
            tr1['fg']="red"
            Yanlis+=1
    if s2.get() == "" or s2.get()[0] not in (cevablar):
        tr2['text']=""
        Bos+=1
    else:
        if s2.get()[0] in answers[1]:
            tr2['text']="✔️"
            tr2['fg']="green"
            Dogru+=1
        else:
            tr2['text']="X"
            tr2['fg']="red"
            Yanlis+=1
    if s3.get() == "" or s3.get()[0] not in (cevablar):
        tr3['text']=""
        Bos+=1
    else:
        if s3.get()[0] in answers[2]:
            tr3['text']="✔️"
            tr3['fg']="green"
            Dogru+=1
        else:
            tr3['text']="X"
            tr3['fg']="red"
            Yanlis+=1
    if s4.get() == "" or s4.get()[0] not in (cevablar):
        tr4['text']=""
        Bos+=1
    else:
        if s4.get()[0] in answers[3]:
            tr4['text']="✔️"
            tr4['fg']="green"
            Dogru+=1
        else:
            tr4['text']="X"
            tr4['fg']="red"
            Yanlis+=1
    if s5.get() == "" or s5.get()[0] not in (cevablar):
        tr5['text']=""
        Bos+=1
    else:
        if s5.get()[0] in answers[4]:
            tr5['text']="✔️"
            tr5['fg']="green"
            Dogru+=1
        else:
            tr5['text']="X"
            tr5['fg']="red"
            Yanlis+=1
    if s6.get() == "" or s6.get()[0] not in (cevablar):
        tr6['text']=""
        Bos+=1
    else:
        if s6.get()[0] in answers[5]:
            tr6['text']="✔️"
            tr6['fg']="green"
            Dogru+=1
        else:
            tr6['text']="X"
            tr6['fg']="red"
            Yanlis+=1
    if s7.get() == "" or s7.get()[0] not in (cevablar):
        tr7['text']=""
        Bos+=1
    else:
        if s7.get()[0] in answers[6]:
            tr7['text']="✔️"
            tr7['fg']="green"
            Dogru+=1
        else:
            tr7['text']="X"
            tr7['fg']="red"
            Yanlis+=1
    if s8.get() == "" or s8.get()[0] not in (cevablar):
        tr8['text']=""
        Bos+=1
    else:
        if s8.get()[0] in answers[7]:
            tr8['text']="✔️"
            tr8['fg']="green"
            Dogru+=1
        else:
            tr8['text']="X"
            tr8['fg']="red"
            Yanlis+=1
    if s9.get() == "" or s9.get()[0] not in (cevablar):
        tr9['text']=""
        Bos+=1
    else:
        if s9.get()[0] in answers[8]:
            tr9['text']="✔️"
            tr9['fg']="green"
            Dogru+=1
        else:
            tr9['text']="X"
            tr9['fg']="red"
            Yanlis+=1
    if s10.get() == "" or s10.get()[0] not in (cevablar):
        tr10['text']=""
        Bos+=1
    else:
        if s10.get()[0] in answers[9]:
            tr10['text']="✔️"
            tr10['fg']="green"
            Dogru+=1
        else:
            tr10['text']="X"
            tr10['fg']="red"
            Yanlis+=1
    if s11.get() == "" or s11.get()[0] not in (cevablar):
        tr11['text']=""
        Bos+=1
    else:
        if s11.get()[0] in answers[10]:
            tr11['text']="✔️"
            tr11['fg']="green"
            Dogru+=1
        else:
            tr11['text']="X"
            tr11['fg']="red"
            Yanlis+=1
    if s12.get() == "" or s12.get()[0] not in (cevablar):
        tr12['text']=""
        Bos+=1
    else:
        if s12.get()[0] in answers[11]:
            tr12['text']="✔️"
            tr12['fg']="green"
            Dogru+=1
        else:
            tr12['text']="X"
            tr12['fg']="red"
            Yanlis+=1
    if s13.get() == "" or s13.get()[0] not in (cevablar):
        tr13['text']=""
        Bos+=1
    else:
        if s13.get()[0] in answers[12]:
            tr13['text']="✔️"
            tr13['fg']="green"
            Dogru+=1
        else:
            tr13['text']="X"
            tr13['fg']="red"
            Yanlis+=1
    if s14.get() == "" or s14.get()[0] not in (cevablar):
        tr14['text']=""
        Bos+=1
    else:
        if s14.get()[0] in answers[13]:
            tr14['text']="✔️"
            tr14['fg']="green"
            Dogru+=1
        else:
            tr14['text']="X"
            tr14['fg']="red"
            Yanlis+=1
    if s15.get() == "" or s15.get()[0] not in (cevablar):
        tr15['text']=""
        Bos+=1
    else:
        if s15.get()[0] in answers[14]:
            tr15['text']="✔️"
            tr15['fg']="green"
            Dogru+=1
        else:
            tr15['text']="X"
            tr15['fg']="red"
            Yanlis+=1
    if s16.get() == "" or s16.get()[0] not in (cevablar):
        tr16['text']=""
        Bos+=1
    else:
        if s16.get()[0] in answers[15]:
            tr16['text']="✔️"
            tr16['fg']="green"
            Dogru+=1
        else:
            tr16['text']="X"
            tr16['fg']="red"
            Yanlis+=1
    if s17.get() == "" or s17.get()[0] not in (cevablar):
        tr17['text']=""
        Bos+=1
    else:
        if s17.get()[0] in answers[16]:
            tr17['text']="✔️"
            tr17['fg']="green"
            Dogru+=1
        else:
            tr17['text']="X"
            tr17['fg']="red"
            Yanlis+=1
    if s18.get() == "" or s18.get()[0] not in (cevablar):
        tr18['text']=""
        Bos+=1
    else:
        if s18.get()[0] in answers[17]:
            tr18['text']="✔️"
            tr18['fg']="green"
            Dogru+=1
        else:
            tr18['text']="X"
            tr18['fg']="red"
            Yanlis+=1
    if s19.get() == "" or s19.get()[0] not in (cevablar):
        tr19['text']=""
        Bos+=1
    else:
        if s19.get()[0] in answers[18]:
            tr19['text']="✔️"
            tr19['fg']="green"
            Dogru+=1
        else:
            tr19['text']="X"
            tr19['fg']="red"
            Yanlis+=1
    if s20.get() == "" or s20.get()[0] not in (cevablar):
        tr20['text']=""
        Bos+=1
    else:
        if s20.get()[0] in answers[19]:
            tr20['text']="✔️"
            tr20['fg']="green"
            Dogru+=1
        else:
            tr20['text']="X"
            tr20['fg']="red"
            Yanlis+=1
    if s21.get() == "" or s21.get()[0] not in (cevablar):
        tr21['text']=""
        Bos+=1
    else:
        if s21.get()[0] in answers[20]:
            tr21['text']="✔️"
            tr21['fg']="green"
            Dogru+=1
        else:
            tr21['text']="X"
            tr21['fg']="red"
            Yanlis+=1
    if s22.get() == "" or s22.get()[0] not in (cevablar):
        tr22['text']=""
        Bos+=1
    else:
        if s22.get()[0] in answers[21]:
            tr22['text']="✔️"
            tr22['fg']="green"
            Dogru+=1
        else:
            tr22['text']="X"
            tr22['fg']="red"
            Yanlis+=1
    if s23.get() == "" or s23.get()[0] not in (cevablar):
        tr23['text']=""
        Bos+=1
    else:
        if s23.get()[0] in answers[22]:
            tr23['text']="✔️"
            tr23['fg']="green"
            Dogru+=1
        else:
            tr23['text']="X"
            tr23['fg']="red"
            Yanlis+=1
    if s24.get() == "" or s24.get()[0] not in (cevablar):
        tr24['text']=""
        Bos+=1
    else:
        if s24.get()[0] in answers[23]:
            tr24['text']="✔️"
            tr24['fg']="green"
            Dogru+=1
        else:
            tr24['text']="X"
            tr24['fg']="red"
            Yanlis+=1
    if s25.get() == "" or s25.get()[0] not in (cevablar):
        tr25['text']=""
        Bos+=1
    else:
        if s25.get()[0] in answers[24]:
            tr25['text']="✔️"
            tr25['fg']="green"
            Dogru+=1
        else:
            tr25['text']="X"
            tr25['fg']="red"
            Yanlis+=1
    if s26.get() == "" or s26.get()[0] not in (cevablar):
        tr26['text']=""
        Bos+=1
    else:
        if s26.get()[0] in answers[25]:
            tr26['text']="✔️"
            tr26['fg']="green"
            Dogru+=1
        else:
            tr26['text']="X"
            tr26['fg']="red"
            Yanlis+=1
    if s27.get() == "" or s27.get()[0] not in (cevablar):
        tr27['text']=""
        Bos+=1
    else:
        if s27.get()[0] in answers[26]:
            tr27['text']="✔️"
            tr27['fg']="green"
            Dogru+=1
        else:
            tr27['text']="X"
            tr27['fg']="red"
            Yanlis+=1
    if s28.get() == "" or s28.get()[0] not in (cevablar):
        tr28['text']=""
        Bos+=1
    else:
        if s28.get()[0] in answers[27]:
            tr28['text']="✔️"
            tr28['fg']="green"
            Dogru+=1
        else:
            tr28['text']="X"
            tr28['fg']="red"
            Yanlis+=1
    if s29.get() == "" or s29.get()[0] not in (cevablar):
        tr29['text']=""
        Bos+=1
    else:
        if s29.get()[0] in answers[28]:
            tr29['text']="✔️"
            tr29['fg']="green"
            Dogru+=1
        else:
            tr29['text']="X"
            tr29['fg']="red"
            Yanlis+=1
    if s30.get() == "" or s30.get()[0] not in (cevablar):
        tr30['text']=""
        Bos+=1
    else:
        if s30.get()[0] in answers[29]:
            tr30['text']="✔️"
            tr30['fg']="green"
            Dogru+=1
        else:
            tr30['text']="X"
            tr30['fg']="red"
            Yanlis+=1
    if s31.get() == "" or s31.get()[0] not in (cevablar):
        tr31['text']=""
        Bos+=1
    else:
        if s31.get()[0] in answers[30]:
            tr31['text']="✔️"
            tr31['fg']="green"
            Dogru+=1
        else:
            tr31['text']="X"
            tr31['fg']="red"
            Yanlis+=1
    if s32.get() == "" or s32.get()[0] not in (cevablar):
        tr32['text']=""
        Bos+=1
    else:
        if s32.get()[0] in answers[31]:
            tr32['text']="✔️"
            tr32['fg']="green"
            Dogru+=1
        else:
            tr32['text']="X"
            tr32['fg']="red"
            Yanlis+=1
    if s33.get() == "" or s33.get()[0] not in (cevablar):
        tr33['text']=""
        Bos+=1
    else:
        if s33.get()[0] in answers[32]:
            tr33['text']="✔️"
            tr33['fg']="green"
            Dogru+=1
        else:
            tr33['text']="X"
            tr33['fg']="red"
            Yanlis+=1
    if s34.get() == "" or s34.get()[0] not in (cevablar):
        tr34['text']=""
        Bos+=1
    else:
        if s34.get()[0] in answers[33]:
            tr34['text']="✔️"
            tr34['fg']="green"
            Dogru+=1
        else:
            tr34['text']="X"
            tr34['fg']="red"
            Yanlis+=1
    if s35.get() == "" or s35.get()[0] not in (cevablar):
        tr35['text']=""
        Bos+=1
    else:
        if s35.get()[0] in answers[34]:
            tr35['text']="✔️"
            tr35['fg']="green"
            Dogru+=1
        else:
            tr35['text']="X"
            tr35['fg']="red"
            Yanlis+=1
    if s36.get() == "" or s36.get()[0] not in (cevablar):
        tr36['text']=""
        Bos+=1
    else:
        if s36.get()[0] in answers[35]:
            tr36['text']="✔️"
            tr36['fg']="green"
            Dogru+=1
        else:
            tr36['text']="X"
            tr36['fg']="red"
            Yanlis+=1
    if s37.get() == "" or s37.get()[0] not in (cevablar):
        tr37['text']=""
        Bos+=1
    else:
        if s37.get()[0] in answers[36]:
            tr37['text']="✔️"
            tr37['fg']="green"
            Dogru+=1
        else:
            tr37['text']="X"
            tr37['fg']="red"
            Yanlis+=1
    if s38.get() == "" or s38.get()[0] not in (cevablar):
        tr38['text']=""
        Bos+=1
    else:
        if s38.get()[0] in answers[37]:
            tr38['text']="✔️"
            tr38['fg']="green"
            Dogru+=1
        else:
            tr38['text']="X"
            tr38['fg']="red"
            Yanlis+=1
    if s39.get() == "" or s39.get()[0] not in (cevablar):
        tr39['text']=""
        Bos+=1
    else:
        if s39.get()[0] in answers[38]:
            tr39['text']="✔️"
            tr39['fg']="green"
            Dogru+=1
        else:
            tr39['text']="X"
            tr39['fg']="red"
            Yanlis+=1
    if s40.get() == "" or s40.get()[0] not in (cevablar):
        tr40['text']=""
        Bos+=1
    else:
        if s40.get()[0] in answers[39]:
            tr40['text']="✔️"
            tr40['fg']="green"
            Dogru+=1
        else:
            tr40['text']="X"
            tr40['fg']="red"
            Yanlis+=1
    if s41.get() == "" or s41.get()[0] not in (cevablar):
        tr41['text']=""
        Bos+=1
    else:
        if s41.get()[0] in answers[40]:
            tr41['text']="✔️"
            tr41['fg']="green"
            Dogru+=1
        else:
            tr41['text']="X"
            tr41['fg']="red"
            Yanlis+=1
    if s42.get() == "" or s42.get()[0] not in (cevablar):
        tr42['text']=""
        Bos+=1
    else:
        if s42.get()[0] in answers[41]:
            tr42['text']="✔️"
            tr42['fg']="green"
            Dogru+=1
        else:
            tr42['text']="X"
            tr42['fg']="red"
            Yanlis+=1
    if s43.get() == "" or s43.get()[0] not in (cevablar):
        tr43['text']=""
        Bos+=1
    else:
        if s43.get()[0] in answers[42]:
            tr43['text']="✔️"
            tr43['fg']="green"
            Dogru+=1
        else:
            tr43['text']="X"
            tr43['fg']="red"
            Yanlis+=1
    if s44.get() == "" or s44.get()[0] not in (cevablar):
        tr44['text']=""
        Bos+=1
    else:
        if s44.get()[0] in answers[43]:
            tr44['text']="✔️"
            tr44['fg']="green"
            Dogru+=1
        else:
            tr44['text']="X"
            tr44['fg']="red"
            Yanlis+=1
    if s45.get() == "" or s45.get()[0] not in (cevablar):
        tr45['text']=""
        Bos+=1
    else:
        if s45.get()[0] in answers[44]:
            tr45['text']="✔️"
            tr45['fg']="green"
            Dogru+=1
        else:
            tr45['text']="X"
            tr45['fg']="red"
            Yanlis+=1
    if s46.get() == "" or s46.get()[0] not in (cevablar):
        tr46['text']=""
        Bos+=1
    else:
        if s46.get()[0] in answers[45]:
            tr46['text']="✔️"
            tr46['fg']="green"
            Dogru+=1
        else:
            tr46['text']="X"
            tr46['fg']="red"
            Yanlis+=1
    if s47.get() == "" or s47.get()[0] not in (cevablar):
        tr47['text']=""
        Bos+=1
    else:
        if s47.get()[0] in answers[46]:
            tr47['text']="✔️"
            tr47['fg']="green"
            Dogru+=1
        else:
            tr47['text']="X"
            tr47['fg']="red"
            Yanlis+=1
    if s48.get() == "" or s48.get()[0] not in (cevablar):
        tr48['text']=""
        Bos+=1
    else:
        if s48.get()[0] in answers[47]:
            tr48['text']="✔️"
            tr48['fg']="green"
            Dogru+=1
        else:
            tr48['text']="X"
            tr48['fg']="red"
            Yanlis+=1
    if s49.get() == "" or s49.get()[0] not in (cevablar):
        tr49['text']=""
        Bos+=1
    else:
        if s49.get()[0] in answers[48]:
            tr49['text']="✔️"
            tr49['fg']="green"
            Dogru+=1
        else:
            tr49['text']="X"
            tr49['fg']="red"
            Yanlis+=1
    if s50.get() == "" or s50.get()[0] not in (cevablar):
        tr50['text']=""
        Bos+=1
    else:
        if s50.get()[0] in answers[49]:
            tr50['text']="✔️"
            tr50['fg']="green"
            Dogru+=1
        else:
            tr50['text']="X"
            tr50['fg']="red"
            Yanlis+=1
    if s51.get() == "" or s51.get()[0] not in (cevablar):
        tr51['text']=""
        Bos+=1
    else:
        if s51.get()[0] in answers[50]:
            tr51['text']="✔️"
            tr51['fg']="green"
            Dogru+=1
        else:
            tr51['text']="X"
            tr51['fg']="red"
            Yanlis+=1
    if s52.get() == "" or s52.get()[0] not in (cevablar):
        tr52['text']=""
        Bos+=1
    else:
        if s52.get()[0] in answers[51]:
            tr52['text']="✔️"
            tr52['fg']="green"
            Dogru+=1
        else:
            tr52['text']="X"
            tr52['fg']="red"
            Yanlis+=1
    if s53.get() == "" or s53.get()[0] not in (cevablar):
        tr53['text']=""
        Bos+=1
    else:
        if s53.get()[0] in answers[52]:
            tr53['text']="✔️"
            tr53['fg']="green"
            Dogru+=1
        else:
            tr53['text']="X"
            tr53['fg']="red"
            Yanlis+=1
    if s54.get() == "" or s54.get()[0] not in (cevablar):
        tr54['text']=""
        Bos+=1
    else:
        if s54.get()[0] in answers[53]:
            tr54['text']="✔️"
            tr54['fg']="green"
            Dogru+=1
        else:
            tr54['text']="X"
            tr54['fg']="red"
            Yanlis+=1
    if s55.get() == "" or s55.get()[0] not in (cevablar):
        tr55['text']=""
        Bos+=1
    else:
        if s55.get()[0] in answers[54]:
            tr55['text']="✔️"
            tr55['fg']="green"
            Dogru+=1
        else:
            tr55['text']="X"
            tr55['fg']="red"
            Yanlis+=1
    if s56.get() == "" or s56.get()[0] not in (cevablar):
        tr56['text']=""
        Bos+=1
    else:
        if s56.get()[0] in answers[55]:
            tr56['text']="✔️"
            tr56['fg']="green"
            Dogru+=1
        else:
            tr56['text']="X"
            tr56['fg']="red"
            Yanlis+=1
    if s57.get() == "" or s57.get()[0] not in (cevablar):
        tr57['text']=""
        Bos+=1
    else:
        if s57.get()[0] in answers[56]:
            tr57['text']="✔️"
            tr57['fg']="green"
            Dogru+=1
        else:
            tr57['text']="X"
            tr57['fg']="red"
            Yanlis+=1
    if s58.get() == "" or s58.get()[0] not in (cevablar):
        tr58['text']=""
        Bos+=1
    else:
        if s58.get()[0] in answers[57]:
            tr58['text']="✔️"
            tr58['fg']="green"
            Dogru+=1
        else:
            tr58['text']="X"
            tr58['fg']="red"
            Yanlis+=1
    if s59.get() == "" or s59.get()[0] not in (cevablar):
        tr59['text']=""
        Bos+=1
    else:
        if s59.get()[0] in answers[58]:
            tr59['text']="✔️"
            tr59['fg']="green"
            Dogru+=1
        else:
            tr59['text']="X"
            tr59['fg']="red"
            Yanlis+=1
    if s60.get() == "" or s60.get()[0] not in (cevablar):
        tr60['text']=""
        Bos+=1
    else:
        if s60.get()[0] in answers[59]:
            tr60['text']="✔️"
            tr60['fg']="green"
            Dogru+=1
        else:
            tr60['text']="X"
            tr60['fg']="red"
            Yanlis+=1
    if s61.get() == "" or s61.get()[0] not in (cevablar):
        tr61['text']=""
        Bos+=1
    else:
        if s61.get()[0] in answers[60]:
            tr61['text']="✔️"
            tr61['fg']="green"
            Dogru+=1
        else:
            tr61['text']="X"
            tr61['fg']="red"
            Yanlis+=1
    if s62.get() == "" or s62.get()[0] not in (cevablar):
        tr62['text']=""
        Bos+=1
    else:
        if s62.get()[0] in answers[61]:
            tr62['text']="✔️"
            tr62['fg']="green"
            Dogru+=1
        else:
            tr62['text']="X"
            tr62['fg']="red"
            Yanlis+=1
    if s63.get() == "" or s63.get()[0] not in (cevablar):
        tr63['text']=""
        Bos+=1
    else:
        if s63.get()[0] in answers[62]:
            tr63['text']="✔️"
            tr63['fg']="green"
            Dogru+=1
        else:
            tr63['text']="X"
            tr63['fg']="red"
            Yanlis+=1
    if s64.get() == "" or s64.get()[0] not in (cevablar):
        tr64['text']=""
        Bos+=1
    else:
        if s64.get()[0] in answers[63]:
            tr64['text']="✔️"
            tr64['fg']="green"
            Dogru+=1
        else:
            tr64['text']="X"
            tr64['fg']="red"
            Yanlis+=1
    if s65.get() == "" or s65.get()[0] not in (cevablar):
        tr65['text']=""
        Bos+=1
    else:
        if s65.get()[0] in answers[64]:
            tr65['text']="✔️"
            tr65['fg']="green"
            Dogru+=1
        else:
            tr65['text']="X"
            tr65['fg']="red"
            Yanlis+=1
    if s66.get() == "" or s66.get()[0] not in (cevablar):
        tr66['text']=""
        Bos+=1
    else:
        if s66.get()[0] in answers[65]:
            tr66['text']="✔️"
            tr66['fg']="green"
            Dogru+=1
        else:
            tr66['text']="X"
            tr66['fg']="red"
            Yanlis+=1
    if s67.get() == "" or s67.get()[0] not in (cevablar):
        tr67['text']=""
        Bos+=1
    else:
        if s67.get()[0] in answers[66]:
            tr67['text']="✔️"
            tr67['fg']="green"
            Dogru+=1
        else:
            tr67['text']="X"
            tr67['fg']="red"
            Yanlis+=1
    if s68.get() == "" or s68.get()[0] not in (cevablar):
        tr68['text']=""
        Bos+=1
    else:
        if s68.get()[0] in answers[67]:
            tr68['text']="✔️"
            tr68['fg']="green"
            Dogru+=1
        else:
            tr68['text']="X"
            tr68['fg']="red"
            Yanlis+=1
    if s69.get() == "" or s69.get()[0] not in (cevablar):
        tr69['text']=""
        Bos+=1
    else:
        if s69.get()[0] in answers[68]:
            tr69['text']="✔️"
            tr69['fg']="green"
            Dogru+=1
        else:
            tr69['text']="X"
            tr69['fg']="red"
            Yanlis+=1
    if s70.get() == "" or s70.get()[0] not in (cevablar):
        tr70['text']=""
        Bos+=1
    else:
        if s70.get()[0] in answers[69]:
            tr70['text']="✔️"
            tr70['fg']="green"
            Dogru+=1
        else:
            tr70['text']="X"
            tr70['fg']="red"
            Yanlis+=1
    if s71.get() == "" or s71.get()[0] not in (cevablar):
        tr71['text']=""
        Bos+=1
    else:
        if s71.get()[0] in answers[70]:
            tr71['text']="✔️"
            tr71['fg']="green"
            Dogru+=1
        else:
            tr71['text']="X"
            tr71['fg']="red"
            Yanlis+=1
    if s72.get() == "" or s72.get()[0] not in (cevablar):
        tr72['text']=""
        Bos+=1
    else:
        if s72.get()[0] in answers[71]:
            tr72['text']="✔️"
            tr72['fg']="green"
            Dogru+=1
        else:
            tr72['text']="X"
            tr72['fg']="red"
            Yanlis+=1
    if s73.get() == "" or s73.get()[0] not in (cevablar):
        tr73['text']=""
        Bos+=1
    else:
        if s73.get()[0] in answers[72]:
            tr73['text']="✔️"
            tr73['fg']="green"
            Dogru+=1
        else:
            tr73['text']="X"
            tr73['fg']="red"
            Yanlis+=1
    if s74.get() == "" or s74.get()[0] not in (cevablar):
        tr74['text']=""
        Bos+=1
    else:
        if s74.get()[0] in answers[73]:
            tr74['text']="✔️"
            tr74['fg']="green"
            Dogru+=1
        else:
            tr74['text']="X"
            tr74['fg']="red"
            Yanlis+=1
    if s75.get() == "" or s75.get()[0] not in (cevablar):
        tr75['text']=""
        Bos+=1
    else:
        if s75.get()[0] in answers[74]:
            tr75['text']="✔️"
            tr75['fg']="green"
            Dogru+=1
        else:
            tr75['text']="X"
            tr75['fg']="red"
            Yanlis+=1
    if s76.get() == "" or s76.get()[0] not in (cevablar):
        tr76['text']=""
        Bos+=1
    else:
        if s76.get()[0] in answers[75]:
            tr76['text']="✔️"
            tr76['fg']="green"
            Dogru+=1
        else:
            tr76['text']="X"
            tr76['fg']="red"
            Yanlis+=1
    if s77.get() == "" or s77.get()[0] not in (cevablar):
        tr77['text']=""
        Bos+=1
    else:
        if s77.get()[0] in answers[76]:
            tr77['text']="✔️"
            tr77['fg']="green"
            Dogru+=1
        else:
            tr77['text']="X"
            tr77['fg']="red"
            Yanlis+=1
    if s78.get() == "" or s78.get()[0] not in (cevablar):
        tr78['text']=""
        Bos+=1
    else:
        if s78.get()[0] in answers[77]:
            tr78['text']="✔️"
            tr78['fg']="green"
            Dogru+=1
        else:
            tr78['text']="X"
            tr78['fg']="red"
            Yanlis+=1
    if s79.get() == "" or s79.get()[0] not in (cevablar):
        tr79['text']=""
        Bos+=1
    else:
        if s79.get()[0] in answers[78]:
            tr79['text']="✔️"
            tr79['fg']="green"
            Dogru+=1
        else:
            tr79['text']="X"
            tr79['fg']="red"
            Yanlis+=1
    if s80.get() == "" or s80.get()[0] not in (cevablar):
        tr80['text']=""
        Bos+=1
    else:
        if s80.get()[0] in answers[79]:
            tr80['text']="✔️"
            tr80['fg']="green"
            Dogru+=1
        else:
            tr80['text']="X"
            tr80['fg']="red"
            Yanlis+=1
    if s81.get() == "" or s81.get()[0] not in (cevablar):
        tr81['text']=""
        Bos+=1
    else:
        if s81.get()[0] in answers[80]:
            tr81['text']="✔️"
            tr81['fg']="green"
            Dogru+=1
        else:
            tr81['text']="X"
            tr81['fg']="red"
            Yanlis+=1
    if s82.get() == "" or s82.get()[0] not in (cevablar):
        tr82['text']=""
        Bos+=1
    else:
        if s82.get()[0] in answers[81]:
            tr82['text']="✔️"
            tr82['fg']="green"
            Dogru+=1
        else:
            tr82['text']="X"
            tr82['fg']="red"
            Yanlis+=1
    if s83.get() == "" or s83.get()[0] not in (cevablar):
        tr83['text']=""
        Bos+=1
    else:
        if s83.get()[0] in answers[82]:
            tr83['text']="✔️"
            tr83['fg']="green"
            Dogru+=1
        else:
            tr83['text']="X"
            tr83['fg']="red"
            Yanlis+=1
    if s84.get() == "" or s84.get()[0] not in (cevablar):
        tr84['text']=""
        Bos+=1
    else:
        if s84.get()[0] in answers[83]:
            tr84['text']="✔️"
            tr84['fg']="green"
            Dogru+=1
        else:
            tr84['text']="X"
            tr84['fg']="red"
            Yanlis+=1
    if s85.get() == "" or s85.get()[0] not in (cevablar):
        tr85['text']=""
        Bos+=1
    else:
        if s85.get()[0] in answers[84]:
            tr85['text']="✔️"
            tr85['fg']="green"
            Dogru+=1
        else:
            tr85['text']="X"
            tr85['fg']="red"
            Yanlis+=1
    if s86.get() == "" or s86.get()[0] not in (cevablar):
        tr86['text']=""
        Bos+=1
    else:
        if s86.get()[0] in answers[85]:
            tr86['text']="✔️"
            tr86['fg']="green"
            Dogru+=1
        else:
            tr86['text']="X"
            tr86['fg']="red"
            Yanlis+=1
    if s87.get() == "" or s87.get()[0] not in (cevablar):
        tr87['text']=""
        Bos+=1
    else:
        if s87.get()[0] in answers[86]:
            tr87['text']="✔️"
            tr87['fg']="green"
            Dogru+=1
        else:
            tr87['text']="X"
            tr87['fg']="red"
            Yanlis+=1
    if s88.get() == "" or s88.get()[0] not in (cevablar):
        tr88['text']=""
        Bos+=1
    else:
        if s88.get()[0] in answers[87]:
            tr88['text']="✔️"
            tr88['fg']="green"
            Dogru+=1
        else:
            tr88['text']="X"
            tr88['fg']="red"
            Yanlis+=1
    if s89.get() == "" or s89.get()[0] not in (cevablar):
        tr89['text']=""
        Bos+=1
    else:
        if s89.get()[0] in answers[88]:
            tr89['text']="✔️"
            tr89['fg']="green"
            Dogru+=1
        else:
            tr89['text']="X"
            tr89['fg']="red"
            Yanlis+=1
    if s90.get() == "" or s90.get()[0] not in (cevablar):
        tr90['text']=""
        Bos+=1
    else:
        if s90.get()[0] in answers[89]:
            tr90['text']="✔️"
            tr90['fg']="green"
            Dogru+=1
        else:
            tr90['text']="X"
            tr90['fg']="red"
            Yanlis+=1
    if s91.get() == "" or s91.get()[0] not in (cevablar):
        tr91['text']=""
        Bos+=1
    else:
        if s91.get()[0] in answers[90]:
            tr91['text']="✔️"
            tr91['fg']="green"
            Dogru+=1
        else:
            tr91['text']="X"
            tr91['fg']="red"
            Yanlis+=1
    if s92.get() == "" or s92.get()[0] not in (cevablar):
        tr92['text']=""
        Bos+=1
    else:
        if s92.get()[0] in answers[91]:
            tr92['text']="✔️"
            tr92['fg']="green"
            Dogru+=1
        else:
            tr92['text']="X"
            tr92['fg']="red"
            Yanlis+=1
    if s93.get() == "" or s93.get()[0] not in (cevablar):
        tr93['text']=""
        Bos+=1
    else:
        if s93.get()[0] in answers[92]:
            tr93['text']="✔️"
            tr93['fg']="green"
            Dogru+=1
        else:
            tr93['text']="X"
            tr93['fg']="red"
            Yanlis+=1
    if s94.get() == "" or s94.get()[0] not in (cevablar):
        tr94['text']=""
        Bos+=1
    else:
        if s94.get()[0] in answers[93]:
            tr94['text']="✔️"
            tr94['fg']="green"
            Dogru+=1
        else:
            tr94['text']="X"
            tr94['fg']="red"
            Yanlis+=1
    if s95.get() == "" or s95.get()[0] not in (cevablar):
        tr95['text']=""
        Bos+=1
    else:
        if s95.get()[0] in answers[94]:
            tr95['text']="✔️"
            tr95['fg']="green"
            Dogru+=1
        else:
            tr95['text']="X"
            tr95['fg']="red"
            Yanlis+=1
    if s96.get() == "" or s96.get()[0] not in (cevablar):
        tr96['text']=""
        Bos+=1
    else:
        if s96.get()[0] in answers[95]:
            tr96['text']="✔️"
            tr96['fg']="green"
            Dogru+=1
        else:
            tr96['text']="X"
            tr96['fg']="red"
            Yanlis+=1
    if s97.get() == "" or s97.get()[0] not in (cevablar):
        tr97['text']=""
        Bos+=1
    else:
        if s97.get()[0] in answers[96]:
            tr97['text']="✔️"
            tr97['fg']="green"
            Dogru+=1
        else:
            tr97['text']="X"
            tr97['fg']="red"
            Yanlis+=1
    if s98.get() == "" or s98.get()[0] not in (cevablar):
        tr98['text']=""
        Bos+=1
    else:
        if s98.get()[0] in answers[97]:
            tr98['text']="✔️"
            tr98['fg']="green"
            Dogru+=1
        else:
            tr98['text']="X"
            tr98['fg']="red"
            Yanlis+=1
    if s99.get() == "" or s99.get()[0] not in (cevablar):
        tr99['text']=""
        Bos+=1
    else:
        if s99.get()[0] in answers[98]:
            tr99['text']="✔️"
            tr99['fg']="green"
            Dogru+=1
        else:
            tr99['text']="X"
            tr99['fg']="red"
            Yanlis+=1
    if s100.get() == "" or s100.get()[0] not in (cevablar):
        tr100['text']=""
        Bos+=1
    else:
        if s100.get()[0] in answers[99]:
            tr100['text']="✔️"
            tr100['fg']="green"
            Dogru+=1
        else:
            tr100['text']="X"
            tr100['fg']="red"
            Yanlis+=1
    net = (Dogru-Yanlis/4)
    yuz = (net*100/100)
    

    root.title("Dogru = %d/100                                Yanlis = %d/100                                Bos = %d/100                                NET = %.2f                                %c %.2f"%(int(Dogru),int(Yanlis),int(Bos),net,'%',yuz))

    if yuz < 49:
        fullscore['bg']="red"
    if yuz > 49:
        fullscore['bg']="orange"
    if yuz > 74:
        fullscore['bg']="light green"


    fullscore['text']=("Dogru = %d/100                                \n                                NET = %.2f/100\nYanlis = %d/100                                \n                                %c %.2f\nBos = %d/100                                "%(int(Dogru),net,int(Yanlis),'%',yuz,int(Bos)))
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


fullscore = Label(third_frame,text="Dogru = /100                                \n                                NET = /100\nYanlis = /100                                \n                                % \nBos = /100                                ",fg='white',bg="black",font=("Roboto",25))
fullscore.place(x=0,y=0)


tr1 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr1.place(x=150,y=20)
tr2 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr2.place(x=150,y=70)
tr3 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr3.place(x=150,y=120)
tr4 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr4.place(x=150,y=170)
tr5 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr5.place(x=150,y=220)
tr6 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr6.place(x=150,y=270)
tr7 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr7.place(x=150,y=320)
tr8 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr8.place(x=150,y=370)
tr9 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr9.place(x=150,y=420)
tr10 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr10.place(x=150,y=470)
tr11 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr11.place(x=150,y=520)
tr12 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr12.place(x=150,y=570)
tr13 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr13.place(x=150,y=620)
tr14 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr14.place(x=150,y=670)
tr15 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr15.place(x=150,y=720)
tr16 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr16.place(x=150,y=770)
tr17 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr17.place(x=150,y=820)
tr18 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr18.place(x=150,y=870)
tr19 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr19.place(x=150,y=920)
tr20 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr20.place(x=150,y=970)
tr21 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr21.place(x=150,y=1020)
tr22 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr22.place(x=150,y=1070)
tr23 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr23.place(x=150,y=1120)
tr24 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr24.place(x=150,y=1170)
tr25 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr25.place(x=150,y=1220)
tr26 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr26.place(x=150,y=1270)
tr27 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr27.place(x=150,y=1320)
tr28 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr28.place(x=150,y=1370)
tr29 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr29.place(x=150,y=1420)
tr30 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr30.place(x=150,y=1470)
tr31 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr31.place(x=150,y=1520)
tr32 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr32.place(x=150,y=1570)
tr33 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr33.place(x=150,y=1620)
tr34 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr34.place(x=150,y=1670)
tr35 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr35.place(x=150,y=1720)
tr36 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr36.place(x=150,y=1770)
tr37 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr37.place(x=150,y=1820)
tr38 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr38.place(x=150,y=1870)
tr39 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr39.place(x=150,y=1920)
tr40 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr40.place(x=150,y=1970)
tr41 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr41.place(x=150,y=2020)
tr42 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr42.place(x=150,y=2070)
tr43 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr43.place(x=150,y=2120)
tr44 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr44.place(x=150,y=2170)
tr45 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr45.place(x=150,y=2220)
tr46 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr46.place(x=150,y=2270)
tr47 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr47.place(x=150,y=2320)
tr48 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr48.place(x=150,y=2370)
tr49 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr49.place(x=150,y=2420)
tr50 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr50.place(x=150,y=2470)
tr51 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr51.place(x=150,y=2520)
tr52 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr52.place(x=150,y=2570)
tr53 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr53.place(x=150,y=2620)
tr54 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr54.place(x=150,y=2670)
tr55 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr55.place(x=150,y=2720)
tr56 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr56.place(x=150,y=2770)
tr57 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr57.place(x=150,y=2820)
tr58 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr58.place(x=150,y=2870)
tr59 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr59.place(x=150,y=2920)
tr60 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr60.place(x=150,y=2970)
tr61 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr61.place(x=150,y=3020)
tr62 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr62.place(x=150,y=3070)
tr63 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr63.place(x=150,y=3120)
tr64 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr64.place(x=150,y=3170)
tr65 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr65.place(x=150,y=3220)
tr66 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr66.place(x=150,y=3270)
tr67 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr67.place(x=150,y=3320)
tr68 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr68.place(x=150,y=3370)
tr69 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr69.place(x=150,y=3420)
tr70 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr70.place(x=150,y=3470)
tr71 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr71.place(x=150,y=3520)
tr72 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr72.place(x=150,y=3570)
tr73 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr73.place(x=150,y=3620)
tr74 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr74.place(x=150,y=3670)
tr75 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr75.place(x=150,y=3720)
tr76 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr76.place(x=150,y=3770)
tr77 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr77.place(x=150,y=3820)
tr78 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr78.place(x=150,y=3870)
tr79 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr79.place(x=150,y=3920)
tr80 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr80.place(x=150,y=3970)
tr81 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr81.place(x=150,y=4020)
tr82 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr82.place(x=150,y=4070)
tr83 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr83.place(x=150,y=4120)
tr84 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr84.place(x=150,y=4170)
tr85 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr85.place(x=150,y=4220)
tr86 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr86.place(x=150,y=4270)
tr87 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr87.place(x=150,y=4320)
tr88 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr88.place(x=150,y=4370)
tr89 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr89.place(x=150,y=4420)
tr90 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr90.place(x=150,y=4470)
tr91 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr91.place(x=150,y=4520)
tr92 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr92.place(x=150,y=4570)
tr93 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr93.place(x=150,y=4620)
tr94 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr94.place(x=150,y=4670)
tr95 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr95.place(x=150,y=4720)
tr96 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr96.place(x=150,y=4770)
tr97 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr97.place(x=150,y=4820)
tr98 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr98.place(x=150,y=4870)
tr99 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr99.place(x=150,y=4920)
tr100 = Label(second_frame,text="",fg='green',font=("Roboto",25))
tr100.place(x=150,y=4970)


Label(second_frame,text=1,font=("Roboto",25)).place(x=20,y=20)
s1=Entry(second_frame,width=2,font=('Arial 24'))
s1.place(x=100,y=20)
second_frame.configure(height=53)
Label(second_frame,text=2,font=("Roboto",25)).place(x=20,y=70)
s2=Entry(second_frame,width=2,font=('Arial 24'))
s2.place(x=100,y=70)
second_frame.configure(height=106)
Label(second_frame,text=3,font=("Roboto",25)).place(x=20,y=120)
s3=Entry(second_frame,width=2,font=('Arial 24'))
s3.place(x=100,y=120)
second_frame.configure(height=159)
Label(second_frame,text=4,font=("Roboto",25)).place(x=20,y=170)
s4=Entry(second_frame,width=2,font=('Arial 24'))
s4.place(x=100,y=170)
second_frame.configure(height=212)
Label(second_frame,text=5,font=("Roboto",25)).place(x=20,y=220)
s5=Entry(second_frame,width=2,font=('Arial 24'))
s5.place(x=100,y=220)
second_frame.configure(height=265)
Label(second_frame,text=6,font=("Roboto",25)).place(x=20,y=270)
s6=Entry(second_frame,width=2,font=('Arial 24'))
s6.place(x=100,y=270)
second_frame.configure(height=318)
Label(second_frame,text=7,font=("Roboto",25)).place(x=20,y=320)
s7=Entry(second_frame,width=2,font=('Arial 24'))
s7.place(x=100,y=320)
second_frame.configure(height=371)
Label(second_frame,text=8,font=("Roboto",25)).place(x=20,y=370)
s8=Entry(second_frame,width=2,font=('Arial 24'))
s8.place(x=100,y=370)
second_frame.configure(height=424)
Label(second_frame,text=9,font=("Roboto",25)).place(x=20,y=420)
s9=Entry(second_frame,width=2,font=('Arial 24'))
s9.place(x=100,y=420)
second_frame.configure(height=477)
Label(second_frame,text=10,font=("Roboto",25)).place(x=20,y=470)
s10=Entry(second_frame,width=2,font=('Arial 24'))
s10.place(x=100,y=470)
second_frame.configure(height=530)
Label(second_frame,text=11,font=("Roboto",25)).place(x=20,y=520)
s11=Entry(second_frame,width=2,font=('Arial 24'))
s11.place(x=100,y=520)
second_frame.configure(height=583)
Label(second_frame,text=12,font=("Roboto",25)).place(x=20,y=570)
s12=Entry(second_frame,width=2,font=('Arial 24'))
s12.place(x=100,y=570)
second_frame.configure(height=636)
Label(second_frame,text=13,font=("Roboto",25)).place(x=20,y=620)
s13=Entry(second_frame,width=2,font=('Arial 24'))
s13.place(x=100,y=620)
second_frame.configure(height=689)
Label(second_frame,text=14,font=("Roboto",25)).place(x=20,y=670)
s14=Entry(second_frame,width=2,font=('Arial 24'))
s14.place(x=100,y=670)
second_frame.configure(height=742)
Label(second_frame,text=15,font=("Roboto",25)).place(x=20,y=720)
s15=Entry(second_frame,width=2,font=('Arial 24'))
s15.place(x=100,y=720)
second_frame.configure(height=795)
Label(second_frame,text=16,font=("Roboto",25)).place(x=20,y=770)
s16=Entry(second_frame,width=2,font=('Arial 24'))
s16.place(x=100,y=770)
second_frame.configure(height=848)
Label(second_frame,text=17,font=("Roboto",25)).place(x=20,y=820)
s17=Entry(second_frame,width=2,font=('Arial 24'))
s17.place(x=100,y=820)
second_frame.configure(height=901)
Label(second_frame,text=18,font=("Roboto",25)).place(x=20,y=870)
s18=Entry(second_frame,width=2,font=('Arial 24'))
s18.place(x=100,y=870)
second_frame.configure(height=954)
Label(second_frame,text=19,font=("Roboto",25)).place(x=20,y=920)
s19=Entry(second_frame,width=2,font=('Arial 24'))
s19.place(x=100,y=920)
second_frame.configure(height=1007)
Label(second_frame,text=20,font=("Roboto",25)).place(x=20,y=970)
s20=Entry(second_frame,width=2,font=('Arial 24'))
s20.place(x=100,y=970)
second_frame.configure(height=1060)
Label(second_frame,text=21,font=("Roboto",25)).place(x=20,y=1020)
s21=Entry(second_frame,width=2,font=('Arial 24'))
s21.place(x=100,y=1020)
second_frame.configure(height=1113)
Label(second_frame,text=22,font=("Roboto",25)).place(x=20,y=1070)
s22=Entry(second_frame,width=2,font=('Arial 24'))
s22.place(x=100,y=1070)
second_frame.configure(height=1166)
Label(second_frame,text=23,font=("Roboto",25)).place(x=20,y=1120)
s23=Entry(second_frame,width=2,font=('Arial 24'))
s23.place(x=100,y=1120)
second_frame.configure(height=1219)
Label(second_frame,text=24,font=("Roboto",25)).place(x=20,y=1170)
s24=Entry(second_frame,width=2,font=('Arial 24'))
s24.place(x=100,y=1170)
second_frame.configure(height=1272)
Label(second_frame,text=25,font=("Roboto",25)).place(x=20,y=1220)
s25=Entry(second_frame,width=2,font=('Arial 24'))
s25.place(x=100,y=1220)
second_frame.configure(height=1325)
Label(second_frame,text=26,font=("Roboto",25)).place(x=20,y=1270)
s26=Entry(second_frame,width=2,font=('Arial 24'))
s26.place(x=100,y=1270)
second_frame.configure(height=1378)
Label(second_frame,text=27,font=("Roboto",25)).place(x=20,y=1320)
s27=Entry(second_frame,width=2,font=('Arial 24'))
s27.place(x=100,y=1320)
second_frame.configure(height=1431)
Label(second_frame,text=28,font=("Roboto",25)).place(x=20,y=1370)
s28=Entry(second_frame,width=2,font=('Arial 24'))
s28.place(x=100,y=1370)
second_frame.configure(height=1484)
Label(second_frame,text=29,font=("Roboto",25)).place(x=20,y=1420)
s29=Entry(second_frame,width=2,font=('Arial 24'))
s29.place(x=100,y=1420)
second_frame.configure(height=1537)
Label(second_frame,text=30,font=("Roboto",25)).place(x=20,y=1470)
s30=Entry(second_frame,width=2,font=('Arial 24'))
s30.place(x=100,y=1470)
second_frame.configure(height=1590)
Label(second_frame,text=31,font=("Roboto",25)).place(x=20,y=1520)
s31=Entry(second_frame,width=2,font=('Arial 24'))
s31.place(x=100,y=1520)
second_frame.configure(height=1643)
Label(second_frame,text=32,font=("Roboto",25)).place(x=20,y=1570)
s32=Entry(second_frame,width=2,font=('Arial 24'))
s32.place(x=100,y=1570)
second_frame.configure(height=1696)
Label(second_frame,text=33,font=("Roboto",25)).place(x=20,y=1620)
s33=Entry(second_frame,width=2,font=('Arial 24'))
s33.place(x=100,y=1620)
second_frame.configure(height=1749)
Label(second_frame,text=34,font=("Roboto",25)).place(x=20,y=1670)
s34=Entry(second_frame,width=2,font=('Arial 24'))
s34.place(x=100,y=1670)
second_frame.configure(height=1802)
Label(second_frame,text=35,font=("Roboto",25)).place(x=20,y=1720)
s35=Entry(second_frame,width=2,font=('Arial 24'))
s35.place(x=100,y=1720)
second_frame.configure(height=1855)
Label(second_frame,text=36,font=("Roboto",25)).place(x=20,y=1770)
s36=Entry(second_frame,width=2,font=('Arial 24'))
s36.place(x=100,y=1770)
second_frame.configure(height=1908)
Label(second_frame,text=37,font=("Roboto",25)).place(x=20,y=1820)
s37=Entry(second_frame,width=2,font=('Arial 24'))
s37.place(x=100,y=1820)
second_frame.configure(height=1961)
Label(second_frame,text=38,font=("Roboto",25)).place(x=20,y=1870)
s38=Entry(second_frame,width=2,font=('Arial 24'))
s38.place(x=100,y=1870)
second_frame.configure(height=2014)
Label(second_frame,text=39,font=("Roboto",25)).place(x=20,y=1920)
s39=Entry(second_frame,width=2,font=('Arial 24'))
s39.place(x=100,y=1920)
second_frame.configure(height=2067)
Label(second_frame,text=40,font=("Roboto",25)).place(x=20,y=1970)
s40=Entry(second_frame,width=2,font=('Arial 24'))
s40.place(x=100,y=1970)
second_frame.configure(height=2120)
Label(second_frame,text=41,font=("Roboto",25)).place(x=20,y=2020)
s41=Entry(second_frame,width=2,font=('Arial 24'))
s41.place(x=100,y=2020)
second_frame.configure(height=2173)
Label(second_frame,text=42,font=("Roboto",25)).place(x=20,y=2070)
s42=Entry(second_frame,width=2,font=('Arial 24'))
s42.place(x=100,y=2070)
second_frame.configure(height=2226)
Label(second_frame,text=43,font=("Roboto",25)).place(x=20,y=2120)
s43=Entry(second_frame,width=2,font=('Arial 24'))
s43.place(x=100,y=2120)
second_frame.configure(height=2279)
Label(second_frame,text=44,font=("Roboto",25)).place(x=20,y=2170)
s44=Entry(second_frame,width=2,font=('Arial 24'))
s44.place(x=100,y=2170)
second_frame.configure(height=2332)
Label(second_frame,text=45,font=("Roboto",25)).place(x=20,y=2220)
s45=Entry(second_frame,width=2,font=('Arial 24'))
s45.place(x=100,y=2220)
second_frame.configure(height=2385)
Label(second_frame,text=46,font=("Roboto",25)).place(x=20,y=2270)
s46=Entry(second_frame,width=2,font=('Arial 24'))
s46.place(x=100,y=2270)
second_frame.configure(height=2438)
Label(second_frame,text=47,font=("Roboto",25)).place(x=20,y=2320)
s47=Entry(second_frame,width=2,font=('Arial 24'))
s47.place(x=100,y=2320)
second_frame.configure(height=2491)
Label(second_frame,text=48,font=("Roboto",25)).place(x=20,y=2370)
s48=Entry(second_frame,width=2,font=('Arial 24'))
s48.place(x=100,y=2370)
second_frame.configure(height=2544)
Label(second_frame,text=49,font=("Roboto",25)).place(x=20,y=2420)
s49=Entry(second_frame,width=2,font=('Arial 24'))
s49.place(x=100,y=2420)
second_frame.configure(height=2597)
Label(second_frame,text=50,font=("Roboto",25)).place(x=20,y=2470)
s50=Entry(second_frame,width=2,font=('Arial 24'))
s50.place(x=100,y=2470)
second_frame.configure(height=2650)
Label(second_frame,text=51,font=("Roboto",25)).place(x=20,y=2520)
s51=Entry(second_frame,width=2,font=('Arial 24'))
s51.place(x=100,y=2520)
second_frame.configure(height=2703)
Label(second_frame,text=52,font=("Roboto",25)).place(x=20,y=2570)
s52=Entry(second_frame,width=2,font=('Arial 24'))
s52.place(x=100,y=2570)
second_frame.configure(height=2756)
Label(second_frame,text=53,font=("Roboto",25)).place(x=20,y=2620)
s53=Entry(second_frame,width=2,font=('Arial 24'))
s53.place(x=100,y=2620)
second_frame.configure(height=2809)
Label(second_frame,text=54,font=("Roboto",25)).place(x=20,y=2670)
s54=Entry(second_frame,width=2,font=('Arial 24'))
s54.place(x=100,y=2670)
second_frame.configure(height=2862)
Label(second_frame,text=55,font=("Roboto",25)).place(x=20,y=2720)
s55=Entry(second_frame,width=2,font=('Arial 24'))
s55.place(x=100,y=2720)
second_frame.configure(height=2915)
Label(second_frame,text=56,font=("Roboto",25)).place(x=20,y=2770)
s56=Entry(second_frame,width=2,font=('Arial 24'))
s56.place(x=100,y=2770)
second_frame.configure(height=2968)
Label(second_frame,text=57,font=("Roboto",25)).place(x=20,y=2820)
s57=Entry(second_frame,width=2,font=('Arial 24'))
s57.place(x=100,y=2820)
second_frame.configure(height=3021)
Label(second_frame,text=58,font=("Roboto",25)).place(x=20,y=2870)
s58=Entry(second_frame,width=2,font=('Arial 24'))
s58.place(x=100,y=2870)
second_frame.configure(height=3074)
Label(second_frame,text=59,font=("Roboto",25)).place(x=20,y=2920)
s59=Entry(second_frame,width=2,font=('Arial 24'))
s59.place(x=100,y=2920)
second_frame.configure(height=3127)
Label(second_frame,text=60,font=("Roboto",25)).place(x=20,y=2970)
s60=Entry(second_frame,width=2,font=('Arial 24'))
s60.place(x=100,y=2970)
second_frame.configure(height=3180)
Label(second_frame,text=61,font=("Roboto",25)).place(x=20,y=3020)
s61=Entry(second_frame,width=2,font=('Arial 24'))
s61.place(x=100,y=3020)
second_frame.configure(height=3233)
Label(second_frame,text=62,font=("Roboto",25)).place(x=20,y=3070)
s62=Entry(second_frame,width=2,font=('Arial 24'))
s62.place(x=100,y=3070)
second_frame.configure(height=3286)
Label(second_frame,text=63,font=("Roboto",25)).place(x=20,y=3120)
s63=Entry(second_frame,width=2,font=('Arial 24'))
s63.place(x=100,y=3120)
second_frame.configure(height=3339)
Label(second_frame,text=64,font=("Roboto",25)).place(x=20,y=3170)
s64=Entry(second_frame,width=2,font=('Arial 24'))
s64.place(x=100,y=3170)
second_frame.configure(height=3392)
Label(second_frame,text=65,font=("Roboto",25)).place(x=20,y=3220)
s65=Entry(second_frame,width=2,font=('Arial 24'))
s65.place(x=100,y=3220)
second_frame.configure(height=3445)
Label(second_frame,text=66,font=("Roboto",25)).place(x=20,y=3270)
s66=Entry(second_frame,width=2,font=('Arial 24'))
s66.place(x=100,y=3270)
second_frame.configure(height=3498)
Label(second_frame,text=67,font=("Roboto",25)).place(x=20,y=3320)
s67=Entry(second_frame,width=2,font=('Arial 24'))
s67.place(x=100,y=3320)
second_frame.configure(height=3551)
Label(second_frame,text=68,font=("Roboto",25)).place(x=20,y=3370)
s68=Entry(second_frame,width=2,font=('Arial 24'))
s68.place(x=100,y=3370)
second_frame.configure(height=3604)
Label(second_frame,text=69,font=("Roboto",25)).place(x=20,y=3420)
s69=Entry(second_frame,width=2,font=('Arial 24'))
s69.place(x=100,y=3420)
second_frame.configure(height=3657)
Label(second_frame,text=70,font=("Roboto",25)).place(x=20,y=3470)
s70=Entry(second_frame,width=2,font=('Arial 24'))
s70.place(x=100,y=3470)
second_frame.configure(height=3710)
Label(second_frame,text=71,font=("Roboto",25)).place(x=20,y=3520)
s71=Entry(second_frame,width=2,font=('Arial 24'))
s71.place(x=100,y=3520)
second_frame.configure(height=3763)
Label(second_frame,text=72,font=("Roboto",25)).place(x=20,y=3570)
s72=Entry(second_frame,width=2,font=('Arial 24'))
s72.place(x=100,y=3570)
second_frame.configure(height=3816)
Label(second_frame,text=73,font=("Roboto",25)).place(x=20,y=3620)
s73=Entry(second_frame,width=2,font=('Arial 24'))
s73.place(x=100,y=3620)
second_frame.configure(height=3869)
Label(second_frame,text=74,font=("Roboto",25)).place(x=20,y=3670)
s74=Entry(second_frame,width=2,font=('Arial 24'))
s74.place(x=100,y=3670)
second_frame.configure(height=3922)
Label(second_frame,text=75,font=("Roboto",25)).place(x=20,y=3720)
s75=Entry(second_frame,width=2,font=('Arial 24'))
s75.place(x=100,y=3720)
second_frame.configure(height=3975)
Label(second_frame,text=76,font=("Roboto",25)).place(x=20,y=3770)
s76=Entry(second_frame,width=2,font=('Arial 24'))
s76.place(x=100,y=3770)
second_frame.configure(height=4028)
Label(second_frame,text=77,font=("Roboto",25)).place(x=20,y=3820)
s77=Entry(second_frame,width=2,font=('Arial 24'))
s77.place(x=100,y=3820)
second_frame.configure(height=4081)
Label(second_frame,text=78,font=("Roboto",25)).place(x=20,y=3870)
s78=Entry(second_frame,width=2,font=('Arial 24'))
s78.place(x=100,y=3870)
second_frame.configure(height=4134)
Label(second_frame,text=79,font=("Roboto",25)).place(x=20,y=3920)
s79=Entry(second_frame,width=2,font=('Arial 24'))
s79.place(x=100,y=3920)
second_frame.configure(height=4187)
Label(second_frame,text=80,font=("Roboto",25)).place(x=20,y=3970)
s80=Entry(second_frame,width=2,font=('Arial 24'))
s80.place(x=100,y=3970)
second_frame.configure(height=4240)
Label(second_frame,text=81,font=("Roboto",25)).place(x=20,y=4020)
s81=Entry(second_frame,width=2,font=('Arial 24'))
s81.place(x=100,y=4020)
second_frame.configure(height=4293)
Label(second_frame,text=82,font=("Roboto",25)).place(x=20,y=4070)
s82=Entry(second_frame,width=2,font=('Arial 24'))
s82.place(x=100,y=4070)
second_frame.configure(height=4346)
Label(second_frame,text=83,font=("Roboto",25)).place(x=20,y=4120)
s83=Entry(second_frame,width=2,font=('Arial 24'))
s83.place(x=100,y=4120)
second_frame.configure(height=4399)
Label(second_frame,text=84,font=("Roboto",25)).place(x=20,y=4170)
s84=Entry(second_frame,width=2,font=('Arial 24'))
s84.place(x=100,y=4170)
second_frame.configure(height=4452)
Label(second_frame,text=85,font=("Roboto",25)).place(x=20,y=4220)
s85=Entry(second_frame,width=2,font=('Arial 24'))
s85.place(x=100,y=4220)
second_frame.configure(height=4505)
Label(second_frame,text=86,font=("Roboto",25)).place(x=20,y=4270)
s86=Entry(second_frame,width=2,font=('Arial 24'))
s86.place(x=100,y=4270)
second_frame.configure(height=4558)
Label(second_frame,text=87,font=("Roboto",25)).place(x=20,y=4320)
s87=Entry(second_frame,width=2,font=('Arial 24'))
s87.place(x=100,y=4320)
second_frame.configure(height=4611)
Label(second_frame,text=88,font=("Roboto",25)).place(x=20,y=4370)
s88=Entry(second_frame,width=2,font=('Arial 24'))
s88.place(x=100,y=4370)
second_frame.configure(height=4664)
Label(second_frame,text=89,font=("Roboto",25)).place(x=20,y=4420)
s89=Entry(second_frame,width=2,font=('Arial 24'))
s89.place(x=100,y=4420)
second_frame.configure(height=4717)
Label(second_frame,text=90,font=("Roboto",25)).place(x=20,y=4470)
s90=Entry(second_frame,width=2,font=('Arial 24'))
s90.place(x=100,y=4470)
second_frame.configure(height=4770)
Label(second_frame,text=91,font=("Roboto",25)).place(x=20,y=4520)
s91=Entry(second_frame,width=2,font=('Arial 24'))
s91.place(x=100,y=4520)
second_frame.configure(height=4823)
Label(second_frame,text=92,font=("Roboto",25)).place(x=20,y=4570)
s92=Entry(second_frame,width=2,font=('Arial 24'))
s92.place(x=100,y=4570)
second_frame.configure(height=4876)
Label(second_frame,text=93,font=("Roboto",25)).place(x=20,y=4620)
s93=Entry(second_frame,width=2,font=('Arial 24'))
s93.place(x=100,y=4620)
second_frame.configure(height=4929)
Label(second_frame,text=94,font=("Roboto",25)).place(x=20,y=4670)
s94=Entry(second_frame,width=2,font=('Arial 24'))
s94.place(x=100,y=4670)
second_frame.configure(height=4982)
Label(second_frame,text=95,font=("Roboto",25)).place(x=20,y=4720)
s95=Entry(second_frame,width=2,font=('Arial 24'))
s95.place(x=100,y=4720)
second_frame.configure(height=5035)
Label(second_frame,text=96,font=("Roboto",25)).place(x=20,y=4770)
s96=Entry(second_frame,width=2,font=('Arial 24'))
s96.place(x=100,y=4770)
second_frame.configure(height=5088)
Label(second_frame,text=97,font=("Roboto",25)).place(x=20,y=4820)
s97=Entry(second_frame,width=2,font=('Arial 24'))
s97.place(x=100,y=4820)
second_frame.configure(height=5141)
Label(second_frame,text=98,font=("Roboto",25)).place(x=20,y=4870)
s98=Entry(second_frame,width=2,font=('Arial 24'))
s98.place(x=100,y=4870)
second_frame.configure(height=5194)
Label(second_frame,text=99,font=("Roboto",25)).place(x=20,y=4920)
s99=Entry(second_frame,width=2,font=('Arial 24'))
s99.place(x=100,y=4920)
second_frame.configure(height=5247)
Label(second_frame,text=100,font=("Roboto",25)).place(x=20,y=4970)
s100=Entry(second_frame,width=2,font=('Arial 24'))
s100.place(x=100,y=4970)
second_frame.configure(height=5300)

second_frame.configure(height=5120.0)


root.mainloop()