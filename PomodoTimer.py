import time
import datetime

#Function for 25 minute timer with countdown
def promodoro():
    print('Ready, set, BE PRODUCTIVE!')
    while True:
        for _ in range(4): #x4 repeat loop
            #1500 seconds = 25 minutes
            for t in range(1500,-1,-1):
                #Countdown timer
                minutes = t / 60
                seconds = t % 60
                
                timeformat = "%d:%2d" % (minutes,seconds) 
                print(timeformat)
                time.sleep(1)
                if t == 0:
                    print('Ding!')
            #Time stamp for referencing how long you've been going.
            print(datetime.datetime.now())
            #300 = 5 min
            print('Take a 5 minute break!')
            time.sleep(300)
        print('15 minute break time! Go find taquitos!')
        #900 seconds = 15 minutes
        time.sleep(900)
        
promodoro()
