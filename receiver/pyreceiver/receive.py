#!/usr/bin/python
from dweet import Dweet
# from datetime import datetime
from time import sleep
import sys


if __name__ == "__main__":
    devicename='t27_testing'
    if len(sys.argv)>1:
        devicename=sys.argv[1]

    dweet = Dweet()
    while 1==1:
        #timenow=str(datetime.now())
        rdata=dweet.latest_dweet(name=devicename)
        print rdata['with'][0]['content']['timenowis']
        sleep(1)