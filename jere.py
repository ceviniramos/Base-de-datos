import sqlite3
conn=sqlite3.connect("repaso.db")
cursor=conn.cursor()
cursor=conn.execute("select * from futbol") 