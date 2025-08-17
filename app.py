# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from missions import missions

app = Flask(__name__)
CORS(app)

# ⚙️ Railway MySQL connection
db_config = {
    'host': 'maglev.proxy.rlwy.net',
    'user': 'root',
    'password': 'DWdqahtbPnwXnPQtOsCiTkjvoqLHkrza',
    'database': 'railway',   # make sure this DB exists in Railway
    'port': 48042
}

def run_query(sql):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)  # fetch rows as dicts
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

@app.route('/missions', methods=['GET'])
def get_missions():
    return jsonify([
        {"id": m["id"], "question": m["question"]}
        for m in missions
    ])

@app.route('/check-sql', methods=['POST'])
def check_sql():
    data = request.get_json()
    user_query = data.get('query')
    mission_id = data.get('mission_id')

    mission = next((m for m in missions if m["id"] == mission_id), None)
    if not mission:
        return jsonify({'error': 'Mission not found'}), 404

    expected_query = mission["expected_query"]

    try:
        user_result = run_query(user_query)
        expected_result = run_query(expected_query)

        if user_result == expected_result:
            return jsonify({"correct": True, "user_result": user_result})
        else:
            return jsonify({
                "correct": False,
                "user_result": user_result,
                "expected_result": expected_result
            })

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

# 🆕 New endpoint to run any query and return the result
@app.route('/run-query', methods=['POST'])
def run_custom_query():
    data = request.get_json()
    sql_query = data.get('query')

    if not sql_query:
        return jsonify({'error': 'No SQL query provided'}), 400

    # Optional safety: Allow only SELECT statements
    if not sql_query.strip().lower().startswith("select"):
        return jsonify({'error': 'Only SELECT queries are allowed'}), 400

    try:
        result = run_query(sql_query)
        return jsonify({'result': result})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400

@app.route('/')
def home():
    return jsonify({'status': 'API is running.'})

if __name__ == '__main__':
    # 👇 This makes it deploy-friendly
    app.run(host="0.0.0.0", port=5000, debug=True)
