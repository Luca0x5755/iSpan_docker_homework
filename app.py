# app.py
import os
from flask import Flask, request, jsonify, render_template
# import mysql.connector

app = Flask(__name__)

# 從環境變數取得 DB 連線設定
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'flaskdb')
}

# def get_db_connection():
#     return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/api/data/write', methods=['POST'])
# def write_data():
#     data = request.get_json()
#     message = data.get('message')
#     if not message:
#         return jsonify({'error': 'Message is required'}), 400

#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return jsonify({'status': 'success'}), 201

# @app.route('/api/data/read', methods=['GET'])
# def read_data():
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT id, message, timestamp FROM messages ORDER BY timestamp DESC")
#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify(rows)







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
