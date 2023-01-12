select * from phonebook;

----------------------------------

create or replace function test()
    returns INTEGER
AS
$$
begin
    return 7;
end
$$ language plpgsql;

select test() as test_results;

-----------------------------------

create or replace function inc1(num integer)
    returns INTEGER
AS
$$
begin
    return num + 1;
end
$$ language plpgsql;

select inc1(100);

-------------------------------------

create or replace function inc2(num integer)
    returns INTEGER
AS
$$
declare
    inner_res integer;
begin
    inner_res := num + 1;
    return inner_res;
end
$$ language plpgsql;

select inc2(77);

---------------------------------------------

create or replace function sum(num1 integer, num2 integer)
    returns INTEGER
AS
$$
declare
    res integer;
begin
    res := $1 + $2;
    return res;
end;
$$ language plpgsql;

select sum(100,500);

-------------------------------------------------

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

-----------------------------------------------

create or replace function getByNTopScore()
    returns table(
        id integer,
        user_name varchar,
        user_score integer
                 )
AS
$$
begin
    return query
        select sg.id, sg.user_name, sg.user_score
        from snake_game as sg
        order by sg.user_score desc
        limit 4;
end
$$ language plpgsql;

select * from getByNTopScore();

---------------------------------------------

create or replace function getabovescore(num integer)
    returns table(
        user_name varchar,
        user_score integer
                 )
as
$$
begin
    return query
        select sg.user_name, sg.user_score from snake_game as sg
        where sg.user_score >= $1;
end
$$ language plpgsql;

select * from getabovescore(5);

-----------------------------------------------------------

create or replace function scorebetweentwo(num1 integer, num2 integer)
    returns table(
        user_name varchar,
        user_score integer
                 )
as
$$
begin
    return query
        select sg.user_name, sg.user_score from snake_game as sg
        where sg.user_score between num1 and num2;
end
$$ language plpgsql;

select * from scorebetweentwo(5,25);

-----------------------------------------------

create or replace function getuser(id integer)
    returns varchar
as
$$
declare
    user_s_name varchar;
begin
    select sg.user_name into user_s_name from snake_game as sg where sg.id = $1;
    return user_s_name;
end
$$ language plpgsql;

select * from getuser(1);

--------------------------------------------

create or replace procedure addcontact(name varchar, tel varchar, card varchar, email varchar, rel varchar)
as
$$
begin
    insert into phonebook(contact,tel_number,tel_connection,email,relationship)
        VALUES (name,tel,card,email,rel);
end
$$ language plpgsql;

call addcontact('Canelo','8-777-777-77-77','Tele2','canelo@gmail.com','idol')








