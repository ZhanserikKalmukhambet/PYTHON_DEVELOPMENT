import psycopg2
from config import config

# check the existency
def does_exists(name):
   params = config()
   conn = psycopg2.connect(**params)

   cur = conn.cursor()
   cur.execute('SELECT * FROM snake_game;')
   rows = cur.fetchall()

   for row in rows:
      if row[1] == name:
         return True
   return False

# showing data
def show_previous_result(name):
   params = config()
   conn = psycopg2.connect(**params)

   cur = conn.cursor()
   cur.execute('SELECT * FROM snake_game;')
   rows = cur.fetchall()
   for row in rows:
      if row[1] == name:
         print(f"""
                  User_name - {row[1]}
                  Level - {row[2]}
                  Score - {row[3]}
                  Speed - {row[4]} """)
   cur.close()
   conn.close()

# inserting data
def insert_data(name, lvl, score, speed):

   sql = """
         INSERT INTO snake_game(user_name, user_level, user_score, user_speed)
         VALUES (%s, %s, %s, %s); 
         """

   params = config()
   conn = psycopg2.connect(**params)

   cur = conn.cursor()
   cur.execute(sql, (name, lvl, score, speed))

   cur.close()
   conn.commit()
   conn.close()

# updating data
def update_data(lvl, score, speed, name):
   sql = f"""
         UPDATE snake_game
         SET user_level = '{lvl}',
             user_score = '{score}',
             user_speed = '{speed}'
         WHERE
             user_name = '{name}'
         """

   params = config()
   conn = psycopg2.connect(**params)

   cur = conn.cursor()
   cur.execute(sql)

   conn.commit()
   cur.close()
   conn.close()







