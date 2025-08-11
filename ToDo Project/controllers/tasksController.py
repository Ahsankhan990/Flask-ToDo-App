from flask import Flask, Blueprint, render_template, request, flash, session, redirect,url_for
from datetime import datetime
from models.tasksModel import tasks_Class

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == "add":
            taskName = request.form['task_name']
            
            username = session['username']
            userId = session['userId']
            addObj = tasks_Class(taskName, username, userId)
            result = addObj.add()
            if result:
                flash("Task Add Succussfully.", "success")
            else:
                flash("Task Not Added.","error")
                
       
        return redirect(url_for('tasks.tasks'))

    userId = session['userId']
    username = session['username']
    viewObj = tasks_Class.view_cons(username, userId)
    tasks = viewObj.view() 
    
    current_day = datetime.now().strftime('%A') 
    current_date = datetime.now().strftime('%d %B, %Y') 
    return render_template('tasks.html', current_day=current_day, current_date=current_date,tasks=tasks)

    
@tasks_blueprint.route('/delete/<int:taskId>', methods=['POST'])
def delete(taskId):
    userId = session['userId']
    username = session['username']
    deleteObj = tasks_Class.view_cons(username,userId)
    result = deleteObj.delete(taskId)

    if result is True:
        flash("Task deleted Succussfully.", "success")
    else:
        flash("Task Not deleted.","error")
            
    return redirect(url_for('tasks.tasks'))
                

    
@tasks_blueprint.route('/edit/<int:taskId>', methods=['GET', 'POST'])
def edit(taskId):
    
    userId = session.get('userId')  
    

    task_data = tasks_Class.get_by_id(taskId, userId)

    if not task_data:
        flash("Task not found or not your task.", "error")
        return redirect(url_for('tasks.tasks'))

    if request.method == 'POST':
        action = request.form.get('action')

        if action == "edit":
            taskName = request.form.get('task_name')

            editObj = tasks_Class(taskName,None,userId)
            result= editObj.edit(taskId)

            if result is True:
                flash("Task updated successfully.", "success")
                return redirect(url_for('tasks.tasks'))
            else:
                flash("Task not updated.", "error")

    return render_template("edit.html", task=task_data)
