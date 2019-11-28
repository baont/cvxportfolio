import sqlite3
con = sqlite3.connect('./db.sqlite3')
sql = """create table tick (id primary key, text1 string, num integer)"""
con.execute(sql)
sql = """insert into tick (id, text1, num) values (1, 'hello', 100)"""
con.execute(sql)
con.commit()
con.close()

import dataset
db = dataset.connect('sqlite:///db.sqlite3')
db.tables