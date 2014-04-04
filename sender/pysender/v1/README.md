##Sender

Dweets (Sends a request) to dweet.io as a predefined device at a fixed interval. Contains information which may be of relevance to other pages.

###First Version
Run sender.py  from v1 folder with
'''
./sender.py [devicename]
'''
This will dweet the current system time every 5 seconds(add the request delays) to a device named passed in the first command line argument, otherwise it will default to 't27_testing'.
The returned packet is displayed on the console.