# NixieDriver
BCD clock application for RPI, used to drive a rudamentary Nixie tube circuit.

Currently this application is outputting 4 BCD values across 16 GPIO pins, each BCD output is inteded to be decoded using a Nixie driver chip (such as a 74141 http://g3ynh.info/digrdout/74141.html).

Future iterations will aim move to an I2C output which will then release 10 of the used GPIO outputs.
