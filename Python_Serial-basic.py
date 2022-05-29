import serial
import time
import sqlite3 as sl
#import paho.mqtt.client as paho
from datetime import datetime

#broker="test.mosquitto.org"
#port=1883

#def on_publish(client,userdata,result):             #create function for callback
#    print("data published")
#    pass


print("\n\t ====== Begin ======")

##
##client1= paho.Client("control1")                           #create client object
##client1.on_publish = on_publish                          #assign function to callback
##client1.connect(broker,port, keepalive=60, bind_address="")                                 #establish connection



ser = serial.Serial(port="/dev/tty.usbmodem0004402340161",
	baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS)

con = sl.connect('my-test.db')
with con:
    # con.execute("DROP TABLE data;")


	con.execute("CREATE TABLE IF NOT EXISTS data_V3 (data_timestamp TEXT NOT NULL PRIMARY KEY,\
		temperature REAL,humidity REAL,magnetic_field REAL,ambient_light REAL,uv_index REAL);")

# ser.isOpen()
i=0
data_magnetic    = None
data_humidity    = None
data_temperature = None
data_light       = None
data_uv          = None

Topic_Temperature = "Thunderboard/Temperature"
Topic_Humidity    = "Thunderboard/Humidity"
Topic_Magnetic    = "Thunderboard/Magnetic" 
Topic_Light       = "Thunderboard/Light" 
Topic_UV          = "Thunderboard/UV" 
print(Topic_Temperature)
print(Topic_Humidity)
print(Topic_Magnetic)
print(Topic_Light)
print(Topic_UV)

while True:
	
	# i+=1
	# print(i)
	data       = ser.readline().decode("utf-8")
	# time.sleep(1)
	data_type  = data[4:6] 
	data_value = str(data[7:])
	# if value[]
	# print(value[-7:-2])
	# print("\n\n==========")
	# print(data,e)
	# print("data type+",data_type.rstrip("\n"),"+\n")
	# print("data type+",data_type)
	# # print(type(data_type))
	# # print("data value+",data_value.rstrip("\n"),"+\n")
	# print("data value+",data_value)
	# print("==========")
	# 31.79\\

	if(data_type == "TE"):
		data_temperature = data_value.strip("\r")
		print("Temperature : ",data_value)
		# print("length of data : ", len(data_value))
		# print("Type of data :", type(data_value))
		# print("|")

	elif(data_type == "HU"):
		data_humidity = data_value.strip("\r")
		print("Humidity : ",data_value)
		# print("length of data : ", len(data_value))
		# print("Type of data :", type(data_value))
		# print("|")

	elif (data_type == "MA"):
		data_magnetic = data_value.strip("\r")
		print("Magnetic field : ",data_value)
		# print("length of data : ", len(data_value))
		# print("Type of data :", type(data_value))
		# print("|")	
	
	elif(data_type == "LU"):
		data_light = data_value.strip("\r")
		print("Ambient light : ",data_value)
		# print("length of data : ", len(data_value))
		# print("Type of data :", type(data_value))
		# print("|")

	elif(data_type == "UV"):
		data_uv = data_value.strip("\r")
		print("UV index : ",data_value)
		# print("length of data : ", len(data_value))
		# print("Type of data :", type(data_value))
		# print("|")

	else:
		print("no condition fullfiled")

	# sql = 'INSERT INTO data_V2 ( temperature,humidity,magnetic_field,ambient_light,uv_index) values(?,?,?,?,?)'
	# data = [(data_temperature,data_humidity,data_magnetic,data_light,data_uv)]
##	sql = 'INSERT OR IGNORE INTO data_V2 (data_timestamp,temperature,humidity,magnetic_field,ambient_light,uv_index) values(?,?,?,?,?,?)'
##	data = [(current_time,data_temperature,data_humidity,data_magnetic,data_light,data_uv)]

	if ((data_temperature!=None) and (data_humidity!=None) and (data_magnetic!=None) and (data_light!=None) and (data_uv != None)):
		
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")

		print("\n\n\n==========")

		print("Current Time =", current_time)
		print(Topic_Temperature)
		
		print("---------- Temperature ----------")
##		send_data_temperature    = client1.publish(Topic_Temperature ,data_temperature)
		# print(Topic_Temperature )
		# print("|",end="")
		print(data_temperature)
		# print("|",end="")

		print("---------- Humidity ----------")
##		send_data_humidity       = client1.publish(Topic_Humidity    ,data_humidity)
		# print(Topic_Humidity    )
		# print("|",end="")
		print(data_humidity)
		# print("|",end="")

		print("---------- Magnetic Field ----------")
##		send_data_magnetic_field = client1.publish(Topic_Magnetic    ,data_magnetic)
		# print(Topic_Magnetic    )
		# print("|",end="")
		print(data_magnetic)
		# print("|",end="")

		print("---------- Ambient Light ----------")		
##		send_data_ambient_light  = client1.publish(Topic_Light       ,data_light)
		print(Topic_Light       )
		# print("|",end="")
		print(data_light)
		# print("|",end="")

		print("---------- UV Index ----------")
##		send_data_uv_index       = client1.publish(Topic_UV          ,data_uv)
		print(Topic_UV          )
		# print("|",end="")
		print(data_uv)
		# print("|",end="")

		print("==========")

		# print("\n\n")

		with con:
			now = datetime.now()
			current_time = now.strftime("%H:%M:%S")
	
			sql = 'INSERT OR IGNORE INTO data_V3 (data_timestamp,temperature,humidity,magnetic_field,ambient_light,uv_index) values(?,?,?,?,?,?)'
			data = [(current_time,data_temperature,data_humidity,data_magnetic,data_light,data_uv)]



			print("Type current_time : ",current_time)
			con.executemany(sql, data)
			print("\t+++ Database Updated +++")
			print("==========")
		data_magnetic    = None;
		data_humidity    = None;
		data_temperature = None;
		data_light       = None;
		data_uv          = None;
		# time.sleep(1.5)


# input=1
# while 1 :
#     # get keyboard input
#     input = ">> "

#         # Python 3 users
#         # input = input(">> ")
#     if input == 'exit':
#         ser.close()
#         exit()
#     else:
#         # send the character to the device
#         # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
#         ser.write(input + '\r\n')
#         out = ''
#         # let's wait one second before reading output (let's give device time to answer)
#         time.sleep(1)
#         while ser.inWaiting() > 0:
#             out += ser.read(1)
            
#         if out != '':
#             print(">>" + out)
