import psycopg2

conn = psycopg2.connect(
   host = 'localhost',
   database = 'postgres',
   user = 'postgres',
   password = 'JASIK_2004'
)

l = []
n = int(input())
print('Enter the contact name and its phone number:')
for i in range(n):
   tup = tuple(map(str,input().split()))
   l.append(tup)

cur = conn.cursor()

sql = """
create or replace procedure insert_list(name varchar, number varchar)
AS
$$
    begin
        insert into phonebook(contact, tel_number) values ($1, $2);
    end;
$$ language plpgsql;

call insert_list(%s, %s);
"""

errors = []

for list in l:
   cnt = 0
   ok = True
   phone_number = list[1]
   for digit in phone_number:
      if '0'<=digit<='9':
         cnt =+ 1
      elif 'a'<=digit<='z':
         ok = False
         break
   if ok == False:
      errors.append(phone_number)
   else:
      cur.execute(sql,(list[0], list[1]))

print('Incorrect data:')
for num in errors:
   print(num)

cur.close()
conn.commit()
conn.close()