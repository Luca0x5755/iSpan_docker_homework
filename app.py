# app.py
import os
from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# 從環境變數取得 DB 連線設定
db_config = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'flaskdb')
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, survived, pclass, name, sex, age, sibsp, parch, cabin, ticketId, portId FROM my_train_titanic.passengers LIMIT 30;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', passengers=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
