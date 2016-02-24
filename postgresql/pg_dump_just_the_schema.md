pg_dump just the schema
----------------------------------------

Note: I already knew how to do this, just wanted to NOTE it down.

$ /usr/bin/pg_dump --dbname=DBNAME --host=HOSTNAME --port=PORT --username=NAME --exclude-table=<TABLE0> --exclude-table=<TABLE1> --schema-only --format=c >> HOSTNAME_DBNAME_snapshot_`date +%Y%m%d%H%M%S`.pg
