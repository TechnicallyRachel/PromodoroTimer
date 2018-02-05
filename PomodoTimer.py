#from __future__ import print_function #If executing in python 2
import time
import datetime
import threading
from threading import Thread
import os
import sys

#

#Function for 25 minute timer with countdown
def promodoro1st():
    print('Ready, set, BE PRODUCTIVE!')
    while True:
        #25 minute Timer with 5 minute breaks repeated 4 times
        for _ in range(2): 
            for t in range(5,-1,-1):
                #Countdown timer
                minutes = t / 60
                seconds = t % 60
                
                timeformat = "%d:%2d" % (minutes,seconds) 
                print(timeformat)
                time.sleep(1)
                if t == 0:
                    print('Ding!')
            #25 minutes
            #180 = 3 min
            #time.sleep(180)
            print(datetime.datetime.now())
            time.sleep(5)
        print('15 minute break time! Go find taquitos!')
        #900 seconds = 15 minutes
        time.sleep(10)



#5 minutes
#time.sleep(300)
"""
#Function for 15 minute timer with countdown
def promodoro2nd():
    while True:
        for t in range(1500,-1,-1):
            minutes = t / 60
            seconds = t % 60

            timeformat = "%d:%2d" % (minutes,seconds) # Python v2 only
            print(timeformat, end='\r')
            time.sleep(1)

        #15 minutes in seconds
        time.sleep(900)
        print datetime.datetime.now()
"""

t1 = Thread(target = promodoro1st)
#t2 = Thread(target = countdown)

t1.start()
#5 minutes
#time.sleep(300)
#t2.start()












"""
#def countdown():
while True:
    t = 25
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print timeformat
    
    print(timeformat, end(\r))
    time.sleep(1)
    t -= 1
    #print('Goodbye!\n\n\n\n\n')
#countdown.start()
"""


        
"""    
def countdown(p,q):
    i=p
    j=q
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):  
            print "\r"+str(k)+str(i)+":"+str(j),
        else:
            print "\r"+str(k)+str(i)+":"+str(k)+str(j),
        time.sleep(1)
    if(i==0 and j==-1):
        print "\rDing!"
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
countdown(25,00) #countdown(min,sec)
"""
"""
#t1 = Thread(target = promodo1st)
t2 = Thread(target = countdown)

#t1.start()
#time.sleep(100)
t2.start()
"""

"""
def countdown(t):

    print('This window will remain open for 3 more seconds...')
    while t >= 0:
        print(t, end = '...')
        time.sleep(1)
        t -= 1
    print('Goodbye! \n \n \n \n \n')

t=3
"""
#print (datetime.datetime.now().strftime("%M:%S"))


"""
boom = int(input("Countdown form:"))
while boom > 0:
    time.sleep(1)
    print(boom)
    boom -= 1
print("BLASTOFF!")
"""

"""
def countdown(n) :
    while n > 0:
        print (n)
        n = n - 1
        if n == 0: < 4 
            print "BLAST OFF!"
            countdown(50)

"""
