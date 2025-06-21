import os
from flask import Flask, request, jsonify, render_template
import mysql.connector
from flasgger import Swagger

app = Flask(__name__)

# --- Flasgger 設定 (建議) ---
# 設定 Swagger UI 的基本資訊
app.config['SWAGGER'] = {
    'title': 'Flask Swagger API',
    'uiversion': 3,
    'version': '1.0.0',
    'description': '一個整合了 Swagger UI 的簡單 Flask API',
    'termsOfService': '/tos.html',
    'contact': {
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    'license': {
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'
    }
}
swagger = Swagger(app)
# -----------------------------


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
    return render_template('index.html')

@app.route('/api/data/write', methods=['POST'])
def write_data():
    """
    寫入一條新的訊息到資料庫
    ---
    tags:
      - Messages
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        description: 要新增的訊息內容
        required: true
        schema:
          type: object
          required:
            - message
          properties:
            message:
              type: string
              description: 訊息文字
              example: "Hello, world!"
    responses:
      201:
        description: 訊息成功建立
        schema:
          type: object
          properties:
            status:
              type: string
              example: success
      400:
        description: 請求格式錯誤，缺少 'message' 欄位
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Message is required"
    """
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (message) VALUES (%s)", (message,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'status': 'success'}), 201

@app.route('/api/data/read', methods=['GET'])
def read_data():
    """
    從資料庫讀取所有訊息
    ---
    tags:
      - Messages
    produces:
      - application/json
    responses:
      200:
        description: 成功讀取訊息列表
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                description: 訊息的唯一 ID
                example: 1
              message:
                type: string
                description: 訊息內容
                example: "這是一條測試訊息"
              timestamp:
                type: string
                format: date-time
                description: 訊息建立的時間戳
                example: "2025-06-21 14:30:00"
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, message, timestamp FROM messages ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    # 將 datetime 物件轉換為字串以利 JSON 序列化
    for row in rows:
        if 'timestamp' in row and row['timestamp']:
            row['timestamp'] = row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    cursor.close()
    conn.close()
    return jsonify(rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
