import pyodbc

class connection:
    def __init__(self):
        self.conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-88EQMC0\\SQLEXPRESS;'
        'DATABASE=ToDo;'
        'Trusted_Connection=yes;'
    )
    
        self.cursor = self.conn.cursor()
    

