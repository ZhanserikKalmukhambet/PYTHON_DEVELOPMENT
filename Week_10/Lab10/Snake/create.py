import psycopg2
from config import config

def create_table():
   sql = """
      CREATE TABLE snake_game(
         id SERIAL NOT NULL,
         user_name VARCHAR(55) NOT NULL,
         user_level INTEGER,
         user_score INTEGER,
         user_speed INTEGER,
         primary key(id) 
      );
   """
   conn = None

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cursor = conn.cursor()
      cursor.execute(sql)
      cursor.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

if __name__ == '__main__':
   create_table()