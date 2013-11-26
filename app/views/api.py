from flask import Blueprint, jsonify

from app import db_session
from app.models.bitcoin import Minutely, Hourly, Daily

mod = Blueprint('api', __name__, url_prefix='/api/v1')

@mod.route('/minutely', methods=['GET'])
def bitcoin_prices_minutely():
    prices_by_minute = db_session.query(Minutely).all()

    price_list = {
            "label":"minutely",
            "data": []
            }

    for price in prices_by_minute:
        price_list['data'].append(
                {
                    "timestamp" : price.timestamp,
                    "last" : price.last,
                    "bid" : price.bid,
                    "ask" : price.ask
                })
    return jsonify(price_list)

@mod.route('/hourly', methods=['GET'])
def bitcoin_prices_hourly():
    prices_by_hour = db_session.query(Hourly).all()

    price_list = {
            "label" : "hourly",
            "data": []
            }

    for price in prices_by_hour:
        price_list['data'].append(
                {
                    "timestamp" : price.timestamp,
                    "last" : price.last,
                    "bid" : price.bid,
                    "ask" : price.ask
                })
    return jsonify(price_list)

@mod.route('/daily', methods=['GET'])
def bitcoin_prices_daily():
    prices_by_day = db_session.query(Daily).all()

    price_list = {
            "label" : "daily",
            "data": []
            }

    for price in prices_by_day:
        price_list['data'].append(
                {
                    "timestamp" : price.timestamp,
                    "last" : price.last,
                    "bid" : price.bid,
                    "ask" : price.ask
                })
    return jsonify(price_list)
