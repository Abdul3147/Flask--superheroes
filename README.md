Superheroes API
Overview
The Superheroes API is a Flask-based web application that allows users to interact with a database of superheroes and their powers. Users can retrieve, update, and manage information about heroes, their powers, and the relationships between them.

Features
List All Heroes: Fetches all superheroes in the database.
Get Hero by ID: Retrieves details of a specific hero using their ID.
List All Powers: Fetches all available powers in the database.
Get Power by ID: Retrieves details of a specific power using its ID.
Update Power Description: Allows users to update the description of a power (must be at least 20 characters long).
Create Hero-Power Relationship: Enables the association of a hero with a power along with a strength level.
Technologies Used
Flask: A lightweight WSGI web application framework in Python.
Flask-SQLAlchemy: Extension for Flask that adds support for SQLAlchemy.
Flask-Migrate: Handles SQLAlchemy database migrations for Flask applications.
SQLite: A lightweight, disk-based database.
Getting Started
Prerequisites
Python 3.x
Flask
Flask-SQLAlchemy
Flask-Migrate
sqlalchemy_serializer
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-name>
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Initialize the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Seed the database (optional): Run the seeding script to populate the database with sample data:

bash
Copy code
python seed.py
Run the application:

bash
Copy code
python app.py
API Endpoints
GET /heroes: Retrieve all heroes.
GET /heroes/<id>: Retrieve a hero by ID.
GET /powers: Retrieve all powers.
GET /powers/<id>: Retrieve a power by ID.
PATCH /powers/<id>: Update a power's description.
POST /hero_powers: Create a new hero-power relationship.
