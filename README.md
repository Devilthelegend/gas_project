# gas_project
 a Django application to provide consumer services for gas utilities. The application would allow customers to submit service requests online, track the status of their requests, and view their account information. The application would also provide customer support representatives with a tool to manage requests and provide support to customers.

# How to start the project?
Prerequisites
Ensure you have the following installed:

Python (3.x)
Pip (Python package installer)
Virtualenv (for creating isolated Python environments)

#Set Up the Virtual Environment
Create a virtual environment in the project directory:
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate

#Install Dependencies
Ensure the virtual environment is activated.

Install the required packages:
pip install -r requirements.txt

#Configure the Project
Database Setup:

Ensure you have the required database server running (e.g., SQLite, PostgreSQL).

Apply database migrations to create the necessary database tables:
python manage.py migrate

#Create a Superuser (Admin):

Create a superuser to access the Django admin interface:
python manage.py createsuperuser
#Run the Development Server
Start the Django development server:
python manage.py runserver
