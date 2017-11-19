from tkinter import *
import dictApp

window = Tk()

def Define():
	list1.delete(0,END)
	output = dictApp.translate(e1.get())
	if(type(output)==list):
		for items in output:
			list1.insert(END, items)
	else:
		list1.insert(END, output)

window.wm_title("Dictionary")

label = Label(window, text="Word")
label.grid(row=0, column=5)

word = StringVar()
e1 = Entry(window, textvariable = word)
e1.grid(row=1, column=5)

b1=Button(window, text="Define", width=20, command=Define)
b1.grid(row=2, column=5)

list1=Listbox(window, height=5, width=100)
list1.grid(row=6, column=0, columnspan=10)

window.mainloop()