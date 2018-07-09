import datetime

import mysql.connector

from celery import Celery
from celery.schedules import crontab

app = Celery('birthdays', broker="pyamqp://guest@localhost//")

# we need to disable UTC so that Celery can use local time
app.conf.enable_utc = False


@app.task
def birthdays_today():
    conn = mysql.connector.connect(
        user='root', database='employees', password='')

    curs = conn.cursor()

    today = datetime.datetime.now()

    query = """SELECT first_name, last_name FROM employees
    WHERE month(birth_date)={0} and day(birth_date)={1};""".format(
        today.month, today.day)

    curs.execute(query)

    for (first_name, last_name) in curs:
        print(
            """

            Hi {0} {1},

            We would like to wish you a great birthday and a memorable year.

            From all of us at company ABC.
            """.format(first_name, last_name)
        )

    curs.close()
    conn.close()


# add "birthdays_today" task to the beat schedule
app.conf.beat_schedule = {
    "birthday-task": {
        "task": "birthdays.birthdays_today",
        "schedule": crontab(hour=20, minute=15)
    }
}
