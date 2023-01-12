import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="postgres",
  user="postgres",
  password="JASIK_2004"
)

query = input('Enter the contact or phone number that you want to delete?\n')

cur = conn.cursor()

sql = """
create or replace procedure delete(type varchar)
AS
$$
begin
    delete from phonebook where contact = $1 or tel_number = $1;
end
$$ language plpgsql;

call delete(%s);
"""

cur.execute(sql,(query,))
cur.execute('SELECT * FROM phonebook;')

print('Successfully deleted !',end='\n')
contacts = cur.fetchall()
for contact in contacts:
   print(contact)

conn.commit()
cur.close()
conn.close()

