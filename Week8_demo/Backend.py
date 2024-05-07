import pyodbc


class backend:
    def __init__(self, ID, Fname, Lname, Email):
        self.Id = ID
        self.fname = Fname
        self.lname = Lname
        self.email = Email
        
    def show_entries():
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ongchangcoj\Downloads\Wk8_demoDB.accdb')

        cursor = conn.cursor()

        cursor.execute('SELECT * FROM Personal_details')

        for row in cursor.fetchall():
            print (row)
        
    def add_entries(Id, fname, lname, email):
    
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ongchangcoj\Downloads\Wk8_demoDB.accdb')

        cursor = conn.cursor()

        cursor.execute('INSERT INTO Personal_details VALUES (?,?,?,?)', (Id, fname, lname, email)) 
        conn.commit()