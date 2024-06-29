#!/bin/bash
# setup.sh

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Set up the database
flask db init
flask db migrate
flask db upgrade

# Create .env file
echo "FLASK_APP=app.py" > .env
echo "FLASK_ENV=development" >> .env
echo "DATABASE_URL=sqlite:///yourdatabase.db" >> .env

# Run the application
flask run
