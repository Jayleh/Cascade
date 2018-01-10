import time
import schedule
from cascadeSource.loginExport import loginExport
from cascadeSource.googleDriveAPI.driveAPI import upload

# You will need to put your own function in place of job and run it with nohup, e.g.:
# nohup python2.7 MyScheduledProgram.py &

def job():
    print("Working on it..")
    loginExport()
    upload()
    print("I did it!")
    return

# schedule to run everyday at 11:00am
schedule.every().day.at("13:36").do(job)

# schedule.every(5).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)  # wait one sec
