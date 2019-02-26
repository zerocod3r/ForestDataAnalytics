# import matplotlib.pyplot as plt
# from mpl_toolkits import Basemap
# import pandas as pd
# import io

# u = u"""latitude,longitude
# 42.357778,-71.059444
# 39.952222,-75.163889
# 25.787778,-80.224167
# 30.267222, -97.763889"""

# # read in data to use for plotted points
# buildingdf = pd.read_csv(io.StringIO(u), delimiter=",")
# lat = buildingdf['latitude'].values
# lon = buildingdf['longitude'].values

# # determine range to print based on min, max lat and lon of the data
# margin = 2 # buffer to add to the range
# lat_min = min(lat) - margin
# lat_max = max(lat) + margin
# lon_min = min(lon) - margin
# lon_max = max(lon) + margin

# # create map using BASEMAP
# m = Basemap(llcrnrlon=lon_min,
#             llcrnrlat=lat_min,
#             urcrnrlon=lon_max,
#             urcrnrlat=lat_max,
#             lat_0=(lat_max - lat_min)/2,
#             lon_0=(lon_max-lon_min)/2,
#             projection='merc',
#             resolution = 'h',
#             area_thresh=10000.,
#             )
# m.drawcoastlines()
# m.drawcountries()
# m.drawstates()
# m.drawmapboundary(fill_color='#46bcec')
# m.fillcontinents(color = 'white',lake_color='#46bcec')
# # convert lat and lon to map projection coordinates
# lons, lats = m(lon, lat)
# # plot points as red dots
# m.scatter(lons, lats, marker = 'o', color='r', zorder=5)
# plt.show()

from bs4 import BeautifulSoup
import requests,json
from geopy.geocoders import Nominatim

url = 'http://epsg.io/trans?s_srs=3067&t_srs=4326&x=240315.9451000&y=6654181.5378000'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
data = json.loads(soup.text)
print(str(data['y']) + str(data['x']))
tmp = str(data['y']) + ','+str(data['x'])
geolocator = Nominatim()
location = geolocator.reverse(tmp)
print(location.address)


