from flask import Flask, redirect, url_for
from controllers.usersController import users_blueprint
from controllers.tasksController import tasks_blueprint

app = Flask(__name__)
app.secret_key = 'ahsan22'
app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)
# @app.route('/')   
# def my():
#     return "To Do App"

@app.route('/')
def register():
    return redirect(url_for('users.registration'))
    

if __name__ == "__main__":
    app.run(debug=True)

