import sqlite3
from flask import Flask, jsonify, request
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello from Lambda!"

def lambda_handler(event, context):
    return handle_request(app, event, context)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

create_table()

# Temporary list to store users
users = []

# Function for the base route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the UserAPI Manager!"})

# Function to display all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

# Function to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id, name, email) VALUES (?, ?, ?)',
                   (new_user['id'], new_user['name'], new_user['email']))
    conn.commit()
    conn.close()
    return jsonify(new_user), 201

# Function to update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE users SET name = ?, email = ? WHERE id = ?',
                 (user_data['name'], user_data['email'], user_id))
    conn.commit()
    conn.close()
    return jsonify(user_data)

# Function to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
