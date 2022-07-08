SELECT * 
FROM information_schema.tables
WHERE table_schema = 'world' 
    AND table_name = 'city'
LIMIT 1;

-- order table
SELECT * FROM city
   ORDER BY NAME;

DELETE FROM city
WHERE ID = 6;

-- delete table
DROP TABLE country;

-- update table
UPDATE city
SET District = 'Pune'
WHERE ID = 6;

-- join two tables
SELECT ID, NAME, AGE, AMOUNT
   FROM country, city
   WHERE  country.ID = city.CUSTOMER_ID;


Use world; 

Insert into city ( 

   Name, 
   CountryCode,
   District,
   Population
)
Values (

  'Taran', 
  'IDN',
  'Mumbai',
  '50000'
)




