#!/usr/bin/python
from dweet import Dweet
from datetime import datetime
from time import sleep
import sys


if __name__ == "__main__":
    devicename='t27_testing'
    if len(sys.argv)>1:
        devicename=sys.argv[1]

    dweet = Dweet()
    while 1==1:
        timenow=str(datetime.now())
        print dweet.dweet_by_name(name=devicename, data={ "timenowis": timenow } )
        sleep(5)