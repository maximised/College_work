
DROP DATABASE IF EXISTS students_db;
CREATE DATABASE IF NOT EXISTS students_db;

USE students_db;

CREATE TABLE Sales (
	pid INT,
	timeid INT,
	locid INT,
	sales INT
);


CREATE TABLE Times (
	timeid INT,
	date1 DATE,
	week INT,
	month INT,
	quartier INT,
	year INT
);


CREATE TABLE Locations (
	locid INT,
	region VARCHAR(20),
	country VARCHAR(20)
);

INSERT INTO Sales VALUES (1, 1, 1, 100);
INSERT INTO Sales VALUES (1, 2, 2, 200);
INSERT INTO Sales VALUES (2, 1, 1, 150);
INSERT INTO Sales VALUES (2, 3, 2, 300);

INSERT INTO Times VALUES (1, '2018-2-1', 10, 1, 1, 2018);
INSERT INTO Times VALUES (2, '2018-3-1', 10, 1, 1, 2018);
INSERT INTO Times VALUES (1, '2018-2-1', 10, 1, 1, 2018);
INSERT INTO Times VALUES (3, '2018-12-1', 11, 2, 2, 2018);

INSERT INTO Locations VALUES (1, 'Easter', 'USA');
INSERT INTO Locations VALUES (2, 'Western', 'USA');

SELECT * FROM Sales;
SELECT * FROM Times;
SELECT * FROM Locations;

SELECT SUM(Sales.sales), Locations.region 
FROM Sales, Locations 
WHERE Sales.locid = Locations.locid
GROUP BY Locations.region;

CREATE VIEW SalesP1 AS SELECT * FROM Sales where pid = 1;

UPDATE SalesP1 SET sales = 300 WHERE pid = 2 and sales = 150;

SELECT * FROM SalesP1;

SELECT * FROM Sales;

#SELECT Location.country,  FROM Sales, Locations WHERE Sales.locid = Locations.locid;