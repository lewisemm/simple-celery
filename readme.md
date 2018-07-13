# Simple Celery

This repository contains all the code from the Celery introductory series published in [The Andela Way](https://medium.com/the-andela-way).

## Asynchronous Processing in Celery
* [main.py](main.py) - Showcases an ordinary implementation of a time consuming operation.
* [task.py](task.py) - This example implements `main.py` above in an asycnhronous manner using Celery.

## Periodic Tasks in Celery
* [periodic.py](periodic.py) - This example implements a timed periodic task that runs after every ten seconds.

## crontabs in Celery
* [birthdays.py](birthdays.py) - This example implements a birthday notification system using Celery's crontab feature.