from flask import Flask, jsonify, render_template, request

from database.database import Database
from weather import get_weather
from system_info import info

app = Flask(__name__)

db = Database()


@app.route("/")
def index():
    return render_template("index.html")


# -------------------------------------------------
# Dashboard API
# -------------------------------------------------

@app.route("/api/live")
def live():

    data = db.last()

    if data is None:
        return jsonify({"status": "waiting"})

    return jsonify(data)


@app.route("/api/weather")
def weather():

    city = db.get_setting("city", "Bursa")

    return jsonify(get_weather(city))


@app.route("/api/stats")
def stats():

    return jsonify(db.today_stats())


@app.route("/api/history")
def history():

    return jsonify(db.history())


@app.route("/api/system")
def system():

    return jsonify(info())


# -------------------------------------------------
# Settings
# -------------------------------------------------

@app.route("/settings")
def settings_page():

    return render_template("settings.html")


@app.route("/api/settings", methods=["GET"])
def settings_get():

    return jsonify(db.settings())


@app.route("/api/settings", methods=["POST"])
def settings_post():

    data = request.json

    db.set_setting("city", data.get("city", "Bursa"))
    db.set_setting(
        "electric_price",
        data.get("electric_price", "3.24")
    )
    db.set_setting(
        "refresh",
        data.get("refresh", "5")
    )

    return jsonify({

        "status": "ok"

    })


# -------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )