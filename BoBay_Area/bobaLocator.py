"""
Script responsible for scraping all boba stores in the BA
"""
import geopandas
import numpy
import pandas as pd
import geocoder
import googlemaps
from shapely.geometry import Point
from geopandas import GeoDataFrame
from geojsonio import display


class bobaLocator(object):
    gmaps = googlemaps.Client(key='[AIzaSyBVngqALccEFstz9ifeIEc-lw70M_ooQSM]')

    def __init__(self, filename):
        self.boba = pd.read_csv(filename)

    def calc_coords(self):
        self.boba['Lat'] = self.boba['Address'].apply(geocoder.google).apply(lambda x: x.lat)
        self.boba['Longitude'] = self.boba['Address'].apply(geocoder.google).apply(lambda x: x.lng)
        self.boba['Coordinates'] = [Point(xy) for xy in zip(self.boba.Longitude, self.boba.Lat)]

    def get_geo(self):
        return(list(self.boba['Coordinates']))

    def get_names(self):
        return(self.boba['Name'])

    def get_gdf(self):
        crs = {'init': 'epsg:4326'}
        return(GeoDataFrame(self.get_names(), crs=crs, geometry=self.get_geo()))

    def visualize(self):
        self.boba['Coordinates'] = [Point(xy) for xy in zip(self.boba.Longitude, self.boba.Lat)]
        updated = self.get_gdf()
        display(updated.to_json())