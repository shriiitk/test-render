from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Web Service!"

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

# Main entry point
if __name__ == "__main__":
    # This is for local testing, but in production, we will use gunicorn to run the server.
    app.run(debug=True)
