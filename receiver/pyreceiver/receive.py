#!/usr/bin/python
from dweet import Dweet# importing custom class for handling server communication
from datetime import datetime
from time import sleep
import sys

# def sendCommand(cmd): #
#     if cmd=='forward':
        # write the relevant commands here
#     elif cmd=='backward':

#     elif cmd=='right':

#     elif cmd=='left':

#     elif cmd=='stop':

if __name__ == "__main__":
    devicename='t27testing'
    if len(sys.argv)>1:
        devicename=sys.argv[1]
    prev=datetime.strptime("00:00:00","%H:%M:%S");
    dweet = Dweet()
    while 1==1:
        #timenow=str(datetime.now())
        #receiving command from server
        try:
                   rdata=dweet.latest_dweet(name=devicename)
               except Exception, e:
                   print "Connection error!!"
                   exit()
        if(rdata['this']=='failed'):
            print "No data, Check Device name"
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
                # sendCommand(commandreceived) # a platform specific function to write the serial data or write the motor commands through GPIO
            print mtime + "  data="+rdata['with'][0]['content']['command']
            sleep(1)