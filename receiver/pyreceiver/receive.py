#!/usr/bin/python
from dweet import Dweet
from datetime import datetime
from time import sleep
import sys
import serial
import RPi.GPIO as GPIO


def sendCommand(cmd,s_port): #
    s_port.open()
    if cmd=='forward':
        # write the relevant commands here
        s_port.write("W");
    elif cmd=='backward':
        s_port.write("S");

    elif cmd=='right':
        s_port.write("D");

    elif cmd=='left':
        s_port.write("A");

    elif cmd=='stop':
        s_port.write("x");





if __name__ == "__main__":
    devicename='t27testing'
    if len(sys.argv)>1:
        devicename=sys.argv[1]
    prev=datetime.strptime("00:00:00","%H:%M:%S");
    test=serial.Serial("/dev/ttyAMA0",9600)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)

    dweet = Dweet()


    while 1==1:
        #timenow=str(datetime.now())
        GPIO.output(7,false);#turning off all LEDs
        GPIO.output(11,false);
        GPIO.output(13,false);
        GPIO.output(15,false);
        

        #receiving command from server
        #checking for HTTP connection

        try:
            rdata=dweet.latest_dweet(name=devicename)
        except Exception, e:
            print "Connection Error Occured"
            GPIO.output(13,True)
            sleep(0.5)
            GPIO.output(13,False)
            sleep(0.5)
            GPIO.output(13,True)
            exit()



        if(rdata['this']=='failed'):
            print "No data, Check Device name"
            GPIO.output(11,True)
            sleep(0.2)
            GPIO.output(11,False)
            sleep(0.2)
            GPIO.output(11,True)
            
        if(rdata['this']=='succeeded'):
            commandreceived=rdata['with'][0]['content']['command']

            #calculating timestamp of servers command
            modifieddate=rdata['with'][0]['created']
            mtime=modifieddate.split('T')[1]
            curr=datetime.strptime(mtime.split('.')[0],"%H:%M:%S");

            #checking if timestamp is new
            if curr>prev:
                print "New Data!!"
                prev=curr

                # a platform specific function to write the serial data or write the motor commands through GPIO
                sendCommand(commandreceived) 
                GPIO.output(7,True);#light the LED if new data is received

            print mtime + "  data="+rdata['with'][0]['content']['command']
        sleep(1)