import psycopg2
from config import config

sql = """
   update students
   set faculty = 'FIT',
           age = 22
   where name = 'Jones' or name = 'Smith';
"""

params = config()

conn = psycopg2.connect(**params)
cur = conn.cursor()
cur.execute(sql)

conn.commit()

cur.close()
conn.close()
