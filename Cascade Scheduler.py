from datetime import datetime
import time
import schedule

# You will need to put your own function in place of job and run it with nohup, e.g.:
# nohup python2.7 MyScheduledProgram.py &

def job():
    print("I'm working...")
    return

schedule.every().day.at("11:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one sec

# while datetime.datetime.now() < target_time:
#     time.sleep(10)
# print('It is 3am, now running the rest of the code')
