import sqlite3 as sl

con = sl.connect('test-database.db')

with con:
	# con.executemany(sql, data)
	data = con.execute("SELECT * FROM data")
	for row in data:
		print(row)