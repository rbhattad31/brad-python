USE world;
SHOW TABLES LIKE "city";
SELECT COUNT(*)
FROM information_schema.tables 
WHERE table_schema = DATABASE()
AND table_name = "city";

CREATE TABLE IF NOT EXISTS customer_data (
    customerId INT ,
    customerName VARCHAR(255),
    customerPlace VARCHAR(255)
);