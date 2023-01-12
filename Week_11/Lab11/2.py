import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="postgres",
  user="postgres",
  password="JASIK_2004"
)

cur = conn.cursor()

name = input('Enter the contact:\n')

sql_insert = """
create or replace procedure insert(name varchar, phone varchar)
AS $$
begin
    insert into phonebook(contact, tel_number) VALUES($1, $2);
end
$$ language plpgsql;

call insert(%s,%s);
"""

sql_update = """
create or replace procedure update(name varchar, phone varchar)
AS $$
begin
    UPDATE phonebook set tel_number = $2 where contact = $1;
end
$$ language plpgsql;

call update(%s, %s);
"""

cur.execute('Select * FROM phonebook;')
contacts = cur.fetchall()

is_exist = False
for contact in contacts:
   if contact[0] == name:
      phone = input('This contact has already registered! Enter the phone number for updating:\n')
      cur.execute(sql_update, (name, phone))
      is_exist = True
      break

if is_exist == False:
   phone = input(f'Enter the phone number of {name}:\n')
   cur.execute(sql_insert, (name, phone))

conn.commit()
cur.close()
conn.close()
