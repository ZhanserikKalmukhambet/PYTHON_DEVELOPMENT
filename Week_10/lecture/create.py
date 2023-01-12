import psycopg2
from config import config

def create_tables():
   commands = (
      """
      CREATE TABLE workers(
         name VARCHAR(100), 
         salary INTEGER
      )
      """,
      """
      CREATE TABLE professors(
         name VARCHAR(100),
         subject VARCHAR(100)
      )
      """,
      """
      CREATE TABLE children(
         name VARCHAR(100),
         age INTEGER
      )
      """
   )

   conn = None

   try:
      params = config()

      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      
      for command in commands:
         cur.execute(command)

      cur.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

if __name__ == '__main__':
    create_tables()