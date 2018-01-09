import time
import schedule
import loginExport
import googleAPI

# You will need to put your own function in place of job and run it with nohup, e.g.:
# nohup python2.7 MyScheduledProgram.py &

def job():
    loginExport.setUp()
    loginExport.loginExport()
    loginExport.tearDown()
    googleAPI.upload()
    return

schedule.every().day.at("11:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one sec
