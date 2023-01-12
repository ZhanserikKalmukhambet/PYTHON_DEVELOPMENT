import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="postgres",
  user="postgres",
  password="JASIK_2004"
)

sql = """
create or replace function output(lim integer, simcard varchar)
    returns table(
        contact varchar,
        tel_number varchar,
        tel_connection varchar
                 )
AS
$$
begin
    return query
        select pb.contact, pb.tel_number, pb.tel_connection from phonebook as pb
        where pb.tel_connection = $2
        ORDER BY pb.contact
        limit $1;
end
$$ language plpgsql;

select * from output(%s, %s)
"""

simcard = input('Which telephone connection?\n')
limit = input('How many people?\n')

cur = conn.cursor()

cur.execute(sql,(limit,simcard))

contacts = cur.fetchall()

for contact in contacts:
  print(contact)

conn.commit()
cur.close()
conn.close()