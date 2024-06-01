# User Management System

## Overview

This project is a User Management System built with Flask, a Python web framework. It allows users to perform CRUD (Create, Read, Update, Delete) operations on user data. The application interacts with a MySQL database to store and manage user information.

## Features

- **Add User**: Form to add new users.
- **Edit User**: Form to update existing user details.
- **Delete User**: Option to delete a user.
- **List Users**: Display a list of all users.

## Files

- `app.py`: The main application file that sets up the Flask app and routes.
- `templates/add_user.html`: HTML form to add a new user.
- `templates/edit_user.html`: HTML form to edit an existing user.
- `templates/list_users.html`: HTML page that lists all users with options to edit or delete each user.
- `templates/index.html`: Home page of the application with navigation to other pages.

## Setup

### Prerequisites

- Python 3.x
- Flask
- MySQL

### Installation

1. **Clone the repository:**
    ```bash
    git clone <https://github.com/Mohanraj2622/Data-Collection-and-Manipulation.git>
    cd user-management-system
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Setup MySQL Database:**

    Create a new database in MySQL:
    ```sql
    CREATE DATABASE user_management;
    ```

    Update the database configuration in `app.py`:
    ```python
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your-username'
    app.config['MYSQL_PASSWORD'] = 'your-password'
    app.config['MYSQL_DB'] = 'user_management'
    ```

5. **Run the application:**
    ```bash
    flask run
    ```

6. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

- **Home Page:** Displays welcome message and navigation menu.
- **Add User Page:** Fill out the form to add a new user.
- **Edit User Page:** Modify user details using the form.
- **List Users Page:** View all users and perform actions such as edit and delete.

## File Details

### `app.py`
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your-username'
app.config['MYSQL_PASSWORD'] = 'your-password'
app.config['MYSQL_DB'] = 'user_management'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)', (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('list_users'))
    return render_template('add_user.html')

@app.route('/edit_user/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor.execute('UPDATE users SET name=%s, email=%s, phone=%s WHERE id=%s', (name, email, phone, id))
        mysql.connection.commit()
        return redirect(url_for('list_users'))
    cursor.execute('SELECT * FROM users WHERE id=%s', (id,))
    user = cursor.fetchone()
    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:id>')
def delete_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM users WHERE id=%s', (id,))
    mysql.connection.commit()
    return redirect(url_for('list_users'))

@app.route('/list_users')
def list_users():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return render_template('list_users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
```

This README file provides an overview of the project, setup instructions, and usage details. Adjust the database configuration and repository URL as necessary.
