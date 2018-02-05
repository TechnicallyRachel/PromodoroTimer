import time
import datetime

#Function for 25 minute timer with countdown
def promodoro():
    print('Welcome to the Promodoro Timer!\n'
          'This timer is set for 25 minute intervals,'
          '\nwith 5 minute breaks!\nAfter 4 25 minute intervals and breaks,' 
          'you get 15 minutes for a snack!')
    print raw_input("Press enter to start:")
    while True:
        #25 minute Timer with 5 minute breaks repeated 4 times
        for _ in range(4): #x4 repeat loop
            print('Ok, ready to be productive? GO!')
            #1500 seconds = 25 minutes
            for t in range(1500,-1,-1):
                #Countdown timer
                minutes = t / 60
                seconds = t % 60
                
                timeformat = "%d:%2d" % (minutes,seconds) 
                print(timeformat)
                time.sleep(1)
                if t == 0:
                    print('Ding! Nice job. Go take a 5 minute break!')
            #Time stamp for referencing how long you've been going.
            print(datetime.datetime.now())
            #300 = 5 min
            print('Take a 5 minute break!')
            time.sleep(300)
        print('15 minute break time! Go find taquitos!')
        #900 seconds = 15 minutes
        time.sleep(900)
        
promodoro()
