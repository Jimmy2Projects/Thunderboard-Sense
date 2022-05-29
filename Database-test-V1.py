import time
import sqlite3 as sl
from datetime import datetime





# while True:
# 	print("==========")
# 	print("Now : ",now)
# 	print("type Now : ", type(now),end="\n\n")
# 	print("current_time : ", current_time)
# 	print("Type current_time : ",type(current_time))
# 	print("==========")
# 	time.sleep(1)


con = sl.connect("test-database.db")

with con:
	con.execute("CREATE TABLE IF NOT EXISTS data (data_timestamp text NOT NULL PRIMARY KEY,\
													temperature REAL,\
													humidity REAL,\
													magnetic_field REAL,\
													ambient_light REAL,\
													uv_index REAL);")



data_magnetic    = 1
data_humidity    = 1
data_temperature = 1
data_light       = 1
data_uv          = 1


while True:

	data_magnetic    += 1
	data_humidity    += 1
	data_temperature += 1
	data_light       += 1
	data_uv          += 1
	with con:
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")

		sql = 'INSERT OR IGNORE INTO data (data_timestamp,\
											temperature,\
											humidity,\
											magnetic_field,\
											ambient_light,\
											uv_index)\
											 values(?,?,?,?,?,?)'
		data = [(current_time,\
			data_temperature,\
			data_humidity,\
			data_magnetic,\
			data_light,\
			data_uv)]

		
		print("Type current_time : ",current_time)
		con.executemany(sql, data)
		print("\t+++ Database Updated +++")
	time.sleep(1)




