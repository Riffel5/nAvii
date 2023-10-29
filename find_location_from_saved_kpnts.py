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


def process_image(matching, device):

    resize = [640, 480]
    skip = 1
    image_glob = ['*.png', '*.jpg', '*.jpeg', '*.JPG']
    max_length = 1000000

    keys = ['keypoints', 'scores', 'descriptors']
    vs = VideoStreamer("./input/", resize, skip, image_glob, max_length)
    frame, ret = vs.next_frame()
    assert ret, 'Error when reading the first frame (try different --input?)'

    frame_tensor = frame2tensor(frame, device)
    last_data = matching.superpoint({'image': frame_tensor})
    last_data = {k + '0': last_data[k] for k in keys}
    last_data['image0'] = frame_tensor

    timer = AverageTimer()
    vs = VideoStreamer("./ref/", resize, skip, image_glob, max_length)

    ref_maps = list(Path("./ref/").glob("*.JPG"))

    with open("ref_kpnts.pkl", 'rb') as handle:
        ref_kpnts = pickle.load(handle)

    for test in ref_kpnts:
       # frame_tensor = frame2tensor(frame, device)
        pred = matching({**last_data, **test})
        kpts0 = last_data['keypoints0'][0].cpu().numpy()
        matches = pred['matches0'][0].cpu().numpy()
       # confidence = pred['matching_scores0'][0].cpu().numpy()
        timer.update('forward')

        valid = matches > -1
        mkpts0 = kpts0[valid]
        print(test["name"], len(mkpts0))


if __name__ == "__main__":
    process_image()
