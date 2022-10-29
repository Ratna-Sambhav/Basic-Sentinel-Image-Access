from image_access import get_satellite_img
import matplotlib.pyplot as plt 
import plotly.express as pxs
import plotly
import plotly.graph_objects as px
import numpy as np
import rasterio
import folium

# Patna Bridge: 
lt=25.6198
ln=85.2043

img, patch, map = get_satellite_img(lat=lt, lon=ln, datetime='2017-05-01/2019-06-01')

img_tiff = rasterio.open('App_pystac/templates/Images/RGB_masked2.tif')
np_img = img_tiff.read([1,2,3])
img = np.moveaxis(np_img, 0, 2)


plot = px.Figure(data=[px.Image(z=img)])


# Add dropdown
# plot.update_layout(
# 	updatemenus=[
# 		dict(
# 			active=0,
# 			buttons=list([
# 				dict(label="Location (5km Area)",
# 					method="update",
# 					args=[{"visible": [True, False]},
# 						{"title": "Location (5km Area)",
# 							}]),
# 				dict(label="Satellite Patch",
# 					method="update",
# 					args=[{"visible": [False, True]},
# 						{"title": "Satellite Patch",
# 							}]),
# 			]),
# 		)
# 	])

plot.write_html("App_pystac/templates/file.html")