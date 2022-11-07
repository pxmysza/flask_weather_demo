from flask import Blueprint, redirect, request, render_template, url_for, flash
from . import db
from forms import SearchForm
from weather_api import ConnectionMixin
from app.models.forecast import Forecast


index_blueprint = Blueprint("index", __name__)
refresh_data_blueprint = Blueprint("refresh", __name__)


def add_to_db(forecast: dict):
    forecast = Forecast.create_from_json(forecast)
    db.session.add(forecast)
    db.session.commit()
    return forecast


@index_blueprint.route("/", methods=["GET", "POST"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        city = form.city.data.lower()
        forecast = Forecast.query.filter_by(city=city).first()
        if forecast:
            flash(f"There is already a forecast from: {forecast.time.strftime('%Y-%m-%d %H:%M')} UTC")
        else:
            forecast = ConnectionMixin.get_weather_details(city)
            forecast = add_to_db(forecast)
            flash(f"No data in database. Querying API...")

        return render_template("weather.html", forecast=forecast)
    return render_template("index.html", form=form)


@refresh_data_blueprint.route("/refresh", methods=["POST"])
def refresh():
    city = request.form["city"]
    new_forecast_dict = ConnectionMixin.get_weather_details(city)
    current_forecast = Forecast.query.filter_by(city=city).first()

    new_forecast_obj = Forecast.create_from_json(new_forecast_dict)

    current_forecast.update_forecast(new_forecast_obj)

    db.session.commit()
    flash("Refreshed ")
    return render_template("weather.html", forecast=new_forecast_obj)
