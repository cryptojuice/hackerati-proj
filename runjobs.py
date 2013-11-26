import json
import time, datetime
import urllib2
import schedule

from app import db_session
from app.models.bitcoin import Minutely, Hourly, Daily

URL = "https://publicdata-bitcoin.firebaseio.com/.json"

def fetch_bitcoin_data():
    req = urllib2.urlopen(URL)
    resp = json.loads(req.read())
    return resp


def bitcoin_fetch_minutely():
    data = fetch_bitcoin_data()

    minutely = Minutely(last=data['last'], bid=data['last'], ask=data['ask'], \
            timestamp=datetime.datetime.now())

    db_session.add(minutely)
    db_session.commit()
    print("Log: Running minute job.")
    return True
    
def bitcoin_fetch_hourly():
    data = fetch_bitcoin_data()

    hourly = Hourly(last=data['last'], bid=data['bid'], ask=data['ask'], \
            timestamp=datetime.datetime.now())

    db_session.add(hourly)
    db_session.commit()
    print("Log: Running hourly job.")
    return True

def bitcoin_fetch_daily():
    data = fetch_bitcoin_data()

    daily = Daily(last=data['last'], bid=data['bid'], ask=data['ask'], \
            timestamp=datetime.datetime.now())

    db_session.add(daily)
    db_session.commit()
    print("Log: Running daily job.")
    return True

def main():
    schedule.every(1).minutes.do(bitcoin_fetch_minutely)
    schedule.every(1).hour.do(bitcoin_fetch_hourly)
    schedule.every(1).day.do(bitcoin_fetch_daily)

    while True:
        schedule.run_pending()
	time.sleep(1)
    return 1

if __name__ == "__main__":
    main()
