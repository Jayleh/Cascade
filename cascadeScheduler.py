import time
import schedule
from cascadeSource.loginExport import loginExport
from cascadeSource.cleanSales import cleanSales
from cascadeSource.googleDriveAPI.pygsheetsAPI import update

# You will need to put your own function in place of job and run it with nohup, e.g.:
# nohup python2.7 MyScheduledProgram.py &


def job():
    print("Working on it...")
    loginExport()
    cleanSales()
    update()
    print("I did it!")
    return


# Schedule to run everyday at 24:00
schedule.every().day.at("14:22").do(job)

# schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # Wait one sec
