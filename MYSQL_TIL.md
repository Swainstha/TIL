# December 4, 2017

##### Terminologies
```
Primary key is a unique key value and should anot occur twicw in the table - (Eg. Column)

Foreign key links two tables together.

Compound key consists of multiple columns.

Index in a database is like an index in back of book.

Redundancy is the phenomena or idea of storing of data twice.
```
-----
##### Log into mysql

```
mysql -u root -p

mysql --local-infile=1 -u root -p     //For writing and reading file permissions

Then type your mysql password
```
-----
##### Show databases using command line
```mysql
SHOW DATABASES/databases;
```
##### Change database 
```mysql
USE <database_name>
```
##### Show tables 
```mysql
SHOW TABLES/tables;
```
##### Showing table structure
```mysql
SHOW COLUMNS FROM <table_name>;
DESCRIBE <table_name>;
```
##### Create Database
```mysql
CREATE DATABASE <database_name>
```
##### Delete Databases
```mysql
DROP DATABASE <database_name>
```

##### Delete table
```mysql
DROP TABLE table_name;
```

##### Use Database
```mysql
USE <database_name>

We must use this command before creating a new table in a database
```
##### Creating a Table
```mysql
CREATE TABLE <table_name> (
column_name(feature_name) data_type if_must_be_filled(NULL or NOT NULL) AUTO_INCREMENT(For IDs) DEFAULT default_value,
PRIMARY_KEY(id_var)
);

CREATE TABLE teams_db (
team_id INT NOT NULL AUTO_INCREMENT FIRST,
team_name VARCHAR(100) NOT NULL AFTER team_id,
PRIMARY_KEY(team_id)
);
```
##### Inserting data into a table
```mysql
INSERT INTO <table_name> (
var_name1, var_nam2, var_nam3)
VALUES(data1, data2, data3);

The string can be inserted using ' ' or " ". doesnot matter.

INSERT INTO team_tbl (
team_name, team_captain, establishment_data)
VALUES('Dronacharya', "Swain Shrestha", NOW()/'2017-12-04');
```

##### See all values of the table
```mysql
SELECT * FROM <table_name>;    // * is a WildCard

```
##### Select specific non repeating data from a table
```mysql 
SELECT DISTINCT var_name FROM table_name;
```
##### select limited rows
```mysql
SELECT var_name FROM table_name LIMIT number;
```
##### Select specific data from a table
```mysql
SELECT var_name FROM <table_name> [WHERE condition that the data must satisfy];

SELECT table_name.var_name FROM table_name;  //using fully qualified names

SELECT team_name FROM team_tbl WHERE team_captain="Swain Shrestha";

Upper case and lower case do not matter by default.
```

##### Select specific data using BETWEEN
```mysql
SELECT team_name FROM team_tbl WHERE team_id BETWEEN 1 AND 5;
```

##### Select specific data using IN
```mysql
SELECT team_name FROM team_tbl WHERE team_captain IN/NOT IN ('Swain','Sushil','Sajan','Shovan', 'Nischal');
```

##### Select using Wildcards
```
SELECT team_name FROM team_tbl WHERE team_captain LIKE 'comp%';

SELECT team_name FROM team_tbl WHERE team_captain LIKE '%comp%';

SELECT team_name FROM team_tbl WHERE team_captain LIKE 'h%d'; //anything starting with h and ending with d
```

##### Comparision Operators
```
> < >= <= !=(<>) =
```

##### Logical Operators
```mysql
AND OR NOT
```

##### Comparion for Special character like NULL
```mysql
IS

SELECT team_name FROM team_tbl WHERE tteam_captain IS NULL;
```

##### Extract year from Date
```mysql
YEAR(NOW());    YEAR(2052-03-10);
```

##### Ordering the table elements
```mysql
SELECT * FROM <table_name> ORDER BY <var_name1>,<var_name2> ASC/DESC LIMIT <no_of_elements_t display>;

SELECT * FROM team_tbl ORDER BY establishment_date ASC LIMIT 1;  //finding lowest or highest
```
##### Using GROUP BY
```mysql
if the table consists of two captains with the same name but with different team names the GROUP BY will show only one person's name.

SELECT * FROM <table_name> GROUP_BY <var_name> ORDER BY <var_name2> ASC;

SELECT * FROM team_tbl GROUP BY team_captain ORDER BY team_name ASC;
```
##### Quering multiple tables
```mysql
SELECT var_name1, var_name2 FROM table1, table2 WHERE table1.var_name3 = table1.var_name3;

SELECT team_name, team_captain, result FROM team_tbl, result_tbl WHERE 
team_tbl.team_id = result_tbl.team_id;
```

##### Deleting everything from the table
```mysql
DELETE FROM <table_name>;
```

##### Deleting with condition
```mysql
DELETE FROM <table_name> where var_name = something;

DELETE FROM team_tbl WHERE team_id = 5;
```
##### Update table
```mysql
UPDATE <table_name> SET field1 = new_value1, field2 = new_value2 [WHERE];

UPDATE team_tbl SET team_captain = "John Subba" WHERE team_name = "Bulls";
```
##### using incomplete variable name to select
```mysql
SELECT var_name1, var_name2 WHERE var_name3 LIKE 'valu%';

SELECT team_id, team_name WHERE team_captain LIKE 'Swa%';
```
##### Using Regex
```mysql
^       matches beginning of the string.
$       matches pattern at the end of the string.
.       Any single character
[...]   Any character listd between the square brackets.
[^]     Any character not listed between the square brackets.
p1|p2|p3  Matches any pattern p1, p2, p3
*       zero or more instances of preceding element
+       one or more instances of preceding element
{n}     n instances of preceding element
{m, n}  m through n instances of preceding element
```
```
SELECT var_name1 FROM table_name WHERE REGEXP '^L';

SELECT var_name FROM table_name WHERE REGEXP '[1-5] boxes of frogs';
```

