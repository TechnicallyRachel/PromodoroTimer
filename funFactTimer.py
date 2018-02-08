#This script lies about its timer and is designed to run quickly to see the program running from beginning to end.
# 3 seconds for the "25 minutes", 2 seconds for "5 minute break", and 5 seconds for "15 minute break".
# I can quickly change these times to the exact requested ones upon request.

import time
import datetime

#Fact variables for each timer segement 
First = ('Did you know that in the last 25 minutes an average of 5625 babies were born?\n'
    'Really puts things in perspective huh?')
Second = ('While you were working diligently for 25 minutes,\n'
          'the Earth was struck by lightning\n'
    '150000 times…I wonder if any of that was near you?')
Third = ('Another 25 minutes down! During those 25 minutes Americans ate about 15250 hot dogs.\n'
    'How many do you think were in New York?')
Fourth = ('Boom! That 25 minutes flew by in a flash! If the fastest mile runner in the world ran the entire time\n'
    'you were working he would have ran almost 7 miles.\n'
    'That really doesn’t even seem possible.')


#Fun Facts Function for "25 minute" timer with countdown
def FactTimer():
    print('Welcome to the Fun Factual Producticity Timer!\n'
          #ASCII ART IMAGE HERE
          'This timer is set for 25 minute intervals,'
          '\nwith 5 minute breaks!\nAfter 4 25 minute intervals and breaks,' 
          'you get 15 minutes for a snack!')
    print raw_input("Boldly press enter to start:")
    while True:
        #Timer with loop iteration for different facts each time.
        facts = [First, Second, Third, Fourth]
        for i in range(len(facts)):
            print('Ok, ready to be productive? GO!') 
            #main timer
            for t in range(3,-1,-1):
                #Countdown timer
                minutes = t / 60
                seconds = t % 60
                
                timeformat = "%d:%2d" % (minutes,seconds) 
                print(timeformat)
                time.sleep(1)
                if t == 0:
                    print('Ding! Nice job. Go take a 5 minute break!')
                    print(facts[i])
                    
            #Time stamp for referencing how long you've been going.
            print(datetime.datetime.now())

            print('Take a "5 minute" break!')
            time.sleep(2)

        print('15 minute break time! Go find taquitos!')
        #5 second longer break
        time.sleep(5)
        
FactTimer()
