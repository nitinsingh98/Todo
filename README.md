# Todo App
==========================

## Introduction
---
This repository was submitted as the final project for CS50X 2025 online course offered by Harvard University. It’s a web application built around Flask’s framework and some software development/web programming languages covered by the course, such as Python, SQL, HTML, and CSS. The application is designed for storing reminders.

## Description
---------------

A simple and intuitive Todo application built with Flask, a micro web framework for Python.
The central component of the application is task management, where the user can upload, store, and delete their reminders from the app. To enable these interactions, the main application is supported by additional files that contain utilities and security functions.

## Features
------------

* Create, read, update, and delete (CRUD) tasks.

## Getting Started
---------------

* First, you will be required to log in using your email address and password.
![Reference image](/static/todo_images/please_log_in.png) 

* If you don't have an account, click on the Sign Up option in the navigation to open the registration page, where you will need to submit your email, first name, and password.
![Reference image](/static/todo_images/sign_up.png)

* After submitting your details (if they are valid), you will be automatically logged in and redirected to the homepage, where you can enter the tasks you want to be reminded of.
![Reference image](/static/todo_images/after_login.png)

* Here, you can create tasks by submitting a title and description, update and delete tasks, mark tasks as complete, and view old tasks along with their creation dates.

After entering the title and description, click the submit button.
![Reference image](/static/todo_images/entering_tasks.png)

After submitting, your task will be added to your reminder list, and it will be marked as incomplete.
![Reference image](/static/todo_images/task_list.png)

To update this task, click on the update button and then click on submit after making changes.  
![Reference image](/static/todo_images/update_uncheck.png)

Here you can also mark it as complete if you have completed this task.
![Reference image](/static/todo_images/update_checked.png)

The task has been completed.
![Reference image](/static/todo_images/after_update.png)

* After successfully creating tasks, you can log out of your account to ensure that no one else can access your personal information or view your reminders.

* After logging out, you will be redirected to the login page again.
![Reference image](/static/todo_images/login.png)

### Prerequisites

* Python (>= 3.8)
* Flask==2.0.1
* Flask-SQLAlchemy==2.5.1
* Flask-Login==0.5.0
* Werkzeug==2.0.1

### Installation

1. Clone the repository: `git clone https://github.com/nitinsingh98/Todo.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (on Linux/Mac) or `venv\Scripts\activate` (on Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Initialize the database:
    * First, open the Python interpreter in the same directory:
    * Then execute the following commands:
        * `from app import db`
        * `db.create_all()`
7. To run the application, execute either `flask run` or `python app.py`.


### Usage

1. Open the application in your web browser: `http://localhost:5000`
2. Create a new task by clicking the submit button
3. Update or delete a task by clicking on it

## Contributing
------------

* Fork the repository and create a new branch for your feature or bug fix
* Commit your changes with a descriptive message
* Open a pull request to merge your changes into the main branch

## License
-------

* MIT License

## Authors
--------

* [Nitin Singh](https://github.com/me50/nitinsingh98)

## Acknowledgments
---------------

* Flask: A micro web framework for Python
* Flask-SQLAlchemy: A SQL toolkit for Flask
* SQLite: A self-contained, file-based database
