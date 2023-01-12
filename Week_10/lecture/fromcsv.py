import psycopg2
from config import config

def from_csv_to_table():
   

   conn = None

   try:
      sql = """
         COPY persons(first_name,last_name,dob,email)
         FROM \'C:\Programming Principles II\PP2_LAB\Week_10\lecture\persons.csv\'
         DELIMITER \',\'
         CSV HEADER;
      """

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
    from_csv_to_table()