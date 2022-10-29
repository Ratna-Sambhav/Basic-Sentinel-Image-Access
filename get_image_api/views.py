from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status 
import json
from App_pystac.models import Entries

## Libraries related to satellite image access
from .image_access import get_satellite_img
import matplotlib.pyplot as plt 
import plotly.express as pxs
import plotly
import plotly.graph_objects as px
import numpy as np
import rasterio
import folium

# Create your views here.
def satellite_image(request):
    if request.method == 'GET':
        data = json.loads(request.body) 
        ide = data['pk']
        print(ide)
        entry = Entries.objects.all().filter(pk=ide)
        # print(entry.values()[0]['userName'])

        # Using the function to download the satellite image, convert to np format and saving it in html form 
        img, patch, map = get_satellite_img(lat=entry.values()[0]['lat'], \
            lon=entry.values()[0]['long'], \
                datetime='2017-05-01' + '/2022-06-01')

        # Accessing the saved geotiff file and bringing it to proper format
        img_tiff = rasterio.open('App_pystac/templates/Images/RGB_masked2.tif')
        np_img = img_tiff.read([1,2,3])
        img = np.moveaxis(np_img, 0, 2)

        # Showing the image in a plotly plot and exporting to html page format
        plot = px.Figure(data=[px.Image(z=img)])
        plot.write_html("App_pystac/templates/file.html")

    return JsonResponse({'message':'Task Done'}, status=status.HTTP_200_OK)