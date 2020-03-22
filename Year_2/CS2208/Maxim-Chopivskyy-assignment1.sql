
DROP TABLE IF EXISTS Works cascade;
DROP TABLE IF EXISTS Supervisor cascade;
DROP TABLE IF EXISTS Department cascade;
DROP TABLE IF EXISTS Employee cascade;

# 1.
DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee(
	eid INT,
	ename VARCHAR(50),
	age INT,
	salary INT,
	
	PRIMARY KEY (eid),
	# 3.
	CHECK (salary >= 200)
);



DROP TABLE IF EXISTS Works;
CREATE TABLE  Works(
	eid INT,
	did INT,
	pct_time FLOAT,
	rating FLOAT,
	
	PRIMARY KEY (eid, did),
	# 5.
	CHECK (rating BETWEEN 1 AND 10)
	
	/*
	# 7.
	# CHECK doesn't work so I can't check if this is correct, I used triggers down below
	
	CHECK ((SELECT SUM(pct_time) FROM Works AS W WHERE W.eid = eid) BETWEEN 0 AND 100)
	 */
);

DROP TABLE IF EXISTS Department;
CREATE TABLE IF NOT EXISTS Department(
	did INT,
	budget INT,
	
	PRIMARY KEY (did)
);

DROP TABLE IF EXISTS Supervisor;
CREATE TABLE IF NOT EXISTS Supervisor(
	eid INT,
	supervisor_id INT,
	did INT
	
	/*
	# 6.
	# CHECK doesn't work so I can't check if this is correct, I used triggers down below
	
	CHECK (supervisor_id IN (SELECT eid FROM Employee) AND supervisor_id != eid),
	*/
	
	/*
	# 8.
	# I couldn't check if this code is correct, I used triggers below
	CHECK ((SELECT salary FROM Employee WHERE eid = supervisor_id) > (SELECT salary FROM Employee AS E WHERE E.eid = eid))
	*/
);


ALTER TABLE Works
ADD FOREIGN KEY (eid) REFERENCES Employee(eid);

ALTER TABLE Works
ADD FOREIGN KEY (did) REFERENCES Department(did);

ALTER TABLE Supervisor
ADD FOREIGN KEY (eid) REFERENCES Employee(eid);

ALTER TABLE Supervisor
ADD FOREIGN KEY (supervisor_id) REFERENCES Employee(eid);

ALTER TABLE Supervisor
ADD FOREIGN KEY (did) REFERENCES Department(did);


#########################################################
#############################################################



# 2.
INSERT INTO Employee
VALUES (1, "Ross", 30, 1000);
INSERT INTO Employee
VALUES (2, "Rachel", 29, 500);
INSERT INTO Employee
VALUES (3, "Barry", 30, 700);
INSERT INTO Employee
VALUES (4, "Peter", 32, 1500);
INSERT INTO Employee
VALUES (5, "John", 28, 1700);
INSERT INTO Employee
VALUES (6, "Alex", 33, 2000);

INSERT INTO Department
VALUES (1, 10000);

INSERT INTO Works
VALUES (1, 1, 45, 2);
INSERT INTO Works
VALUES (2, 1, 100, 1);
INSERT INTO Works
VALUES (3, 1, 25, 2);
INSERT INTO Works
VALUES (4, 1, 10, 2);
INSERT INTO Works
VALUES (5, 1, 20, 1);
INSERT INTO Works
VALUES (6, 1, 100, 1);

INSERT INTO Supervisor
VALUES (1, 5, 1);
INSERT INTO Supervisor
VALUES (2, 4, 1);
INSERT INTO Supervisor
VALUES (3, 4, 1);
INSERT INTO Supervisor
VALUES (4, 6, 1);
INSERT INTO Supervisor
VALUES (5, 6, 1);


#####################################################################
#####################################################################


# 4.
DROP TRIGGER IF EXISTS check_rating_insert;
DELIMITER //
CREATE TRIGGER check_rating_insert
BEFORE INSERT ON Works
FOR EACH ROW
BEGIN
	IF new.rating NOT BETWEEN 1 AND 3 THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "New ratings should be between 1 and 3";
	END IF;
END; //
DELIMITER ;


