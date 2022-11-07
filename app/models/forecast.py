from __future__ import annotations
from app import db, ma
from datetime import datetime
from flask_marshmallow import fields


class Forecast(db.Model):
    __tablename__ = "forecasts"
    _id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(256), unique=True)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Integer)
    overcast = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    air_pressure = db.Column(db.Float)
    chance_of_rain = db.Column(db.Integer)
    chance_of_snow = db.Column(db.Integer)

    @staticmethod
    def create_from_json(json_body: dict) -> Forecast:
        return Forecast(
            city=json_body["city"],
            time=datetime.utcnow(),
            temperature=json_body["temperature"],
            humidity=json_body["humidity"],
            overcast=json_body["overcast"],
            wind_speed=json_body["wind_speed"],
            air_pressure=json_body["air_pressure"],
            chance_of_rain=json_body["chance_of_rain"],
            chance_of_snow=json_body["chance_of_snow"],
        )

    def update_forecast(self, forecast: Forecast) -> None:
        self.city = forecast.city
        self.time = forecast.time
        self.temperature = forecast.temperature
        self.humidity = forecast.humidity
        self.overcast = forecast.overcast
        self.wind_speed = forecast.wind_speed
        self.air_pressure = forecast.air_pressure
        self.chance_of_rain = forecast.chance_of_rain
        self.chance_of_snow = forecast.chance_of_snow

