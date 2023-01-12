import psycopg2
from config import config

def delete_items(subject):

   sql = 'DELETE FROM professors WHERE subject = %s;'

   conn = None
   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()

      cur.execute(sql,(subject,))

      cur.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

go = input()

if __name__ == '__main__':
   delete_items(go)
