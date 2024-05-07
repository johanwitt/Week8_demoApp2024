import pyodbc
import tkinter as tk

# this is branch 1
# Backend pyodbc starts here

def show_entries():
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ongchangcoj\Downloads\Wk8_demoDB.accdb')

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Personal_details')

    for row in cursor.fetchall():
        print (row)
        
def add_entries():
    ID = e1.get()
    Fname = e2.get()
    Lname = e3.get()
    Email = e4.get()
    
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ongchangcoj\Downloads\Wk8_demoDB.accdb')

    cursor = conn.cursor()

    cursor.execute('INSERT INTO Personal_details VALUES (?,?,?,?)', (ID, Fname, Lname, Email)) 
    conn.commit()

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

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

# button group

tk.Button(master, text='Show', command=show_entries).grid(row=7, column =0)
tk.Button(master, text='Submit', command=add_entries).grid(row=7, column =1)

tk.mainloop()