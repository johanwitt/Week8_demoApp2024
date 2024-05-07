import pyodbc
import tkinter as tk

from Backend import backend

# this is branch 1
# moved all the backend to Backend.py



# Frontend tkinter starts here

master = tk.Tk()



# labels for textboxes
tk.Label(master, text="ID").grid(row=0)
tk.Label(master, text="F Name").grid(row=1)
tk.Label(master, text="L Name").grid(row=2)
tk.Label(master, text="Email").grid(row=3)

# textboxes
e1=tk.Entry(master)
e2=tk.Entry(master)
e3=tk.Entry(master)
e4=tk.Entry(master)

# get textbox data
ID = e1.get()
Fname = e2.get()
Lname = e3.get()
Email = e4.get()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

# button group

tk.Button(master, text='Show', command=backend.show_entries).grid(row=7, column =0)
tk.Button(master, text='Submit', command=backend.add_entries(ID, Fname, Lname, Email)).grid(row=7, column =1)

tk.mainloop()