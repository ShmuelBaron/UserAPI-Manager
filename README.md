# UserAPI Manager

## Description

UserAPI Manager is a Flask application that provides a RESTful API for managing users. It includes endpoints to create, read, update, and delete user records, using SQLite as the database. The project is designed to be deployed on AWS Lambda using the `serverless_wsgi` library.

## Features

- **GET /users**: Retrieve a list of all users.
- **POST /users**: Add a new user.
- **PUT /users/<user_id>**: Update an existing user by ID.
- **DELETE /users/<user_id>**: Delete a user by ID.

## Requirements

- Python 3.6 or later
- Flask
- SQLite
- serverless_wsgi

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   
Navigate to the project directory:

bash
Copy code
cd UserAPI-Manager
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Usage
Create the database table: The table will be created automatically when you run the application for the first time.

Run the Flask application locally:

bash
Copy code
python app.py
The application will be available at http://127.0.0.1:5000.

Deploying to AWS Lambda:

Ensure you have the AWS CLI and serverless framework installed.
Use the serverless command to deploy your application.
API Endpoints
GET /users
Retrieve all users.

Response:

json
Copy code
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    ...
]
POST /users
Add a new user. The request body should be a JSON object with id, name, and email fields.

Request Body:

json
Copy code
{
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}
Response:

json
Copy code
{
    "id": 2,
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
}
PUT /users/<user_id>
Update an existing user. The request body should include name and email fields.

Request Body:

json
Copy code
{
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
Response:

json
Copy code
{
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
DELETE /users/<user_id>
Delete a user by ID.

Response:

json
Copy code
{
    "message": "User deleted"
}
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Feel free to open issues or submit pull requests. Please make sure to follow the coding conventions and guidelines in this repository.
