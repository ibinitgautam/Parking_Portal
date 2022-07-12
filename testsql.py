import mysql.connector as sq

mydb = sq.connect(
    host='localhost',
    user='root',
    passwd = 'root'
)

cur = mydb.cursor()
cur.execute("use park;")
cur.execute("insert into student values(20, 'Jatin');")
mydb.commit()