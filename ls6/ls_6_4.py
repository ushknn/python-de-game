import tkinter
root = tkinter.Tk()
root.title("first Image")
canvas = tkinter.Canvas(root, width=400, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="py_samples/Chapter6/iroha.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()
