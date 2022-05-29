import serial
import time
ser = serial.Serial(port="/dev/tty.usbmodem0004402340161",
	baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS)

while True:
	data       = ser.readline().decode("utf-8")
	time.sleep(1)
	print("Raw data :", data)
	data_type  = data[4:6] 
	data_value = str(data[7:])
	print("data type+",data_type)
	print("data value+",data_value)