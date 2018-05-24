'''
You should be able to test this script on your computer without a Pi.
Delete the hashtags before "import grovepi" and "sensor_vale" and comment out (add a hashtag before) the line that contains: "sensor_value = 3" to run it with the Pi, Groove Pi and Loudness sensor.
This script will create a .csv file with the sensor_value, timestamp and date in the folder where your script lives. 
It will record the timestamp and sensor_value every second for four hours, which is equal to the "timeout" variable of 3600 seconds times 4.
This CSV file will show up in the same folder as this script 
Run with python 2
Find the GrovePi Example for using the Grove Loudness Sensor here:
https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_loudness_sensor.py
'''
import time as t
#import grovepi
from os import path
import csv
from random import randint

date = t.localtime(t.time())
name = 'LoudnessOutput1Time%d:%d:%d_Date%d_%d_%d.csv'%(date[3],date[4],date[5],date[1],date[2],(date[0] %100))
timeout = t.time() + 3600*4 
test = 0


# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND
loudness_sensor = 0

with open(name,'w+') as csvfile:
    fieldnames = ['Sound_Level', 'Time', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    while True:
        try:
            # Read the sound level
            sensor_value = randint(0,60) #generates a random number between 0 and 60 for testing without a Pi
            
            #sensor_value = grovepi.analogRead(loudness_sensor) 

            print "sensor_value =", sensor_value, "\nTime = %d:%d:%d\nDATE = %d_%d_%d\n_____________"%(date[3],date[4],date[5],date[1],date[2],(date[0] %100))

            date = t.localtime(t.time())
            timestamp = "%d:%d:%d"%(date[3],date[4],date[5])
            datestamp = "%d_%d_%d"%(date[1],date[2],(date[0] %100))                                                                            
            writer.writerow({'Sound_Level': str(sensor_value), 'Time': str(timestamp), 'Date': str(datestamp)})
            t.sleep(3)

            if t.time() > timeout:
                break

        except IOError:
            print "Error"
