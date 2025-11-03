--? Write MySQL queries for the questions 1 to 6 and give outputs for SQL queries 7 to 8, based on Table PASSENGERS shown below:

CREATE TABLE PASSENGERS (
    PNO INT PRIMARY KEY,
    NAME VARCHAR(20),
    TNO INT,
    CLASS VARCHAR(20),
    SEATNO INT,
    AGE INT,
    FARE INT
);

INSERT INTO PASSENGERS VALUES
    (1, 'ANU', 1101, 'II', 11, 25, 700),
    (2, 'SAGAR', 1103, 'AC-CHAIR', 34, 43, 1300),
    (3, 'SAMIR', 2019, 'AC-I', 78, 18, 900),
    (4, 'GAURAV', 2011, 'II', 23, 17, 700),
    (5, 'KRIPAL', 1893, 'I', 3, 25, 1700),
    (6, 'ANKUR', 1101, 'II', 6, 20, 500),
    (7, 'PRIYA', 3012, 'AC-II', 2, 11, 1200);

--? 1. To display the name and seat no. where class is II and age is more than 18.
--? 2. To display trainno and class where the fare is between 900 and 1300.
--? 3. To display the list of passengers in ascending order of age.
--? 4. To display a column NEWFARE showing new FARE by increasing FARE by 10%.
--? 5. Insert a new row in the above table with the details (9,Ajay,2011,II,19,20,500).
--? 6. Display all records in the table as strings to display NAME is AGE years old.
--? 7. SELECT TNO, NAME FROM PASSENGERS WHERE FARE<1200 ORDER BY FARE, NAME DESC;
--? 8. UPDATE PASSENGERS SET FARE=FARE-50 WHERE NAME LIKE ‘_R%A’;

--* 1.
SELECT NAME, SEATNO FROM PASSENGERS WHERE CLASS = 'II' AND AGE > 18;

--* 2.
SELECT TNO, CLASS FROM PASSENGERS WHERE FARE BETWEEN 900 AND 1300;

--* 3.
SELECT * FROM PASSENGERS ORDER BY AGE;

--* 4.
SELECT *, FARE * 1.1 AS NEWFARE FROM PASSENGERS;

--* 5.
INSERT INTO PASSENGERS (PNO, NAME, TNO, CLASS, SEATNO, AGE, FARE) VALUES (9, 'Ajay', 2011, 'II', 19, 20, 500);

--* 6.
SELECT NAME, "is", AGE, "years old." FROM PASSENGERS;

--* 7. Output:
/*
 TNO | NAME
-----|-------
1101 | ANKUR 
2011 | Ajay  
2011 | GAURAV
1101 | ANU   
2019 | SAMIR
*/

--* 8. Output:
/*
Before UPDATE:
 PNO | NAME  | FARE
-----|-------|-----
   7 | PRIYA | 1200

After UPDATE:
 PNO | NAME  | FARE
-----|-------|-----
   7 | PRIYA | 1150
*/