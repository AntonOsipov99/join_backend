# Join Backend
A backend for the task management web app Join.
## Installation
* Clone the repository with the command "git clone git@github.com:AntonOsipov99/join_backend.git"
* Generate a virtual environment with the command "python -m venv venv"
* Start the virtual environment with "venv/Scripts/activate" on windows or "source venv/bin/activate" on mac/linux
* Install the requirements with the command "pip install -r requirements.txt"
* Create a plan for the database changes with the command "python manage.py makemigrations"
* The command "python manage.py migrate" executes the plan and makes the actual changes to your database
* Run the server with the command "python manage.py runserver"
