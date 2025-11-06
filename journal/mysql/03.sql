--? Write SQL commands for:

CREATE TABLE GRADUATE (
    SNO INT PRIMARY KEY,
    NAME VARCHAR(20),
    STIPEND INT,
    SUBJECT VARCHAR(30),
    AVERAGE INT,
    `DIV` INT
);

INSERT INTO GRADUATE VALUES
    (1, 'KARAN', 400, 'PHYSICS', 68, 1),
    (2, 'DIVAKAR', 450, 'COMPUTER SCI', 68, 1),
    (3, 'DIVYA', 300, 'CHEMISTRY', 62, 2),
    (4, 'ARUN', 350, 'PHYSICS', 63, 1),
    (5, 'SABINA', 500, 'MATHS', 70, 1);

CREATE TABLE GUIDE (
    MAINSTREAM VARCHAR(30) PRIMARY KEY,
    ADVISOR VARCHAR(20)
);

INSERT INTO GUIDE VALUES
    ('PHYSICS', 'VINOD'),
    ('CHEMISTRY', 'ALOK'),
    ('MATHS', 'RAJAN'),
    ('COMPUTER SCI', 'MAHESH');

--? 1. List the names of those students who have obtained div 1 sorted by name.
--? 2. Display the report listing name, stipend, subject and amount of stipend received in a year assuming stipend is paid every month.
--? 3. To count the number of students who are either physics or chemistry graduate.
--? 4. To insert a new row.
--? 5. To increase stipend by 100 if div is 1.
--? 6. SELECT NAME, ADVISOR FROM GRADUATE, GUIDE WHERE GRADUATE.SUBJECT=GUIDE.MAINSTREAM;
--? 7. SELECT AVG(STIPEND) FROM GRADUATE WHERE AVERAGE >= 65;

--* 1.
SELECT NAME FROM GRADUATE WHERE `DIV` = 1 ORDER BY NAME;

--* 2.
SELECT NAME, STIPEND, SUBJECT, STIPEND * 12 AS "ANNUAL STIPEND" FROM GRADUATE;

--* 3.
SELECT COUNT(*) AS STUDENT_COUNT FROM GRADUATE WHERE SUBJECT IN ('PHYSICS', 'CHEMISTRY');

--* 4.
INSERT INTO GRADUATE (SNO, NAME, STIPEND, SUBJECT, AVERAGE, `DIV`) VALUES (6, 'NEHA', 380, 'BIOLOGY', 64, 2);

--* 5.
UPDATE GRADUATE SET STIPEND = STIPEND + 100 WHERE `DIV` = 1;

--* 6. Output:
/*
  NAME    | ADVISOR
----------|---------
  KARAN   | VINOD
  DIVAKAR | MAHESH
  DIVYA   | ALOK
  ARUN    | VINOD
  SABINA  | RAJAN
*/

--* 7. Output:
/*
AVG(STIPEND)
------------
   550.0000 
------------
*/
