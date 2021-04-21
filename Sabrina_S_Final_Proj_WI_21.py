import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import seaborn as sns
import matplotlib.image as mpimg

nyc_bnb = pd.read_csv("AB_NYC_2019.csv")
#print(nyc_bnb)
print(nyc_bnb['longitude'])
#finding range of longitude and latitude so graph will fit right
max_long = nyc_bnb['longitude'].max()
print("max longitude is:", max_long)
max_lat = nyc_bnb['latitude'].max()
print("max latitude is:", max_lat)

min_long = nyc_bnb['longitude'].min()
print("min longitude is:", min_long)
min_lat = nyc_bnb['latitude'].min()
print("min latitude is:", min_lat)

#using the nyc map provided in the data set
fig_1 = plt.figure(figsize=(10,8))
nyc_map = mpimg.imread("New_York_City_2.png")
plt.imshow(nyc_map, zorder = 0, extent = [-74.258, -73.7, 40.49,40.92])
ax = plt.gca()
nyc_bnb.plot( kind = 'scatter', zorder = 2, x='longitude', y = 'latitude', ax = ax)
plt.tight_layout()

#Getting rid of 0 values in Reviews 
rid_empty_reviews = nyc_bnb[nyc_bnb.number_of_reviews != 0]

fig_2 = plt.figure(figsize=(10,8))
nyc_map = mpimg.imread("New_York_City_2.png")
plt.imshow(nyc_map, zorder = 0, extent = [-74.258, -73.7, 40.49,40.92])
ax = plt.gca()
rid_empty_reviews.plot( kind = 'scatter', zorder = 2, x='longitude', y = 'latitude', c = 'number_of_reviews', ax = ax, cmap=plt.get_cmap('Dark2'), alpha = 0.9, figsize=(10,8))
plt.tight_layout()
plt.show()

#Finding area with highest concentration of above average reviews
rev_m = np.mean(rid_empty_reviews['number_of_reviews'])
print(rev_m)

unique_hood = set(nyc_bnb['neighbourhood'])

above_av = nyc_bnb.loc[nyc_bnb.number_of_reviews > 100]
fig_3 = plt.figure(figsize=(10,8))
sns.boxplot(x = 'number_of_reviews', y = 'neighbourhood', data = above_av,)

plt.xticks(rotation = 45)
plt.show()

top_5_hood = nyc_bnb.loc[(nyc_bnb['neighbourhood'] == 'East Elmhurst') | (nyc_bnb['neighbourhood'] == 'Jamaica') | (nyc_bnb['neighbourhood'] == 'Richmond Hill') | (nyc_bnb['neighbourhood'] == 'Springfield Gardens') | (nyc_bnb['neighbourhood'] == 'Tribeca')]
bnb_heat = top_5_hood.groupby('neighbourhood').number_of_reviews.value_counts().unstack().fillna(0)
fig_4 = plt.figure()
sns.heatmap(bnb_heat, cmap="Blues", annot = True)
plt.xticks(rotation = 45)
plt.show()

#Finding what to price BnB at in Tribeca
BnB_TB = nyc_bnb.loc[(nyc_bnb['neighbourhood'] == 'Tribeca')]
Tri_heat = BnB_TB.groupby('room_type').price.value_counts().unstack().fillna(0)
fig_5 = plt.figure()
sns.heatmap(Tri_heat.T, cmap="BuPu" )
plt.xticks(rotation = 45)
plt.show()
#Entire home/apt, < 1200

#How many days would people stay at a place priced over 1000?
d_1000 = nyc_bnb['minimum_nights'].value_counts()
print(d_1000)

fig_6 = plt.figure()
BnB_greater_than_100 = nyc_bnb.loc[(nyc_bnb['price'] > 799) & (nyc_bnb['neighbourhood'] == 'Tribeca')]
sns.countplot(data = BnB_greater_than_100, x = 'minimum_nights')

plt.xticks(rotation = 45)
plt.show()
#best choice is 30 nights 

#Who should host the BnB
fig_7 = plt.figure()
host_with_most = nyc_bnb.loc[(nyc_bnb['neighbourhood'] == 'Tribeca')]
sns.scatterplot(data= host_with_most, x = 'host_name', y= 'calculated_host_listings_count')
plt.xticks(rotation = 45)
plt.show()
#BlueGround