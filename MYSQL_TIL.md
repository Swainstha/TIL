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

```mysql -u root -p

Then type your mysql password
```
-----
##### Show databases using command line
```
SHOW DATABASES/databases;
```
##### Change database 
```
USE <database_name>
```
##### Show tables 
```
SHOW TABLES/tables;
```
##### Showing table structure
```
SHOW COLUMNS FROM <table_name>;
DESCRIBE <table_name>;
```
##### Create Database
```
CREATE DATABASE <database_name>
```
##### Delete Databases
```
DROP DATABASE <database_name>
```

##### Delete table
```
DROP TABLE table_name;
```

##### Use Database
```
USE <database_name>

We must use this command before creating a new table in a database
```
##### Creating a Table
```
CREATE TABLE <table_name> (
column_name(feature_name) data_type if_must_be_filled(NULL or NOT NULL) AUTO_INCREMENT(For IDs),
PRIMARY_KEY(id_var)
);

CREATE TABLE teams_db (
team_id INT NOT NULL AUTO_INCREMENT,
team_name VARCHAR(100) NOT NULL,
PRIMARY_KEY(team_id)
);
```
##### Inserting data into a table
```
INSERT INTO <table_name> (
var_name1, var_nam2, var_nam3)
VALUES(data1, data2, data3);

The string can be inserted using ' ' or " ". doesnot matter.

INSERT INTO team_tbl (
team_name, team_captain, establishment_data)
VALUES('Dronacharya', "Swain Shrestha", NOW()/'2017-12-04');
```

##### See all values of the table
```
SELECT * FROM <table_name>;
```
##### Select specific data from a table
```
SELECT var_name FROM <table_name> [WHERE condition that the data must satisfy]

SELECT team_name FROM team_tbl WHERE team_captain="Swain Shrestha";

Upper case and lower case do not matter by default.
```

##### Comparision Operators
```
> < >= <= !=(<>) =
```

##### Logical Operators
```
AND OR NOT
```

##### Comparion for Special character like NULL
```
IS

SELECT team_name FROM team_tbl WHERE tteam_captain IS NULL;
```

##### Extract year from Date
```
YEAR(NOW());    YEAR(2052-03-10);
```

##### Ordering the table elements
```
SELECT * FROM <table_name> ORDER BY <var_name> ASC/DESC LIMIT <no_of_elements_t display>;

SELECT * FROM team_tbl ORDER BY establishment_date ASC LIMIT 1;
```
##### Using GROUP BY
```
if the table consists of two captains with the same name but with different team names the GROUP BY will show only one person's name.

SELECT * FROM <table_name> GROUP_BY <var_name> ORDER BY <var_name2> ASC;

SELECT * FROM team_tbl GROUP BY team_captain ORDER BY team_name ASC;
```
##### Quering multiple tables
```
SELECT var_name1, var_name2 FROM table1, table2 WHERE table1.var_name3 = table1.var_name3;

SELECT team_name, team_captain, result FROM team_tbl, result_tbl WHERE 
team_tbl.team_id = result_tbl.team_id;
```

##### Deleting everything from the table
```
DELETE FROM <table_name>;
```

##### Deleting with condition
```
DELETE FROM <table_name> where var_name = something;

DELETE FROm team_tbl WHERE team_id = 5;
```
##### Update table
```
UPDATE <table_name> SET field1 = new_value1, field2 = new_value2 [WHERE];

UPDATE team_tbl SET team_captain = "John Subba" WHERE team_name = "Bulls";
```
##### using incomplete variable name to select
```
SELECT var_name1, var_name2 WHERE var_name3 LIKE 'valu%';

SELECT team_id, team_name WHERE team_captain LIKE 'Swa%';
```
##### Using Regex
```
^   matches beginning of the string.
$   matches pattern at the end of the string.
.   Any single character
[...]   Any character listd between the square brackets.
[^]   Any character not listed between the square brackets.
p1|p2|p3  Matches any pattern p1, p2, p3
*   zero or more instances of preceding element
+   one or more instances of preceding element
{n}   n instances of preceding element
{m, n}  m through n instances of preceding element
```
```
SELECT var_name1 FROM table_name WHERE REGEXP '^L';


```



