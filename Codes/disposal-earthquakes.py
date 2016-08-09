# Graph disposal wells and earthquakes over time
# Disposal Wells vs. Year
# Earthquakes vs. Year

from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Disposal Wells

disposal_wells = pd.read_csv('Well Headers.csv', index_col=33, parse_dates=True)

disposal_wells['Year'] = disposal_wells.index.year

disposal_wells_per_year = disposal_wells.groupby(['Year']).size()


# Earthquakes

earthquakes = pd.read_csv('completeEarthquakeFreq.txt', index_col=1, parse_dates=True)

earthquakes['Year'] = earthquakes.index.year

earthquakes_per_year = earthquakes.groupby(['Year']).size()


# Cumulative number of disposal wells

cum_disposal_wells_per_year = disposal_wells_per_year.cumsum()

# Visualization
plt.close()
fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)
disposal_wells_per_year.plot(ax=axes[0], title = 'Disposal Wells per Year (Spud Date)')
#earthquakes_per_year.plot(ax=axes[2], title = 'Earthquakes per Year')
cum_disposal_wells_per_year.plot(ax=axes[1], title = 'Cumulative Number of Disposal Wells')
plt.show()