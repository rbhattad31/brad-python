SELECT * FROM city;
ALTER TABLE city
ADD Place VARCHAR(200);

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