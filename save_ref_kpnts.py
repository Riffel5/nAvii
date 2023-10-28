from pathlib import Path
import argparse
import cv2
import matplotlib.cm as cm
import torch
import pickle

from models.matching import Matching
from models.utils import (AverageTimer, VideoStreamer,
                          make_matching_plot_fast, frame2tensor)

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
resize = [640, 480]
skip = 1
image_glob = ['*.png', '*.jpg', '*.jpeg', '*.JPG']
max_length = 1000000
matching = Matching(config).eval().to(device)


keys = ['keypoints', 'scores', 'descriptors']
vs = VideoStreamer("./input/", resize, skip, image_glob, max_length)
frame, ret = vs.next_frame()
assert ret, 'Error when reading the first frame (try different --input?)'

all_data = []


last_frame = frame
last_image_id = 0

timer = AverageTimer()
vs = VideoStreamer("./ref/", resize, skip, image_glob, max_length)

ref_maps = list(Path("./ref/").glob("*.JPG"))
i = 0
while True:
    frame, ret = vs.next_frame()
    if not ret:
        break
    frame_tensor = frame2tensor(frame, device)
    last_data = matching.superpoint({'image': frame_tensor})
    last_data = {k + '1': last_data[k] for k in keys}
    last_data['image1'] = frame_tensor
    last_data['name'] = str(ref_maps[i])
    all_data.append(last_data)
    i += 1

with open("ref_kpnts.pkl", 'wb') as output:
    pickle.dump(all_data, output, pickle.HIGHEST_PROTOCOL)

