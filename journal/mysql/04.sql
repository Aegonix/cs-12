--? Write SQL commands for:

CREATE TABLE STATIONARY (
    S_ID VARCHAR(10) PRIMARY KEY,
    STATIONARYNAME VARCHAR(30),
    COMPANY VARCHAR(20),
    PRICE INT
);

INSERT INTO STATIONARY VALUES
    ('Dp01', 'Dot Pen', 'Abc', 10),
    ('Pl02', 'Pencil', 'Xyz', 6),
    ('Er05', 'Eraser', 'Xyz', 7),
    ('Pl01', 'Pencil', 'Cam', 5);

CREATE TABLE CONSUMER (
    C_ID INT PRIMARY KEY,
    CONSUMERNAME VARCHAR(30),
    ADDRESS VARCHAR(30),
    S_ID VARCHAR(10)
);

INSERT INTO CONSUMER VALUES
    (01, 'Good Learner', 'Delhi', 'Pl01'),
    (06, 'Write Well', 'Mumbai', 'Er05'),
    (12, 'Topper', 'Delhi', 'Dp01');

--? 1. To display the details of those consumers whose address is "delhi".
--? 2. To display the details of stationary whose price is in the range 8 to 15 both inclusive.
--? 3. To increase the price of all stationary by 2.
--? 4. To display the consumername, address from table consumer and company and price from table stationary, with their corresponding matching s_id
--? 5. To delete all rows from stationary where company is xyz.
--? 6. To add a new column state in table consumer.
--? 7. SELECT DISTINCT ADDRESS FROM CONSUMER;
--? 8. SELECT COMPANY, MAX(PRICE), MIN(PRICE), COUNT(*) FROM STATIONARY GROUP BY COMPANY;

--* 1.
SELECT * FROM CONSUMER WHERE ADDRESS = 'Delhi';

--* 2.
SELECT * FROM STATIONARY WHERE PRICE BETWEEN 8 AND 15;

--* 3.
UPDATE STATIONARY SET PRICE = PRICE + 2;

--* 4.
SELECT CONSUMER.CONSUMERNAME, CONSUMER.ADDRESS, STATIONARY.COMPANY, STATIONARY.PRICE FROM CONSUMER, STATIONARY WHERE CONSUMER.S_ID = STATIONARY.S_ID;

--* 5.
DELETE FROM STATIONARY WHERE COMPANY = 'xyz';

--* 6.
ALTER TABLE CONSUMER ADD STATE VARCHAR(20);

--* 7. Output:
/*
  ADDRESS
-----------
  Delhi
  Mumbai
*/

--* 8. Output:
/*
  COMPANY | MAX(PRICE) | MIN(PRICE) | COUNT(*)
----------|------------|------------|----------
  Abc     |         12 |         12 |        1
  Cam     |          7 |          7 |        1
*/