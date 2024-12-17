from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route("/")
def home():
    return "Hello, World!"

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
