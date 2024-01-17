#!/bin/bash

DB=./hx02/data.db

rm $DB
python3 ./hx02/db.py

for i in {001..060} ; do
echo "insert into customer(name,email) values('a$i','a$i@example.com')"  \
| sqlite3 $DB
done

echo "Customer:"
echo "select * from customer" | sqlite3 $DB | tail
