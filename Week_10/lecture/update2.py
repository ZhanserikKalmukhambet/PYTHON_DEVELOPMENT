import psycopg2
from config import config

def update_student(email, faculty):
   sql = """
      UPDATE students
      SET email = %s
      WHERE faculty = %s
   """

   conn = None
   updated_rows = 0

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      cur.execute(sql, (email, faculty))

      updated_rows = cur.rowcount

      conn.commit()

      cur.close()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()
   
   return updated_rows

if __name__ == '__main__':
   update_student('fuck','Business')