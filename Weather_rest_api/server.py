from fastapi import FastAPI
from pydantic import BaseModel
import requests
import datetime

current_date = datetime.datetime.now()


class Input(BaseModel):
    city: str


api_key = "cdc494c41ee1b12822e7af2723e99690"

app = FastAPI()


@app.put('/predict')
def predict(d: Input):
    if d.city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={d.city}&appid={api_key}"
        data = requests.get(url)
        json_data = data.json()
        wether_data1 = json_data["main"]
        wether_data2 = json_data["weather"]
        temp = wether_data1["temp"]
        temp = round(temp-273.15)
        humid = wether_data1["humidity"]
        day_name = current_date.strftime('%A')
        for i in wether_data2:
            weather = i['main']
        result = {"temperature": temp, "humidity": humid,
                  "dayname": day_name, "Cloud": weather}

        return result

