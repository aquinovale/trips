# É necessário instalar os pacotes do python com o pip

import json

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Execução --- testado no python 3.7

python exercicio1.py


# Arquivos 

data-sample_data-nyctaxi-trips-2009-json_corrigido.json
data-sample_data-nyctaxi-trips-2010-json_corrigido.json
data-sample_data-nyctaxi-trips-2011-json_corrigido.json
data-sample_data-nyctaxi-trips-2012-json_corrigido.json


# Saída esperada

Lendo arquivo data-sample_data-nyctaxi-trips-2009-json_corrigido.json
Lendo arquivo data-sample_data-nyctaxi-trips-2010-json_corrigido.json
1.What is the average distance traveled by trips with a maximum of 2 passengers;
2.6625269962033875

==============================================================================

2. Which are the 3 biggest vendors based on the total amount of money raised;
vendor_id
CMT    9.774542e+06
VTS    9.521717e+06
DDS    1.357451e+06
Name: total_amount, dtype: float64

==============================================================================

3. Make a histogram of the monthly distribution over 4 years of rides paid with cash;
              dropoff_datetime  dropoff_latitude    ...      trip_distance  vendor_id
year   month                                        ...                              
2009.0 1.0               66812             66812    ...              66812      66812
       2.0               66680             66680    ...              66680      66680
       3.0               73943             73943    ...              73943      73943
       4.0               71142             71142    ...              71142      71142
       5.0               74152             74152    ...              74152      74152
       6.0               71346             71346    ...              71346      71346
       7.0               74072             74072    ...              74072      74072
       8.0               74022             74022    ...              74022      74022
       9.0               71508             71508    ...              71508      71508
       10.0              74014             74014    ...              74014      74014
       11.0              71417             71417    ...              71417      71417
       12.0              21605             21605    ...              21605      21605
2010.0 1.0               66172             66172    ...              66172      66172
       2.0               66830             66830    ...              66830      66830
       3.0               73616             73616    ...              73616      73616
       4.0               71076             71076    ...              71076      71076
       5.0               73665             73665    ...              73665      73665
       6.0               70984             70984    ...              70984      70984
       7.0               73483             73483    ...              73483      73483
       8.0               73365             73365    ...              73365      73365
       9.0               71115             71115    ...              71115      71115
       10.0              73642             73642    ...              73642      73642
       11.0              70881             70881    ...              70881      70881
       12.0              25884             25884    ...              25884      25884

[24 rows x 17 columns]

==============================================================================

4. Make a time series chart computing the number of tips each day for the last 3 months of 2012.
Empty DataFrame
Columns: [dropoff_datetime, dropoff_latitude, dropoff_longitude, fare_amount, passenger_count, payment_type, pickup_datetime, pickup_latitude, pickup_longitude, rate_code, store_and_fwd_flag, surcharge, tip_amount, tolls_amount, total_amount, trip_distance, vendor_id, month, year]
Index: []



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

S3----->Athena------->Quicksigth
