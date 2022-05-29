import sqlite3 as sl

con = sl.connect('my-test.db')


with con:
    con.execute("DROP TABLE data;")