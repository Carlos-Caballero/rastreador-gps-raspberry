import serial
import time
import string
import pynmea2

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()
	print("valor: " , newdata.decode('utf-8', 'backslashreplace'))
	newdata=newdata.decode('utf-8', 'backslashreplace')

	if newdata[0:5] == "GPGLL" or newdata[0:6] == "$GPGLL" or newdata[0:7] == "b'GPGLL":
		newmsg=pynmea2.parse(newdata)
		lat=newmsg.latitude
		lng=newmsg.longitude
		print('---------------------------------------------')
		gps = "LATITUD=" + str(lat) + " LONGITUD=" + str(lng)
		print(gps)
		print('---------------------------------------------')
