import pandas as pd 
import numpy as np
from pandas import DataFrame, Series
import plotly.plotly as py
import plotly.tools as tls

#Importing Dataset
eq_data = pd.read_csv('..\\Files\\processed-data\\completeEarthquakeFreq.csv')

#Changing data format
eq_data['origintime'] = pd.to_datetime(eq_data['origintime'])
eq_data['YEAR'] =  eq_data.origintime.apply(lambda x: x.year)

#Removing 2016, as it's still ongoing
eq_data = eq_data[eq_data['YEAR'] != 2016]

#Setting credentials for plotly
tls.set_credentials_file(username='aayushmnit', api_key='lft7xcme6n')

#Plotting
data = []
layout = dict(
    title = 'Earthquake Yearly data',
    # showlegend = False,
    autosize = False,
    width = 1000,
    height = 1200,
    hovermode = False,
    legend = dict(
        x=0.7,
        y=-0.1,
        bgcolor="rgba(255, 255, 255, 0)",
        font = dict( size=11 ),
    )
)
years = eq_data['YEAR'].unique()
counts = list(eq_data.groupby('YEAR').size())
for i in range(len(years)):
    geo_key = 'geo'+str(i+1) if i != 0 else 'geo'
    lons = list(eq_data[ eq_data['YEAR'] == years[i] ]['longitude'])
    lats = list(eq_data[ eq_data['YEAR'] == years[i] ]['latitude'])
    # Walmart store data
    data.append(
        dict(
            type = 'scattergeo',
            showlegend=False,
            lon = lons,
            lat = lats,
            geo = geo_key,
            name = years[i],
            marker = dict(
                color = "rgb(0, 0, 255)",
                opacity = 0.5
            )
        )
    )
    # Year markers
    data.append(
        dict(
            type = 'scattergeo',
            showlegend = False,
            lon = [-78],
            lat = [47],
            geo = geo_key,
            text = [str(years[i]) + ',' + str(counts[i])],
            mode = 'text',
        )
    )
    layout[geo_key] = dict(
        scope = 'usa',
        showland = True,
        landcolor = 'rgb(229, 229, 229)',
        showcountries = False,
        domain = dict( x = [], y = [] ),
        subunitcolor = "rgb(255, 255, 255)",
        
    )


def draw_sparkline( domain, lataxis, lonaxis ):
    ''' Returns a sparkline layout object for geo coordinates  '''
    return dict(
        showland = False,
        showframe = False,
        showcountries = False,
        showcoastlines = False,
        domain = domain,
        lataxis = lataxis,
        lonaxis = lonaxis,
        bgcolor = 'rgba(255,200,200,0.0)',
        scale = 10
    )

z = 0
COLS = 7
ROWS = 9
for y in reversed(range(ROWS)):
    for x in range(COLS):
        geo_key = 'geo'+str(z+1) if z != 0 else 'geo'
        layout[geo_key]['domain']['x'] = [float(x)/float(COLS), float(x+1)/float(COLS)]
        layout[geo_key]['domain']['y'] = [float(y)/float(ROWS), float(y+1)/float(ROWS)]
        z=z+1
        if z > 63:
            break

fig = { 'data':data, 'layout':layout }
py.iplot( fig, filename='Oklahoma Earthquakes', height=1200, width=1000 )