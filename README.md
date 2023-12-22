Django Todo App

This is a simple Django application that displays a todo form. The form allows users to enter a task, a deadline, and a status. The status can be either "pending" or "completed".

Requirements

Python 3.8 or higher
Django 3.2 or higher

Installation

Clone the repository:
git clone https://github.com/Tomdrius/django_todo_form/
Change directory to the project directory:
cd django-todo-app
Install the dependencies:
pip install -r requirements.txt
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
source venv/bin/activate
Run the development server:
python manage.py runserver
The application will be available at http://localhost:8000.

Usage

To add a new task, fill out the form on the home page. The deadline is optional.

To mark a task as completed, change the status to "completed".

Testing

To run the tests, run the following command:

python manage.py test

Deployment

To deploy the application to production, you can use a web server such as Apache or Nginx.

License

This project is licensed under the MIT License.