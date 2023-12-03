from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello World")

@app.route('/health')
def health():
    is_application_online = True  # Placeholder for the health check result

    if is_application_online:
        status = "success"
        details = "Application is online"
    else:
        status = "failure"
        details = "Application is offline"

    return jsonify(status=status, details=details)
    
if __name__ == '__main__':
    app.run(debug=True)
