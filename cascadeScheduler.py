import time
import schedule
from cascadeSource.loginExport import loginExport
from cascadeSource.googleDriveAPI.pygsheetsAPI import update

# You will need to put your own function in place of job and run it with nohup, e.g.:
# nohup python2.7 MyScheduledProgram.py &


def job():
    print("Working on it..")
    loginExport()
    update()
    print("I did it!")
    return


# Schedule to run everyday at 11:00am
schedule.every().day.at("10:51").do(job)

# schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # Wait one sec
