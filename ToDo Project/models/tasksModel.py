from db import connection


class tasks_Class:
    def __init__(self, taskName, username, userId):
        self.taskName = taskName
        self.username = username
        self.userId = userId
        
    @classmethod
    def view_cons(cls,username, userId):
        return cls(None,username,userId)
    
   
    @classmethod
    def get_by_id(cls, taskId, userId):
        try:
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("select taskName from tbltasks where id=? and usersid=?", (taskId, userId))
            row = cursor.fetchone()
            db.conn.close()

            if row:
                return {'id': taskId, 'taskName': row[0]}
            else:
                return None
        except Exception as e:
            return str(e)

    
    def edit(self,taskId):
        try:
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute(
                "update tbltasks set taskName=? where id=? and usersid=?",
                (self.taskName, taskId, self.userId)
            )
            db.conn.commit()
            db.conn.close()

            if cursor.rowcount == 0:
                return False # No rows updated
            return True
        except Exception as e:
            return str(e)

    def add(self):
        try: 
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("insert into tbltasks (taskName,usersid) values(?,?)",(self.taskName,self.userId))
            db.conn.commit()
            db.conn.close()
            return True
        except Exception as e:
            return str(e)
        

    def view(self):
        try: 
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("select id,taskName from tbltasks where usersid=?",(self.userId,))
            data = cursor.fetchall()
            db.conn.close()
            return [{'id': row[0], 'name': row[1]} for row in data]
        except Exception as e:
            return str(e)
        
    def delete(self,taskId):
        try: 
            db = connection()
            cursor = db.conn.cursor()
            cursor.execute("delete from tbltasks where id=? and usersid=?",(taskId,self.userId))
            affected = cursor.rowcount
            db.conn.commit()
            db.conn.close()
            if affected == 0:
                return f"No task deleted (wrong ID or not your task)."
            return True
        except Exception as e:
            return str(e)
        
  