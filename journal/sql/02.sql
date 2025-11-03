--? Write MySQL queries for questions 1 to 6, and give the output for questions 7 and 8 based on the Table SHOP, shown below.

CREATE TABLE SHOP (
    NO INT PRIMARY KEY,
    SHOPNAME VARCHAR(30),
    SALE INT,
    AREA VARCHAR(15),
    C_PERC FLOAT(3, 1),
    RATING CHAR(1),
    CITY VARCHAR(20)
);

INSERT INTO SHOP VALUES
    (1, 'S.M. Sons', 250000, 'West', 68.6, 'C', 'Delhi'),
    (2, 'Dharohar', 500000, 'South', 81.8, 'A', 'Mumbai'),
    (3, 'Kriti Art', 300000, 'North', 79.8, 'B', 'Kolkatta'),
    (4, 'Ripple', 380000, 'North', 88.0, 'B', 'Mumbai'),
    (5, 'Best Stores', 456000, 'East', NULL, 'A', 'Delhi'),
    (6, 'Crystal', 290000, 'South', 66.7, 'A', 'Kolkatta');

--? 1. Show all the names of all shops which are in the area ‘South’ and c_perc < 75.
--? 2. To display names of cities that and end with the letter ‘i’ and have the letter ‘l’ as the 3rd character.
--? 3. To display a list of all the shops with sale > 300000 in descending order of shopname.
--? 4. To display shopname, area and rating for only those shops whose sale is between 350000 and 400000 (including both values).
--? 5. To display the shops whose rating is A.
--? 6. To display name of the shop whose c_perc is unknown.
--? 7. SELECT shopname, city FROM SHOP WHERE city IN ("Mumbai", "Delhi");
--? 8. SELECT shopname, "is in", city FROM SHOP WHERE shopname NOT LIKE "%t_r%";

--* 1.
SELECT SHOPNAME FROM SHOP WHERE AREA = 'South' AND C_PERC < 75;

--* 2.
SELECT CITY FROM SHOP WHERE CITY LIKE '__l%i';

--* 3.
SELECT * FROM SHOP WHERE SALE > 300000 ORDER BY SHOPNAME DESC;

--* 4.
SELECT SHOPNAME, AREA, RATING FROM SHOP WHERE SALE BETWEEN 350000 AND 400000;

--* 5.
SELECT * FROM SHOP WHERE RATING = 'A';

--* 6.
SELECT SHOPNAME FROM SHOP WHERE C_PERC IS NULL;

--* 7. Output:
/*
  shopname    | city   
--------------|---------
| S.M. Sons   | Delhi  |
| Dharohar    | Mumbai |
| Ripple      | Mumbai |
| Best Stores | Delhi  |
*/

--* 8. Output:
/*
 shopname | is in | city
-----------------------------
S.M. Sons | is in | Delhi   
Dharohar  | is in | Mumbai  
Kriti Art | is in | Kolkatta
Ripple    | is in | Mumbai  
Crystal   | is in | Kolkatta
*/
