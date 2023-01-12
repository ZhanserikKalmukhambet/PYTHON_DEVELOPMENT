import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="postgres",
  user="postgres",
  password="JASIK_2004"
)

sql = """
create or replace function getAllRecords()
    returns table(
        contact varchar,
        tel_number varchar,
        tel_connection varchar,
        email varchar,
        relationship varchar
                 )
AS
$$
begin
    return query
        select * from phonebook;
end;
$$  language plpgsql;

select * from getAllRecords();   
"""

cur = conn.cursor()
cur.execute(sql)

contacts = cur.fetchall()
for record in contacts:
   print(record)

conn.commit()
cur.close()
conn.close()
