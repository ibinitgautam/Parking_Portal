import mysql.connector as sql

mydb = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

cur = mydb.cursor()

cur.execute("use park;")
cur.execute("select Payment from payment;")

for pay in cur:
    print(pay[0] + 3000)
    break;


#print(int(cur[0]) + 3000)