import tkinter

def check():
	if cval.get() == True:
		print("Checked!!")
	else:
		print("Not Checked!!")		

root = tkinter.Tk()
root.title("最初からチェックされてる")
root.geometry("400x200")
cval = tkinter.BooleanVar()
cval.set(True)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval, command=check)
cbtn.pack()
root.mainloop()
