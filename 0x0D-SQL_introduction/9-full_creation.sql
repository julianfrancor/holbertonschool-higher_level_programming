-- script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows. The database name will be passed as an argument to the mysql command.
-- If the table second_table already exists, your script should not fail
-- You are not allowed to use the SELECT and SHOW statements
-- cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- create the table
CREATE TABLE IF NOT EXISTS second_table
    (id INT, name VARCHAR(256), score INT);
-- fill the table
INSERT INTO second_table VALUES
    (1, 'Jhon', 10),
    (1, 'Alex', 3),
    (1, 'Bob', 14),
    (1, 'George', 8);
