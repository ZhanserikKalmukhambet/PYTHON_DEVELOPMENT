import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="postgres",
  user="postgres",
  password="JASIK_2004"
  )

cur = conn.cursor()

func = """
   create or replace function getcontactnumber()
    returns table(
        contact VARCHAR,
        tel_number VARCHAR
                 )
AS
$$
begin
   return query
       select p.contact, p.tel_number from phonebook as p;
end
$$ language plpgsql;

select *
from getcontactnumber();
"""
cur.execute(func)
info = cur.fetchall()
for contact in info:
   print(contact[0], '-', contact[1])

conn.commit()
cur.close()
conn.close()