import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read JSON data into the datastore variable
data = []
for filename in ("data-sample_data-nyctaxi-trips-2009-json_corrigido.json","data-sample_data-nyctaxi-trips-2010-json_corrigido.json", "data-sample_data-nyctaxi-trips-2011-json_corrigido.json", "data-sample_data-nyctaxi-trips-2012-json_corrigido.json"):
    with open('/home/vinicius/Downloads/head/'+filename, 'r') as f:
        print("Lendo arquivo " + filename)
        data = data + f.readlines()

for i, item in enumerate(data):
    data[i] = json.loads(item)

#Use the new datastore datastructure
obj = pd.DataFrame(data)

avg = obj.where(obj["passenger_count"] <= 2)
print("1.What is the average distance traveled by trips with a maximum of 2 passengers;")
print(avg["trip_distance"].mean())


total = obj.groupby(['vendor_id'])['total_amount'].sum()
print("\n==============================================================================\n")
print("2. Which are the 3 biggest vendors based on the total amount of money raised;")
print(total.sort_values(ascending=False).head(3))



print("\n==============================================================================\n")
obj['dropoff_datetime'] = pd.to_datetime(obj['dropoff_datetime'], format='%Y-%m-%dT%H:%M:%S.%f')
obj['month'] = obj['dropoff_datetime'].apply(lambda x : x.month)
obj['year'] = obj['dropoff_datetime'].apply(lambda x : x.year)
obj['payment_type'] = obj['payment_type'].apply(lambda x : x.upper())
resultado = (obj.where(obj["payment_type"] == "CASH")).groupby(['year', 'month']).count()
print("3. Make a histogram of the monthly distribution over 4 years of rides paid with cash;")
print(resultado)
n, bins, patches = plt.hist(resultado['vendor_id'], bins='auto', facecolor='blue', alpha=0.5)
plt.show()


print("\n==============================================================================\n")
print("4. Make a time series chart computing the number of tips each day for the last 3 months of 2012.")
filter1 = obj['month'] == 10
filter2 = obj['month'] == 11
filter3 = obj['month'] == 12
filter4 = obj['year'] == 2012
resultado4 = obj.where((filter1 | filter2 | filter3) & filter4)
res_limpo = resultado4.dropna(how='all')
print(res_limpo)


