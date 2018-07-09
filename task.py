import time
from celery import Celery

app = Celery("task", broker="pyamqp://guest@localhost//")


# extract the time consuming portion of code and place it into
# a separate block
@app.task
def sleep_asynchronously():
    """
    This function simulates a task that takes 20 seconds to
    execute to completion.
    """
    time.sleep(20)


print("Let's begin!")

# this is how the sleep_asynchronously() method is invoked to
# execute asynchronously
sleep_asynchronously.delay()

print("... and that's the end of our really short app.")
