from db import connection
from controllers import usersController
from flask import Flask, flash
import re
class users:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def login_method(cls, email, password):
        return cls(None, email, password)
    
    
    def valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def register(self):
        try:
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("select email from tblusers where email=?",(self.email,))
            check_reg = cursor.fetchone()
            
            if check_reg:
                flash("Email Already exist")
            else:
                cursor.execute("insert into tblusers (username,email,password) values(?,?,?)",(self.username, self.email, self.password))
                db.conn.commit()
                db.conn.close()        
                return True
        
        except Exception as e:
            print(e)
            return False
        
        
    
    def login(self):
        try:
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("select id,username from tblusers where email=? and password=?",(self.email, self.password))
            fetchRow = cursor.fetchone()
            db.conn.close()
            
            if fetchRow:
                return {'id': fetchRow[0], 'username': fetchRow[1]}
            else:
                return False
        
        except Exception as e:
            print(e)
            return False
       
        