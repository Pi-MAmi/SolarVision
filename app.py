from flask import Flask, jsonify, render_template

from database.database import Database
from weather import get_weather

app = Flask(__name__)

db = Database()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/live")
def live():

    data = db.last()

    if data is None:
        return jsonify({"status": "waiting"})

    return jsonify(data)


@app.route("/api/weather")
def weather():

    return jsonify(get_weather())


@app.route("/api/stats")
def stats():

    return jsonify(db.today_stats())


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )