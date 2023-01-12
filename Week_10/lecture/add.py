import psycopg2
from config import config

def add_column():

   sql = """
      alter table professors
      add column age INTEGER,
      add column s_language VARCHAR(255);
   """

   conn = None
   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()

      cur.execute(sql)

      cur.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

if __name__ == '__main__':
   add_column()