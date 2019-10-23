# NixieDriver
BCD clock application for RPI, used to drive a rudamentary Nixie tube circuit.

Currently this application is outputting 4 BCD values across 16 GPIO pins, each BCD output is inteded to be decoded using a Nixie driver chip (such as a 74141 http://g3ynh.info/digrdout/74141.html).

Future iterations will aim move to an I2C output which will then release 10 of the used GPIO outputs.

# Notes
I've created an rpi.gpio module facade within this solution to enable development and testing on a windows enviroment. Throughout the code, anywhere a call needs to be made to the RPi.GPIO module it is made to the facade instead, if the module import within the facade is unsuccessful then a dummy method is called instead.
