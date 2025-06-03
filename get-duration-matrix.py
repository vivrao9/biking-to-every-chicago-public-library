import pandas as pd
import numpy as np
import routingpy as rp

# load data in
df = pd.read_csv("CPL_Locations.csv", index_col="BRANCH")
coordinates = df[["LNG_CLEAN", "LAT_CLEAN"]]
names = df.index

# create a DataFrame for all library branches
# this DataFrame acts as a filler for the matrix
blanks = pd.DataFrame(index=df.index, columns=list(df.index))

# set up Mapbox token
# api_key = ***INSERT API KEY HERE***
api = rp.MapboxOSRM(api_key=api_key,
	timeout=2,
	skip_api_error=True,
	retry_over_query_limit=True
	)

# create a function to loop through and run Matrix(...) for each
# index-column pair in the blanks DataFrame
for i in blanks.index:
	print(i)
	# this is the index
	
	for j in blanks.columns:
		# this is the column header
		
		# find coordinates for the index library
		i_coord_lat = df.loc[i, "LAT_CLEAN"]
		i_coord_lon = df.loc[i, "LNG_CLEAN"]
		
		# find coordinates for the column library
		j_coord_lat = df.loc[j, "LAT_CLEAN"]
		j_coord_lon = df.loc[j, "LNG_CLEAN"]
		
		# return pair of coordinates
		current_coords = [[i_coord_lon, i_coord_lat],[j_coord_lon, j_coord_lat]]
		# print(current_coords)
		
		# run this coordinate pair through Mapbox OSRM's Matrix API
		matrix = api.matrix(locations=current_coords, profile="cycling")
		blanks.loc[i, j] = matrix.durations[0][1]
		blanks.loc[j, i] = matrix.durations[1][0]

blanks.to_csv("./matrix.csv")
print(blanks)
