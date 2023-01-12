---1_task---
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


---2_task---INSERT
create or replace procedure insert(name varchar, phone varchar)
AS $$
begin
    insert into phonebook(contact, tel_number) VALUES($1, $2);
end
$$ language plpgsql;

call insert('Cristiano','8-747-747-74-74');

---2_task---UPDATE
create or replace procedure update(name varchar, phone varchar)
AS $$
begin
    UPDATE phonebook set tel_number = $2 where contact = $1;
end
$$ language plpgsql;

call update('Cristiano', '8-707-707-70-07');


---3_task---

---pass---


---4_task---
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
        limit $1+1;
end
$$ language plpgsql;

select * from output(3, 'Tele2')


---5_task---
create or replace procedure delete(type varchar)
AS
$$
begin
    delete from phonebook where contact = $1 or tel_number = $1;
end
$$ language plpgsql;

call delete('Meirambek');
