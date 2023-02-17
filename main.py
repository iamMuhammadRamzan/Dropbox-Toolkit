import argparse
from model.rotation_classifier import RotationClassifier
from pathlib import Path
import cv2
from tqdm import tqdm
import os
from PIL import Image
import numpy as np
from utils.compute_matrices import compute_matrics_scores
from utils.dropbox_toolkit import DropboxToolkit
from utils.img_rotation import correct_image_rotation, rotate_image_randomly 
import io
import json
from utils.dropbox_toolkit import (get_image_list, read_image, create_folder,
                                    write_image, clean_dbx_image)


def test(input_dir):
    classifier = RotationClassifier()
    img_paths = [os.path.join(input_dir, f) for f in os.listdir(input_dir)]
    preds = [] 
    gt = []
    for img_path in tqdm(img_paths):
        image = cv2.imread(img_path)
        rotation, image = rotate_image_randomly(image)
        gt.append(rotation)
        pred_angle = classifier.predict(image)
        preds.append(pred_angle)
    compute_matrics_scores(gt, preds)

def predict(input_path, output_dir):
    classifier = RotationClassifier()
    f = open ('dropbox_credentials.json', "r")  
    credentials = json.loads(f.read())
    dbx = DropboxToolkit(credentials)
    image_paths = get_image_list(dbx ,input_path)
    for image_path in tqdm(image_paths, desc="Processing"):
        image = read_image(dbx, image_path)
        rotation = classifier.predict(image)
        image = correct_image_rotation(image, rotation)
        output_path = create_folder(dbx, image_path, output_dir)
        file_path = write_image(dbx, image, output_path)
        clean_dbx_image(dbx, image_path)

def main(input_path, output_dir, mode):
    if mode == "test":
        test(input_path)
    else :
        predict(input_path, output_dir)
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    arg = parser.add_argument
    arg("-i", "--input_path", type=str, help="Path with images.", required=True)
    arg("-o", "--output_dir", type=str, help="Path to save results.", required=False,
        default="output")
    parser.add_argument("--mode", type=str, help="mode to switch between test and predict", 
                                  default="predict")
    arg("--local_rank", default=-1, type=int, help="node rank for distributed training")
    args  = parser.parse_args()
    input_path = args.input_path
    output_dir = args.output_dir
    mode = args.mode
    main(input_path, output_dir, mode)