# Geographic-TSP
Practical code for solving geographic travelling salesman problem using _routingpy_ and _pyconcorde_. This repository was forked from Mike Jones' Geographic TSP repo (https://github.com/mikedbjones/Geographic-TSP) and is applied to the Chicago Public Library system by bike.

The shortest route is available in route.geojson, which was calculated from ```create-route.py```. The path was exported using Mapbox OSRM through routingpy. Some biking were not 100% accurate, so they were manually tweaked on geojson.io (https://geojson.io).

![Solution](https://github.com/vivrao9/biking-to-every-chicago-public-library/blob/master/solution.png)
