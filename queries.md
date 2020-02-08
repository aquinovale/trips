# DDL 

CREATE EXTERNAL TABLE `sample`(
  `vendor_id` string COMMENT 'from deserializer', 
  `pickup_datetime` string COMMENT 'from deserializer', 
  `dropoff_datetime` string COMMENT 'from deserializer', 
  `passenger_count` int COMMENT 'from deserializer', 
  `trip_distance` decimal(38,18) COMMENT 'from deserializer', 
  `pickup_longitude` double COMMENT 'from deserializer', 
  `pickup_latitude` double COMMENT 'from deserializer', 
  `rate_code` int COMMENT 'from deserializer', 
  `store_and_fwd_flag` int COMMENT 'from deserializer', 
  `dropoff_longitude` double COMMENT 'from deserializer', 
  `dropoff_latitude` double COMMENT 'from deserializer', 
  `payment_type` string COMMENT 'from deserializer', 
  `fare_amount` decimal(38,18) COMMENT 'from deserializer', 
  `surcharge` decimal(38,18) COMMENT 'from deserializer', 
  `tolls_amount` decimal(38,18) COMMENT 'from deserializer', 
  `total_amount` decimal(38,18) COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
LOCATION
  's3://viniciusvale/sample'
TBLPROPERTIES (
  'has_encrypted_data'='false', 
  'transient_lastDdlTime'='1581035082')


# Minimum Requirements Techniques

1.What is the average distance traveled by trips with a maximum of 2 passengers;

SELECT avg(trip_distance) FROM sample
WHERE passenger_count <= 2;

2. Which are the 3 biggest vendors based on the total amount of money raised;

SELECT vendor_id, sum(total_amount) FROM sample
GROUP BY vendor_id
ORDER BY sum(total_amount) DESC;


3. Make a histogram of the monthly distribution over 4 years of rides paid with cash;

SELECT extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)), count(payment_type)  FROM sample 
WHERE upper(payment_type) = 'CASH' 
GROUP BY extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime))
ORDER BY extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)) DESC;


4. Make a time series chart computing the number of tips each day for the last 3 months of 2012.

I don't understood this question, so I can have wrong

SELECT extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)), extract(MONTH FROM from_iso8601_timestamp(dropoff_datetime)), count(*)  FROM sample 
WHERE extract(MONTH FROM from_iso8601_timestamp(dropoff_datetime)) IN (10,11,12) AND extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)) = 2012
GROUP BY extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)), extract(MONTH FROM from_iso8601_timestamp(dropoff_datetime))
ORDER BY extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)), extract(MONTH FROM from_iso8601_timestamp(dropoff_datetime));



# Bonus

1 - What is the average trip time on Saturdays and Sundays;

SELECT avg(trip_distance)  FROM sample 
WHERE extract(DOW FROM from_iso8601_timestamp(dropoff_datetime)) IN (0,6) 


2 - Make a latitude and longitude map view of pickups and dropoffs in the year 2010;

SELECT pickup_latitude, pickup_longitude, dropoff_latitude, dropoff_longitude  FROM sample 
WHERE extract(YEAR FROM from_iso8601_timestamp(dropoff_datetime)) = 2010


3 - Simulate JSON data streaming and view using a real-time metric with the Trips Data;
I don't understood this question.

4 - To be able to provision your entire environment in a public cloud, preferably AWS.

S3-------->Athena--------->QuickSight


