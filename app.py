from flask import Flask, request, jsonify, render_template
from threading import Lock
from chattix_lib import ChatUtility

app = Flask(__name__)

# Shared storage for messages
messages = []
users = set()
lock = Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    is_valid, message = ChatUtility.validate_message(data)
    if not is_valid:
        return jsonify({"error": message}), 400

    sanitized_message = ChatUtility.sanitize_input(data["message"])
    formatted_message = ChatUtility.format_message(data["username"], sanitized_message)

    with lock:
        messages.append(formatted_message)
        users.add(data["username"])

    return jsonify({"status": "Message received"}), 200

@app.route('/receive', methods=['GET'])
def receive_messages():
    with lock:
        return jsonify(messages), 200

if __name__ == '__main__':
    app.run(debug=True)
