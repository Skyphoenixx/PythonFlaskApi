import os
from flask import Flask, jsonify, render_template, request
import pymysql

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# Fetch database host from environment variable
DB_HOST = os.getenv('DB_HOST', 'localhost').split(':')[0]  # Extract host without port
DB_PORT = int(os.getenv('DB_HOST', 'localhost').split(':')[1]) if ':' in os.getenv('DB_HOST', 'localhost') else 3306
DB_USER = os.getenv('DB_USER', 'dbuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'dbpassword')
DB_NAME = os.getenv('DB_NAME', 'flaskdb')

def get_db_connection():
    connection = pymysql.connect(host=DB_HOST,
                                 port=DB_PORT,
                                 user=DB_USER,
                                 password=DB_PASSWORD,
                                 db=DB_NAME,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

@app.route('/health')
def health():
    return "Up & Running"

@app.route('/create_table')
def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
    """
    cursor.execute(create_table_query)
    connection.commit()
    connection.close()
    return "Table created successfully"

@app.route('/insert_record', methods=['POST'])
def insert_record():
    name = request.json['name']
    connection = get_db_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO example_table (name) VALUES (%s)"
    cursor.execute(insert_query, (name,))
    connection.commit()
    connection.close()
    return "Record inserted successfully"

@app.route('/data')
def data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM example_table')
    result = cursor.fetchall()
    connection.close()
    return jsonify(result)

# UI route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
