import firebase_admin
import requests
import torch
from firebase_admin import credentials, db

from find_location_from_saved_kpnts import process_image
from models.matching import Matching

torch.set_grad_enabled(False)


device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('Running inference on device \"{}\"'.format(device))

nms_radius = 4
keypoint_threshold = 0.005
max_keypoints = 1024
superglue = 'indoor'
sinkhorn_iterations = 20
match_threshold = 0.2

config = {
    'superpoint': {
        'nms_radius': nms_radius,
        'keypoint_threshold': keypoint_threshold,
        'max_keypoints': max_keypoints
    },
    'superglue': {
        'weights': superglue,
        'sinkhorn_iterations': sinkhorn_iterations,
        'match_threshold': match_threshold,
    }
}

matching = Matching(config).eval().to(device)

cred = credentials.Certificate('navii-key.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://navii-fc6c9-default-rtdb.firebaseio.com/'})


def listener(event):
    image_url = event.data  # new data at /reference/event.path. None if deleted
    data = requests.get(image_url).content
    f = open('./input/img.jpg', 'wb')
    f.write(data)
    f.close()

    process_image(matching, device)


firebase_admin.db.reference('image').listen(listener)