#################################################################
#################################################################


# 6.
DROP TRIGGER IF EXISTS super_is_employee_insert;
DELIMITER //
CREATE TRIGGER super_is_employee_insert
BEFORE INSERT ON Supervisor
FOR EACH ROW
BEGIN
	IF new.supervisor_id NOT IN 
	(SELECT eid FROM Employee)THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Supervisor is not an employee";
	END IF;
END; //
DELIMITER ;

DROP TRIGGER IF EXISTS super_is_employee_update;
DELIMITER //
CREATE TRIGGER super_is_employee_update
BEFORE UPDATE ON Supervisor
FOR EACH ROW
BEGIN
	IF new.supervisor_id NOT IN 
	(SELECT eid FROM Employee)THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Supervisor is not an employee";
	END IF;
END; //
DELIMITER ;


#########################################################################
#########################################################################


# 7.
DROP TRIGGER IF EXISTS check_pct_insert;
DELIMITER //
CREATE TRIGGER check_pct_insert
AFTER INSERT ON Works
FOR EACH ROW
BEGIN
	IF (SELECT SUM(pct_time) FROM Works WHERE eid = new.eid) NOT BETWEEN 0 AND 100 THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Total percent of time should be between 0 and 100%";
	END IF;
END; //
DELIMITER ;

DROP TRIGGER IF EXISTS check_pct_update;
DELIMITER //
CREATE TRIGGER check_pct_update
AFTER UPDATE ON Works
FOR EACH ROW
BEGIN
	IF (SELECT SUM(pct_time) FROM Works WHERE eid = new.eid) NOT BETWEEN 0 AND 100 THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Total percent of time should be between 0 and 100%";
	END IF;
END; //
DELIMITER ;


####################################################################
####################################################################

# 8.
DROP TRIGGER IF EXISTS salary_insert_super;
DELIMITER //
CREATE TRIGGER salary_insert_super
BEFORE INSERT ON Supervisor
FOR EACH ROW
BEGIN
	IF (SELECT salary FROM Employee AS E WHERE E.eid = new.supervisor_id) 
		<= (SELECT salary FROM Employee AS E WHERE E.eid = new.eid) THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Supervisors salary should be above supervisees salary";
	END IF;
END; //
DELIMITER ;


DROP TRIGGER IF EXISTS salary_update_super;
DELIMITER //
CREATE TRIGGER salary_update_super
BEFORE UPDATE ON Supervisor
FOR EACH ROW
BEGIN
	IF (SELECT salary FROM Employee AS E WHERE E.eid = new.supervisor_id) 
		<= (SELECT salary FROM Employee AS E WHERE E.eid = new.eid) THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Supervisors salary should be above supervisees salary";
	END IF;
END; //
DELIMITER ;


DROP TRIGGER IF EXISTS salary_update_employee;
DELIMITER //
CREATE TRIGGER salary_update_employee
BEFORE UPDATE ON Employee
FOR EACH ROW
BEGIN
	IF ((new.salary) <= (SELECT MAX(salary) FROM Employee WHERE eid IN (SELECT eid FROM Supervisor WHERE supervisor_id = new.eid)))
		OR
	   ((new.salary) >= (SELECT MIN(salary) FROM Employee WHERE eid IN (SELECT supervisor_id FROM Supervisor WHERE eid = new.eid)))
	   THEN
		SIGNAL SQLSTATE "45000"
		SET MESSAGE_TEXT = "Supervisors salary should be above supervisees salary";
	END IF;
END; //
DELIMITER ;


##############################################################
##############################################################


# 9.
DROP TRIGGER IF EXISTS increase_salary;
DELIMITER //
CREATE TRIGGER increase_salary
BEFORE UPDATE ON Works
FOR EACH ROW
BEGIN
	IF new.rating >= old.rating+1 THEN
		UPDATE Employee
		SET salary = salary*1.1
		WHERE eid = new.eid;
	END IF;
END; //
DELIMITER ;


#########################################################################
#########################################################################


