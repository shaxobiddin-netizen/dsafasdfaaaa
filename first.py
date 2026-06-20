import psycopg2

conn = psycopg2.connect(
    host     = 'localhost',
    port     = 5432,
    database = 'maktab',
    user     = 'postgres',
    password = '1234'
)
cur=conn.cursor()
cur.execute("select * from maktab")
natija=cur.fetchall()
for i in natija:
    print(i)
print('Ulanish muvaffaqiyatli!')
conn.close()
cur.close()

