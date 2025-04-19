import tkinter as tk
from tkinter import Label
from PIL import Image,ImageTk


root=tk.Tk()
img=Image.open("Images/srikrishna.jpg")
pic=ImageTk.PhotoImage(img)

labell=Label(root,image=pic)
labell.pack()
root.mainloop()