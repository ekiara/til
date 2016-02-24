PostgreSQL getting owner of all tables 
----------------------------------------

REF: http://cully.biz/2013/12/11/postgresql-getting-the-owner-of-tables/

SELECT t.table_name, t.table_type, c.relname, c.relowner, u.usename
FROM information_schema.tables t
JOIN pg_catalog.pg_class c ON (t.table_name = c.relname)
JOIN pg_catalog.pg_user u ON (c.relowner = u.usesysid)
WHERE t.table_schema='public';
