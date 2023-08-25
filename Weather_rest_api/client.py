from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        city = data.get("city_name")
        payload = json.dumps({"city": city})
        response = requests.put("http://127.0.0.1:8000/predict", data=payload)
        output = response.json()
        temp = output["temperature"]
        humid = output["humidity"]
        day_name = output["dayname"]
        weather = output["Cloud"]

    return render_template("submit.html", temperature=temp, humidity=humid, weather_type=weather, day_name=day_name, city=city.capitalize())


if __name__ == "__main__":
    app.run(debug=True)
