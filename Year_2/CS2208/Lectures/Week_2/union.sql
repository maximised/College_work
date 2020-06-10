DROP DATABASE IF EXISTS test_db;
CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE S1 (
	sid INT,
	sname VARCHAR(50),
	rating INT,
	age FLOAT
);

CREATE TABLE S2 (
	sid INT,
	sname VARCHAR(50),
	rating INT,
	age FLOAT
);

INSERT INTO S1 VALUES (22, 'dustin', 7, 45.0);
INSERT INTO S1 VALUES (31, 'lubber', 8, 55.5);
INSERT INTO S1 VALUES (58, 'lubber', 10, 35.0);


INSERT INTO S2 VALUES (28, 'yuppy',  9,  35.0);
INSERT INTO S2 VALUES (31, 'lubber', 8,  55.5);
INSERT INTO S2 VALUES (44, 'guppy',  5,  35.0);
INSERT INTO S2 VALUES (58, 'rusty',  10, 35.0);



SELECT * from S1;
SELECT * from S2;

(SELECT * FROM S1) UNION (SELECT * FROM S2);
