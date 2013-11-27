"""
This modules fetches bitcoin data from firebase feed.
Scheduled jobs run by the minute, hourly and daily.

"""

import json
import time, datetime
import urllib2
import schedule

from app import db_session
from app.models.bitcoin import Minutely, Hourly, Daily


def fetch_bitcoin_data():
    """
    Pull bitcoin price data from firebase.
    """

    url = "https://publicdata-bitcoin.firebaseio.com/.json"

    try:
        req = urllib2.urlopen(url)
    except urllib2.URLError:
        print("connection to {} failed.".format(url))
        return False

    resp = json.loads(req.read())
    return resp


def save_bitcoin_data(data):
    """
    Save to database using db_session.
    """
    db_session.add(data)
    db_session.commit()
    return True


def bitcoin_fetch_minutely():
    data = fetch_bitcoin_data()

    if data:
        minutely = Minutely(last=data['last'], bid=data['last'], ask=data['ask'], \
                timestamp=datetime.datetime.now())
        save_bitcoin_data(minutely)
        print("Running job: 'minutely'")


def bitcoin_fetch_hourly():
    data = fetch_bitcoin_data()

    if data:
        hourly = Hourly(last=data['last'], bid=data['bid'], ask=data['ask'], \
                timestamp=datetime.datetime.now())

        save_bitcoin_data(hourly)
        print("Running job: 'hourly'")


def bitcoin_fetch_daily():
    data = fetch_bitcoin_data()

    if data:
        daily = Daily(last=data['last'], bid=data['bid'], ask=data['ask'], \
                timestamp=datetime.datetime.now())

        save_bitcoin_data(daily)
        print("Running job: 'daily'")


def main():
    # schedule jobs frequency.
    schedule.every(1).minutes.do(bitcoin_fetch_minutely)
    schedule.every(1).hour.do(bitcoin_fetch_hourly)
    schedule.every(1).day.do(bitcoin_fetch_daily)

    while True:
        schedule.run_pending()
	time.sleep(1)
    return 1

if __name__ == "__main__":
    main()
