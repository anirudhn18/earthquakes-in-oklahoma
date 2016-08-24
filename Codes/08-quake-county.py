from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('ggplot')

#read in both drilling data and earthquakes
earth_ok = pd.read_csv("../Files/processed-data/completeEarthquakeFreq.csv", index_col = 1,parse_dates = [1])
drill_ok = pd.read_csv("../Files/processed-data/well_header.csv", parse_dates=['SPUDDATE'])

earth_last10 = earth_ok['2005':]
drill_last10 = drill_ok[drill_ok['SPUDDATE']>datetime(2005,1,1)][['SPUDDATE','COUNTY']]

#Changing data format

#group both datasets by county
num_per_county = drill_ok.groupby('COUNTY')
sorted_counties_wells = num_per_county.size().sort_values(ascending=False)
num_last10 = drill_last10.groupby('COUNTY')
counties_last10 = num_last10.size().sort_values(ascending=False)

earth_county = earth_ok.groupby('county')
num_quakes_county = earth_county.size().sort_values(ascending=False)

elast_county = earth_last10.groupby('county')
num_quakes_last = elast_county.size().sort_values(ascending=False)

#overall top 100
greater_than_100 = num_quakes_county[num_quakes_county > 100]
average_intensity_values = earth_county.max_mmi.mean().sort_values(ascending = False)[greater_than_100.index]

#last 10 years
greater_last10 = num_quakes_last[num_quakes_last > 100]
average_intensity_last10 = elast_county.max_mmi.mean().sort_values(ascending = False)[greater_last10.index]

#earthquake and  wells
sorted_counties_wells_earth = num_per_county.size().sort_values(ascending=False)[greater_than_100.index]
sorted_wellCount_last10 = num_last10.size().sort_values(ascending=False)[greater_last10.index]

greater_than_100.plot.bar()
plt.title('Counties with more than 100 Earthquakes')
plt.xlabel('Counties')
plt.savefig('../Plots/counties-gt100eq.png')

#average_intensity_values =  average_intensity_values.sort(ascending=False,inplace=False)
plt.figure(2)
average_intensity_values.plot.bar()
plt.title('Average Intensity per County')
plt.xlabel('Counties')
plt.savefig('../Plots/intensity-per-county.png')

#sorted_counties_wells_earth =  sorted_counties_wells_earth.sort(ascending=False,inplace=False)
plt.figure(3)
sorted_counties_wells_earth.plot.bar()
plt.title('Counties with more than 100 Earthquakes as Index, Wells per county')
plt.xlabel('Counties')
plt.savefig('../Plots/wells-per-county-gt100eq.png')


################################################################################
plt.figure(4)
greater_last10.plot.bar()
plt.title('Counties with more than 100 Earthquakes last 10 Years')
plt.xlabel('Counties')
plt.savefig('../Plots/last10yrs-gt100eq.png')

#average_intensity_last10= average_intensity_last10.sort(ascending=False,inplace=False)
plt.figure(5)
average_intensity_last10.plot.bar()
plt.title('Average Intensity per County last 10 years')
plt.xlabel('Counties')
plt.savefig('../Plots/last10yrs-intensity-per-county.png')


#sorted_wellCount_last10= sorted_wellCount_last10.sort(ascending=False,inplace=False)
plt.figure(6)
sorted_wellCount_last10.plot.bar()
plt.title('Counties with more than 100 Earthquakes as Index, Wells per county last 10 years')
plt.xlabel('Counties')
plt.savefig('../Plots/last10yrs-wells-per-county-gt100eq.png')
