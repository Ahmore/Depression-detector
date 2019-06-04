from apscheduler.schedulers.background import BackgroundScheduler

import gui.start
from services.api import get_azure_data
from services.api import get_azure_token
from services.api import send_measurement
from services.camera import make_photo
import datetime

def start_interval_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(make_photo_interval_job, 'interval', minutes=60)
    scheduler.start()

def make_photo_interval_job():
    token = get_azure_token(gui.login.token)
    photo = make_photo()
    photo_data = get_azure_data(token, photo)

    now = str(datetime.datetime.now())
    data = {
        'hidden_photo': photo_data
    }

    send_measurement(gui.login.token, now, data)