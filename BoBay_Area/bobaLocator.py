"""
Script responsible for scraping all boba stores in the BA
"""

import pandas as pd
import geocoder
import googlemaps
from shapely.geometry import Point
from geopandas import GeoDataFrame


class bobaLocator(object):
    gmaps = googlemaps.Client(key='[AIzaSyBVngqALccEFstz9ifeIEc-lw70M_ooQSM]')

    def __init__(self, filename):
        self.boba = pd.read_csv(filename)