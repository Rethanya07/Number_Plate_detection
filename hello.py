import tkinter as tk
root =tk.Tk()
root.geometry("500x500")
root.title("My First GUI")
label= tk.Label(root,text="Hello world!",font=('Arial',18))
label.pack()
root.mainloop()