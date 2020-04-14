## 3. Psycopg2 ##

import psycopg2
conn=psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
print(cur)
cur.close()


## 4. Creating a table ##

import psycopg2
conn=psycopg2.connect("dbname= dq user=dq")
cur=conn.cursor()
cur.execute("create table notes (id int, body text, title text);")
conn.close()

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value text)")
conn.close()

## 7. Executing queries ##

conn= psycopg2.connect("dbname=dq user=dq")
cur=conn.cursor()
cur.execute("INSERT INTO notes VALUES(1, 'Do more missions on Dataquest.','Dataquest reminder');")
conn.commit()
cur.execute("SELECT * from notes;")
rows= cur.fetchall()
print(rows)

conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE income OWNER dq;")
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE income;")
conn.close()