import numpy as np
import pandas as pd
from geojson import LineString, dump
import routingpy as rp
from time import sleep

# Mapbox token
api_key = "*** INSERT API KEY HERE ***"
api = rp.MapboxOSRM(api_key=api_key,
	timeout=2,
	skip_api_error=True,
	retry_over_query_limit=True
	)

# read in files
df = pd.read_csv('../CPL_Locations.csv')
coordinates = df[['LNG_CLEAN', 'LAT_CLEAN']].values.tolist()
names = df['BRANCH']
names = names.to_list()

# pasting solution from solver
# manually added 0 and 81 to the end again
solution = [0, 81, 48, 129, 3, 84, 76, 157, 79, 160, 13, 94, 47, 128, 17, 98, 34, 115, 71, 152, 80, 161, 55, 136, 2, 83, 14, 95, 15, 96, 74, 155, 27, 108, 72, 153, 78, 159, 22, 103, 38, 119, 60, 141, 23, 104, 73, 154, 31, 112, 46, 127, 64, 145, 37, 118, 58, 139, 68, 149, 8, 89, 41, 122, 45, 126, 30, 111, 1, 82, 35, 116, 77, 158, 53, 134, 6, 87, 70, 151, 66, 147, 67, 148, 42, 123, 43, 124, 75, 156, 4, 85, 9, 90, 51, 132, 62, 143, 28, 109, 49, 130, 50, 131, 63, 144, 39, 120, 24, 105, 25, 106, 40, 121, 44, 125, 29, 110, 12, 93, 69, 150, 5, 86, 36, 117, 54, 135, 11, 92, 10, 91, 16, 97, 7, 88, 26, 107, 32, 113, 59, 140, 65, 146, 19, 100, 61, 142, 33, 114, 21, 102, 56, 137, 18, 99, 20, 101, 52, 133, 57, 138, 0, 81]

# pick alternate elements: these correspond to the originals
tour = solution[::2]

# order the original coordinates and names
coords_ordered = [coordinates[i] for i in tour]
names_ordered = [names[i] for i in tour]

# create a list to batch directions
indices = [(0, 24), (24, 48), (48, 72), (72, 81)]
all_directions = []

# get directions
for index in indices:
	dir = api.directions(locations=coords_ordered[index[0]:index[1]],
	profile="cycling")
	
	print(dir)
	print("Distance: ", dir.distance/1600, " miles", "\nDuration: ", dir.duration/60, " minutes")
	all_directions.append(dir.geometry)
	sleep(3)

geoj = LineString(all_directions)

with open("route.geojson", "w") as out_file:
	dump(geoj, out_file)
