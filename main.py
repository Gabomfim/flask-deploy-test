from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Main
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
