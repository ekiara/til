PostgreSQL show all table permissions
----------------------------------------

<DATABASENAME>=# SELECT * FROM information_schema.role_table_grants WHERE grantee='postgres';
<DATABASENAME>=# SELECT * FROM information_schema.role_table_grants WHERE grantee='<OTHER_PG_USER_NAME>';
