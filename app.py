from flask import Flask, render_template
from solar_monitor import generate_10_readings

app = Flask(__name__)

@app.route('/')
def dashboard():
    data = generate_10_readings()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    print("✅ Flask app running at: http://127.0.0.1:5000/")
    app.run(debug=True)
