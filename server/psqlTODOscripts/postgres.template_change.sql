ALTER database template1 is_template=false;

DROP database template1;

CREATE DATABASE template1
WITH OWNER = postgres
   ENCODING = 'UTF8'
   TABLESPACE = pg_default
   LC_COLLATE = 'Bosnian (Latin)_Bosnia and Herzegovina.1252'
   LC_CTYPE = 'Bosnian (Latin)_Bosnia and Herzegovina.1252'
   CONNECTION LIMIT = -1
   TEMPLATE template0;

ALTER database template1 is_template=true;


SELECT d.datname as "Name",
       pg_catalog.pg_get_userbyid(d.datdba) as "Owner",
       pg_catalog.pg_encoding_to_char(d.encoding) as "Encoding",
       d.datcollate as "Collate",
       d.datctype as "Ctype",
       pg_catalog.array_to_string(d.datacl, E'\n') AS "Access privileges"
FROM pg_catalog.pg_database d
ORDER BY 1;
