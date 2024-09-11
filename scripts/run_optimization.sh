#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run database migrations
python manage.py migrate

# Load sample data (you'll need to create this fixture)
python manage.py loaddata sample_network_data.json

# Run the network optimization
python manage.py optimize_network

# Run tests
python manage.py test network_optimizer

# Start the development server
python manage.py runserver