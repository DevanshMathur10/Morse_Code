from tkinter import *

root=Tk()
root.title("MORSE ENCODER")
root.geometry("1000x800")
root.state('zoomed')
codes={ 
                    'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':''}

bg=PhotoImage(file="C:/Users/dr_de/Documents/VS/TKINTER/bavk.png")
imglbl=Label(root,image=bg)
imglbl.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(root)
frame.place(x=760,y=390,anchor='center')
frame.configure(background='black')
def encrypt():
    message=str(Entry1.get()).upper()
    cipher=""
    for letter in message:
        if letter !=" ":
            cipher+=codes[letter]+" "
        else:
            cipher+=" "
    ciplbl=Text(frame,height=2,width=30,font=("arial",30),bg='black',fg='white')
    ciplbl.insert(INSERT,cipher)
    ciplbl.grid(row=3,column=0,sticky=W+E)
    ciplbl.configure(state='disabled')

def decrypt():
    message=str(Entry1.get())
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(codes.keys())[list(codes.values()).index(citext)]
                citext = ''
    deciplbl=Text(frame,height=2,width=30,font=("arial",30),bg='black',fg='white')
    deciplbl.insert(INSERT,decipher)
    deciplbl.grid(row=3,column=0,sticky=W+E)
    deciplbl.configure(state='disabled')

Entry1=Entry(frame,bg='black',fg='white')
Entry1.grid(row=0,column=0)

btn=Button(frame,text="ENCRYPT",command=encrypt,bg='black',fg='white')
btn.grid(row=1,column=0)
btn=Button(frame,text="DECRYPT",command=decrypt,bg='black',fg='white')
btn.grid(row=2,column=0)

root.mainloop()
