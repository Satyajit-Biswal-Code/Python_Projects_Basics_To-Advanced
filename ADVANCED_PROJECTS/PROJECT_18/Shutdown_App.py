import tkinter as tk
import os
from cms.toolbar.items import Button
from pycparser.ply.yacc import restart


def restart():
    os.system("shutdown /r /t 1")
def Shutdown():
    os.system("shutdown /s /t 1")
def Logout():
    os.system("shutdown -l")

root=tk.Tk()
root.geometry("500x500")
root.config(background="blue")
root.title("os shutdown")

btn=tk.Button(root,text="Restart",command=restart)
btn.config(font=("verdana",10))
btn.pack(pady=30)

btn1=tk.Button(root,text="Shutdown",command=Shutdown)
btn1.config(font=("verdana",10))
btn1.pack(pady=30)

btn2=tk.Button(root,text="Logout",command=Logout)
btn2.config(font=("verdana",10))
btn2.pack(pady=30)

root.mainloop()