# -*- coding: big5 -*-
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import sys
#import wx,string
import tkinter as tk
sys.path.append('src')
#from Tkinter import *
#import Tkinter as tk
import inception

pad_x = 180

window = tk.Tk()

window.title('Hsin\'s Music Composer')

window.geometry('550x330')

window.configure(background='black')

var = tk.StringVar()
mode = tk.IntVar()


OptionList = [
"C",
"Db",
"D",
"Eb",
"E",
"F",
"Gb",
"G",
"Ab",
"A",
"Bb",
"B"
] 

variable = tk.StringVar()
variable.set(OptionList[0])

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=3, font=('Helvetica', 12))
opt.place(x=410, y=60)


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='gray', bg='black')
labelTest.place(x=375, y=35)

key_offset = 0

def key_sel(*args):
    global key_offset 
    key = variable.get()
    if key == "Db":
        key_offset = 1
    elif key == "D":
        key_offset = 2
    elif key == "Eb":
        key_offset = 3    
    elif key == "E":
        key_offset = 4
    elif key == "F":
        key_offset = 5
    elif key == "Gb":
        key_offset = 6
    elif key == "G":
        key_offset = 7
    elif key == "Ab":
        key_offset = -4
    elif key == "A":
        key_offset = -3
    elif key == "Bb":
        key_offset = -2
    elif key == "B":
        key_offset = -1
    else:
        key_offset = 0
    labelTest.configure(text="The selected key is {} key".format(variable.get()))
    
labelTest.configure(text="The selected key is {} key".format(variable.get()))        
variable.trace("w", key_sel)


l = tk.Label(window, fg='snow', bg='black', width=40, text='Please select music style and key')
l.pack()


def print_selection():
    l.config(text='Press Start to compose')

start_hit = False
#num = 0
#mode = 0





def start():
    global start_hit
    #global num
    if start_hit == False:
       start_hit = True
       l.config(text= 'Composing started!')
       inception.inception(mode.get(), 0, key_offset)
       l.config(text= 'Composing finished!')
       start_hit = False
    #num = num + 1
    else:
       start_hit = False
       var.set('')

r1 = tk.Radiobutton(window, fg='gray' , bg='black',text='Pop Ballad', variable=mode, value=0, command=print_selection)
r1.pack(padx = pad_x, anchor = 'w')

#r2 = tk.Radiobutton(window, fg='gray' , bg='black',text='Hsin\'s Minor', variable=mode, value=1, command=print_selection)
#r2.pack(padx = pad_x, anchor = 'w')

r3 = tk.Radiobutton(window, fg='gray' , bg='black',text='Pop Minor Tunes', variable=mode, value=2, command=print_selection)
r3.pack(padx = pad_x, anchor = 'w')

r4 = tk.Radiobutton(window, fg='gray' , bg='black',text='Bossa Nova', variable=mode, value=3, command=print_selection)
r4.pack(padx = pad_x, anchor = 'w')

r5 = tk.Radiobutton(window,  fg='gray' , bg='black', text='Blue Note', variable=mode, value=4, command=print_selection)
r5.pack(padx = pad_x, anchor = 'w')

r6 = tk.Radiobutton(window,  fg='gray' , bg='black', text='Major Pentatonic', variable=mode, value=5, command=print_selection)
r6.pack(padx = pad_x, anchor = 'w')

r7 = tk.Radiobutton(window,  fg='gray' , bg='black', text='Minor Pentatonic', variable=mode, value=6, command=print_selection)
r7.pack(padx = pad_x, anchor = 'w')
#font=('Arial', 12)
b = tk.Button(window, text='Start', width=10, height=1, command=start)
b.pack(padx=20, pady=10)

img_gif = tk.PhotoImage(file = 'cover_ss-2.gif')
label_img = tk.Label(window, image = img_gif, compound = tk.CENTER)
label_img.pack()


## emotion mapping
emotion = tk.IntVar()
labelEmotion = tk.Label(text="Emotion Mapping", font=('Helvetica', 12), fg='snow', bg='black')
labelEmotion.place(x=375, y=95)
e1 = tk.Radiobutton(window, fg='gray' , bg='black',text='Joy', variable=emotion, value=0, command=print_selection)
e1.place(x=375, y=115)
e2 = tk.Radiobutton(window, fg='gray' , bg='black',text='Anger', variable=emotion, value=1, command=print_selection)
e2.place(x=375, y=138)
#e2.pack(padx=375, anchor = 'w')
e3 = tk.Radiobutton(window, fg='gray' , bg='black',text='Sadness', variable=emotion, value=2, command=print_selection)
e3.place(x=375, y=161)
e1 = tk.Radiobutton(window, fg='gray' , bg='black',text='Happiness', variable=emotion, value=3, command=print_selection)
e1.place(x=375, y=184)

window.mainloop()



