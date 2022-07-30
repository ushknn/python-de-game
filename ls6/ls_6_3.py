import tkinter

def click_btn():
  button["text"] = "Clicked!!"

root = tkinter.Tk()
root.title("first button")
root.geometry("800x600")
button = tkinter.Button(root, text="Please Click!!", font=("Times New Roman", 24), command=click_btn)
button.place(x=200, y=100)
root.mainloop()