# 10.
DROP VIEW IF EXISTS MANAGER_SALARY;
DELIMITER //
CREATE VIEW MANAGER_SALARY(ename, salary, did) AS
SELECT ename, salary, did 
FROM Employee NATURAL JOIN Works 
WHERE (eid, did) NOT IN
(
	SELECT eid, did 
	FROM Supervisor 
	ORDER BY did
)
ORDER BY did
 //
DELIMITER ;


###################################################################
################################################################


# 11.
#finds lowest in rating
/*
DROP PROCEDURE IF EXISTS lowest_ranked;
DELIMITER //
CREATE PROCEDURE lowest_ranked(IN dept_id INT)
BEGIN
	SELECT E.eid, E.ename, W.did, W.rating
	FROM Employee AS E JOIN Works AS W
	ON E.eid = W.eid AND W.did = dept_id
	WHERE E.eid IN
	(
		SELECT eid FROM Works
		WHERE (rating, did) IN
		(
			SELECT MIN(rating), did
			FROM Works
			WHERE did = dept_id
		)
	);
END //
DELIMITER ;
*/

# finds employees with no supervisees(lowest in hierarchy)
DROP PROCEDURE IF EXISTS lowest_ranked;
DELIMITER //
CREATE PROCEDURE lowest_ranked(IN dept_id INT)
BEGIN
	SELECT * FROM Employee
	WHERE eid IN
	(
		SELECT eid
		FROM Works
		WHERE eid NOT IN
		(
			SELECT supervisor_id FROM Supervisor WHERE did = dept_id
		)
	AND did = dept_id
	);
END //
DELIMITER ;

##########################################################
##########################################################


# 12.
DROP VIEW IF EXISTS MINIMUM_PCT_TIME;
DELIMITER //
CREATE VIEW MINIMUM_PCT_TIME(ename, min_pct_time) AS
SELECT E.ename, MIN(pct_time)
FROM Works AS W JOIN Employee AS E
ON W.eid = E.eid
GROUP BY W.eid
ORDER BY W.eid;

 //
DELIMITER ;




########################################################################
########################################################################



# Code for testing
/*
SELECT * FROM Employee;
SELECT * FROM Supervisor;
SELECT * FROM Works;
SELECT * FROM Department;


INSERT INTO Employee
VALUES (11,'Dan', 25, 200);
INSERT INTO Employee
VALUES (12, 'con', 30, 230);
INSERT INTO Employee
VALUES (13, 'david', 40, 230);
INSERT INTO Employee
VALUES (14, 'vanellope', 21, 300);

INSERT INTO Works
VALUES (11, 20, 0.3, 1);
INSERT INTO Works
VALUES (12, 21, 0.4, 3);
INSERT INTO Works
VALUES (13, 21, 0.5, 3);
INSERT INTO Works
VALUES (14, 21, 0.4, 2);
INSERT INTO Works
VALUES (11, 21, 0.5, 2);
INSERT INTO Works
VALUES (1, 20, 55, 2);
INSERT INTO Works
VALUES (1, 21, 1, 2);


INSERT INTO Department
VALUES (20, 200000);
INSERT INTO Department
VALUES (21, 300000);

INSERT INTO Supervisor
VALUES (11, 12, 21);
INSERT INTO Supervisor
VALUES (1, 12, 20);
INSERT INTO Supervisor
VALUES (1, 13, 21);
INSERT INTO Supervisor
VALUES (6, 1, 1);


UPDATE Works
SET rating = rating + 1
WHERE eid = 1 AND did = 1;
UPDATE Works
SET pct_time = 45
WHERE eid = 1 AND did = 1;

UPDATE Supervisor
SET supervisor_id = 6
WHERE eid = 1 AND did = 1;

UPDATE Employee
SET salary = 2050
WHERE eid = 1;

DELETE FROM Employee;
DELETE FROM Works;
DELETE FROM Supervisor;
DELETE FROM Department;


DESCRIBE Employee;
DESCRIBE Works;
DESCRIBE Supervisor;
DESCRIBE Department;


SELECT * FROM MANAGER_SALARY;
SELECT * FROM MINIMUM_PCT_TIME;
CALL lowest_ranked(1);

SELECT W.eid, MIN(pct_time), E.ename
FROM Works AS W JOIN Employee AS E
ON W.eid = E.eid
GROUP BY W.eid
ORDER BY eid;
*/