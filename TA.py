import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk as tema
import tkinter as tk
from tkinter.messagebox import showinfo

root = tb.Window(themename= 'minty')
nama = tk.StringVar()
kls = tk.StringVar()
al = tk.StringVar()
hr = tk.StringVar()
SIL = tk.StringVar()


def Sumbit():
    showinfo(title = 'Submit', message = 'Respond saved and sumbitted')

root.title("Form Izin")
root.geometry('400x600')
root.resizable(False, False)
root.config(bg='light blue')

frame = tema.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

labelNM = tema.Label(frame, text = 'Nama', font=('bold'))
labelNM.pack(padx= 1, fill='x', expand=True)
formNM = tema.Entry(frame, textvariable=nama)
formNM.pack(padx=20, fill='x', expand=True)

labelkls = tema.Label(frame, text='Kelas ', font=('bold'))
labelkls.pack(padx=1, pady = 2, fill='x', expand=True)
formkls = tema.Combobox(frame, textvariable= kls, value=('X.1', 'X.2', 'X.2', 'X.4', 'X.5', 'X.6', 'X.7', 'X.8', 'X.9', 'X.10', 'X.11', 'X.12', 'X.13', 'X.14'))
formkls.pack(padx=20, pady = 2, fill='x', expand=True)

labelAlasan = tema.Label(frame, text = 'Alasan tidak masuk : ', font=('bold'))
labelAlasan.pack(padx= 1, fill='x', expand=True)

SIL1 = tema.Radiobutton(frame, value='s', text= 'Sakit', variable=SIL)
SIL1.pack(padx=10, fill='x', expand=True)
SIL2 = tema.Radiobutton(frame, value='i', text= 'Izin', variable=SIL)
SIL2.pack(padx=10, fill='x', expand=True)
SIL3 = tema.Radiobutton(frame, value='l', text= 'Lainnya, tuliskan alasan:', variable=SIL)
SIL3.pack(padx=10, fill='x', expand=True)

formAlasan = tema.Entry(frame, textvariable=al)
formAlasan.pack(padx=40, fill='x', expand=True)

labelhr = tema.Label(frame, text='Lama izin : ')
labelhr.pack(padx=10, fill='x', expand=True)
hr1 = tema.Radiobutton(frame, value='1', text= '1 hari', variable=hr)
hr1.pack(padx=10, fill='x', expand=True)
hr2 = tema.Radiobutton(frame, value='2', text= '2 hari', variable=hr)
hr2.pack(padx=10, fill='x', expand=True)
hr3 = tema.Radiobutton(frame, value='3', text= '3 hari', variable=hr)
hr3.pack(padx=10, fill='x', expand=True)
hr4 = tema.Radiobutton(frame, value='4', text= '4 hari', variable=hr)
hr4.pack(padx=10, fill='x', expand=True)
hr5 = tema.Radiobutton(frame, value='5', text= '5 hari', variable=hr)
hr5.pack(padx=10, fill='x', expand=True)
hr6 = tema.Radiobutton(frame, value='6', text= '6 hari', variable=hr)
hr6.pack(padx=10, fill='x', expand=True)
hr7 = tema.Radiobutton(frame, value='7', text= '7 hari', variable=hr)
hr7.pack(padx=10, fill='x', expand=True)
hrl7 = tema.Radiobutton(frame, value='>7', text= 'Lebih dari 7 hari', variable=hr)
hrl7.pack(padx=10, fill='x', expand=True)

BTN = tema.Button(frame, text='Sumbit', command=Sumbit)
BTN.pack(padx=10, fill='x', expand=True)
root.mainloop()