DROP DATABASE IF EXISTS students_db;
CREATE DATABASE IF NOT EXISTS students_db;

USE students_db;

DROP TABLE IF EXISTS Students, Enrolled;


CREATE TABLE Students (
	sid VARCHAR(10),
	name VARCHAR(45),
	login VARCHAR(45),
	age INT,
	gpa DECIMAL(2), 
	PRIMARY KEY (sid)
);

CREATE TABLE Enrolled (
	sid VARCHAR(10),
	cid VARCHAR(45),
	grade VARCHAR(2),
	PRIMARY KEY (sid, cid)
);


INSERT INTO Students VALUES('53666', 'Jones','jones@cs', 18, 3.4);
INSERT INTO Students VALUES('53688', 'Smith','smith@eecs', 18, 3.2);
INSERT INTO Students VALUES('53650', 'Smith','smith@math', 19, 3.8);


INSERT INTO Enrolled VALUES('53831', 'Carnatic101', 'C');
INSERT INTO Enrolled VALUES('53831', 'Reggae203', 'B');
INSERT INTO Enrolled VALUES('53650', 'Topology112', 'A');
INSERT INTO Enrolled VALUES('53666', 'History105', 'B');


/*DROP TABLE Enrolled;*/

/*SELECT * FROM Students;
SELECT * FROM Enrolled;*/

/*
SELECT S.name, S.age, E.grade FROM Students S, Enrolled E
WHERE S.sid = E.sid AND S.age < 21;

*/

CREATE VIEW YoungActiveStudents(sid, name, grade, age) AS
SELECT S.sid, S.name, E.grade, S.age FROM Students S, Enrolled E
WHERE S.sid = E.sid AND S.age < 21;

/*SELECT * FROM YoungActiveStudents;*/

CREATE VIEW YoungStudents(sid, name, age) AS
SELECT Students.sid, Students.name, Students.age  FROM Students
WHERE Students.age < 21;


/*Select * from YoungStudents;*/

SELECT * from YoungActiveStudents;
/*
SELECT * FROM Students;
*/

UPDATE YoungStudents SET age = 15 WHERE sid = '53650';
SELECT * FROM Students;
SELECT * FROM Enrolled;

UPDATE YoungActiveStudents SET grade = 'F' WHERE sid = '53650';
/*
SELECT * FROM Students;
SELECT * FROM YoungActiveStudents;
SELECT * FROM YoungActiveStudents where grade > 'A';

SELECT S.sid, S.name, E.grade, S.age FROM Students S, Enrolled E
WHERE S.sid = E.sid AND S.age < 21 and E.grade > 'A';
*/

/*
INSERT INTO YoungActiveStudents (sid, name, grade, age) VALUES ('55111', 'Peter', 'A', 18);
*/
/*DROP TABLE Students;*/
/*
SELECT * FROM YoungActiveStudents;
*/
/*SELECT * FROM Enrolled;*/

INSERT INTO Students (sid, name, login, age) VALUES('53652', 'Peter','peter@cs', 19);
/*
SELECT * FROM STUDENTS;
*/


DROP VIEW YoungActiveStudents ;
CREATE VIEW YoungActiveStudents(sid, name, grade, age) AS
SELECT S.sid, S.name, E.grade, S.age FROM Students S, Enrolled E
WHERE S.sid = E.sid AND S.age < 21
WITH CHECK OPTION;



/*INSERT INTO Students (sid, name, login, age) VALUES('53653', 'Peter','peter@cs', 33);*/
UPDATE YoungActiveStudents SET age = 28 WHERE sid = '53650';
SELECT * FROM STUDENTS;


CREATE VIEW YearAvg AS SELECT S.year, AVG (S.gpa) FROM Students S GROUP BY S.YEAR;

SELECT * FROM YearAvg;
