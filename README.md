# Flask-ToDo-App
A simple ToDo web application built with Python (Flask), SQL Server, Jinja2, HTML, and CSS.

## Features
- Add new tasks  
- Edit existing tasks  
- Delete tasks  
- Task list linked to logged-in user  
- Flash messages for success and error handling  
- Displays current date and day  

## Technologies and Concepts Used
- **Python 3** – Programming language  
- **Flask** – Backend web framework  
- **SQL Server** – Database  
- **HTML, CSS, Jinja2** – Frontend and templating  
- **pyodbc** – Database connectivity  
- **Object-Oriented Programming (OOP)** – For model structure  
- **Modular Structure** – Separate files for routes, models, and database connection  
- **Form Validation** – For task input  

## How to Run
1. Clone or download the repository  
2. Open `db.py` and update your SQL Server connection string  
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
4. Run the application:
   python app.py
5. Open your browser and go to:
    http://127.0.0.1:5000