##### Alter table
```mysql
ALTER TABLE table_name DROP var_name

ALTER TABLE table_name ADD var_name2 INT NOT NULL AFTER var_name1;

ALTER TABLE table_name ADD var_name DATE NOT NULL FIRST; 

ALTER TABLE table_name MODIFY var_name VARCHAR(10);

ALTER TABLE table_name1 RENAME TO table_name2;

ALTER TABLE table_name ADD PRIMARY KEY (column_list);

ALTER TABLE table_name ADD UNIQUE index_name (column_list);

ALTER TABLE table_name ADD INDEX index_name (column_list);
```

##### Creating index
```mysql
CREATE INDEX index_name ON table_name (column1, column2);
```

##### Temporary Table
```mysql
CREATE TEMPORARY TABLE ...;
The table wont be shown using SHOW TABLES and it will vanish after logging out the session.
```

##### Tackling secure file privileges
```mysql
SHOW VARIABLES LIKE "secure_file_priv";

and using the same path for the file.
```

##### Write data from table to file and load data from file to table
```mysql
SELECT * FROM table_name INTO OUTFILE 'var/lib/mysql-files/file_name.txt' FIELDS TERMINATED By ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n\r';

LOAD DATA LOCAL INFILE 'var/lib/mysql-files/file_name.txt' INTO TABLE table_name FIELDS TERMINATED By ',' ENCLOSED BY '"'  LINES TERMINATED BY '\r';
```
##### Dump database or table to a file or from file to a database
```mysql
mysqldump -u root -p db_name table_name > ~/Desktop/table_name_dump.txt

mysqldump -u root -p db_name table_name < ~/Desktop/table_name_dump.txt

mysqldump -u root -p db_name < ~/Desktop/db_name_dump.txt
```
##### MYSQLIMPORT
```mysql
mysqlimport -u root -p --local db_name ~/pathname/file_name.txt

mysqlimport -u root -p --local --fields-terminated-by="," --line-terminated-by="\r\n" db_name ~/pathname/file_name.txt
```

##### Import using LOAD DATA
```mysql
LOAD DATA LOCAL INFILE '~/pathname/file_name.txt' INTO TABLE table_name;
```
-----
-----

# December 4, 2017


##### Starting lampp server
```
sudo /opt/lampp/lampp start
```

##### Stopping lampp server
```
sudo /opt/lampp/lampp stop
```
##### Using terminal for apache server
```
Start apache command: $ sudo systemctl start apache2.service.
stop apache command : $ sudo systemctl stop apache2.service.
restart apache command: $ sudo systemctl restart apache2.service.
apache2ctl command can be used to stop or start apache web server under any Linux distribution or UNIX
```
##### Creating custom column
```mysql
SELECT CONCAT(var_name1, ',', var_name2) AS new_var_name FROM table_name;
```

##### Using Functions
```
SELECT name, UPPER(name) FROM table_name;

SELECT cost, SQRT(cost) FROM table_name;  

###### Aggregate function

SELECT AVG(cost), SUM(cost) FROM table_name; 

SELECT COUNT(*) AS count, SUM(cost) AS sum, MAX(cost) AS max FROM table_name WHERE team_id=1;
```

##### Using HAVING
```mysql
SELECT seller_id, COUNT(*) AS count FROM table_name GROUP BY seller_id HAVING COUNT(*) > 3;

HAVING is used when we use GROUPs and WHERE is used when we want rows.

```
##### Using Sub-Query
```
SELECT name, cost FROM table_name WHERE cost >= (
  SELECT AVG(cost) FROM table_name
)
ORDER BY cost DESC;
```

##### Using JOIN
```
//LEFT JOIN means the left table is included no matter what,forces left table tp be shown.

SELECT customer.name, items.name FROM customer LEFT OUTER JOIN  
items ON customer.id = seller_id;
```

##### Using UNION
```
SELECT name, cost, bids FROM table_name  WHERE bids > 100
UNION
SELECT name , cost, bids FROM table_name WHERE cost < 1000 ;

The column names must be the same in both the queries.

UNION ALL - leaves duplicate entries
```

##### Insert into multiple rows
```
INSERT INTO table_name(var1, var2, var3) VALUES
(p1,q1, r1),
(p2, q2, r2);

INSERT INTO table_name(var1, var2, var3) SELECT

```
-----
-----

# December 5, 2017

##### Rename table
```mysql
RENAME TABLE table_name1 TO table_name2;
```

##### Using view
```mysql
CREATE VIEW view_name AS
SELECT * FROM table_name;

View is a dynamic table for viewing purpose which gets updated whenever the original table gets updated.
```
##### ACID
```
Atomicity - All parts of a transaction succeed or fail together.

Consistency - The database will always be consistent.

Isolation - No transaction can interfere with another's. Isolation brings us the benefit of hiding uncommitted state changes from the outside world, as failing transactions shouldn’t ever corrupt the state of the system.

Durability - Once the transaction is committed it wont be lost. A successful transaction must permanently change the state of a system
```
