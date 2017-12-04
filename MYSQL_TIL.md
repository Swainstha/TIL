# December 4, 2017

###### Terminologies
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
```



```
