from sqlite3 import connect
import psycopg2
from config import config

def insert_list_names(names):
   sql = 'INSERT INTO professors(name, subject) VALUES(%s, %s)'
   conn = None

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()

      cur.executemany(sql,names)

      conn.commit()
      cur.close()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

l = []

for i in range(5):
   t = tuple(map(str,input().split()))
   l.append(t)

if __name__ == '__main__':
   insert_list_names(l)