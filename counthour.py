import schedule
import time

def job():
    x = 1
    while x <= 10: 
        # criaClient()
        # enviarEmail()
        print(x)
        time.sleep(1)
        x += 1
print ('asd')
schedule.every().day.at('17:26').do(job)
#schedule.every(1).seconds.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
 