import firebase_admin
import requests
import torch
from firebase_admin import credentials, db
from datetime import datetime
from find_location_from_saved_kpnts import process_image
from models.matching import Matching
from search_graph import get_shortest_path_text

cred = credentials.Certificate('navii-key.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://navii-fc6c9-default-rtdb.firebaseio.com/'})


def listener(event):
    destination_loc = event.data  # new data at /reference/event.path. None if deleted
    source_loc = firebase_admin.db.reference("location").get()
    print(destination_loc)
    print(source_loc)
    search_list = get_shortest_path_text(source_loc, destination_loc)
    print(search_list)
    firebase_admin.db.reference("to_location_text").set(search_list)


firebase_admin.db.reference('selectedLocation').listen(listener)
