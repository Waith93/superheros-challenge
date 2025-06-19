# Superheroes Challenge
A RESTful Flask API for managing superheroes, their powers, and the relationships between them. This application supports full CRUD operations with proper validations, meaningful error handling, and nested JSON responses.



## Project Structure

superheros-challenge/
├── server/
│ ├── init.py
│ ├── app.py
│ ├── models.py
│ └── seed.py
├── migrations/
├── Pipfile / Pipfile.lock
├── README.md
└── app.py

##  Getting Started

###  Setup

1. **Clone the repo**

git clone https://github.com/Waith93/superheros-challenge.git
cd superheros-challenge

### Create virtual environment and install dependencies
pipenv install
pipenv shell

### Set up the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

### Seed the database
python server/seed.py

### Run the server
flask run

### Technologies Used
Python 3
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite (for development)
SQLAlchemy Serializer
Pipenv (for dependency management)

### Models
Hero
Power
 HeroPower 	

### API Endpoints
## Heroes
GET /heroes
Returns a list of all heroes.

GET /heroes/<id>
Returns a specific hero and their associated powers.

404 if not found.

## Powers
GET /powers
Returns all available powers.

GET /powers/<id>
Returns a specific power.

404 if not found.

## PATCH /powers/<id>
Update a power’s description.

400 if description is invalid (must be ≥ 20 characters).

404 if power is not found.

## Hero Powers
POST /hero_powers
Create a new hero-power association.

Requires: strength, hero_id, power_id

400 if validation fails.

Returns nested hero and power data on success.

## Validations
Power.description must be at least 20 characters long.

HeroPower.strength must be one of ['Strong', 'Weak', 'Average'].

## Error Handling Examples
// 404 - Not Found
{
  "error": "Power not found"
}

// 400 - Validation Error
{
  "errors": ["validation errors"]
}

### Author
Stacy Waithera