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
plt.figure(figsize=(10,8))
nyc_map = mpimg.imread("New_York_City_2.png")
plt.imshow(nyc_map, zorder = 0, extent = [-74.258, -73.7, 40.49,40.92])
ax = plt.gca()
nyc_bnb.plot( kind = 'scatter', zorder = 2, x='longitude', y = 'latitude', ax = ax)
plt.tight_layout()
plt.show()