import dictApp
from tkinter import *

window = Tk()

def final():
	print(e1_value)
	final = dictApp.translate(e1_value)
	t1.insert(END, final)

e1_value = StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)


t1=Text(window, height=1, width=20)
t1.grid(row=2, column=0)

b1=Button(window, text="Define", command=final)
b1.grid(row=0, column=2, rowspan=2)



window.mainloop()

