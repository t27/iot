#iot
===
 
A simple receiver and sender set up for device to device messages over the web. This implements a socket-less interface where messages are read on demand. For a environment where instantaneous communication is required, a socket based implementation is recommended.


This code was used to send messages from a robot to the web and from a webpage to a robot(use cases described [here](#use-cases))

Currently using the [dweet.io](http://dweet.io) servers. Thanks dweet.io!

###Receiver
Code which shows the recent data sent by the sender. Implemented in both python and javascript

###Sender
Sends information to the server. Implemented in python and javascript.

###Use Cases

* A webpage to send commands to a remote computer(Embedded computer/microcontroller) - (jssender+pyreceiver)
* Display sensor data sent by an embedded computer on a webpage - (pysender+jsreceiver)
* Communicated between two embedded computers(internet of things) - (pysender+pyreceiver)
