import os
import glob
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#import tensorflow as tf
import sys

root_dir=sys.argv[1]

split_file=sys.argv[2]

save_file_name=sys.argv[3]
dataset_split_path=os.path.join(root_dir, split_file)

with open(dataset_split_path, 'r') as split:
    train_classes = [line.rstrip() for line in split.readlines()]
#print(train_classes[413])

no_of_classes=len(train_classes)
num_examples = 20
img_width = 28
img_height = 20
channels = 1

dataset = np.zeros([no_of_classes, num_examples, img_height, img_width], dtype=np.float32)


for label, name in enumerate(train_classes):
    alphabet, character, rotation = name.split('/')
    rotation=float(rotation[3:])
    img_dir=os.path.join(root_dir, 'images_evaluation', alphabet, character)
    
    if not (os.path.isdir(img_dir)):
        img_dir=os.path.join(root_dir, 'images_background', alphabet, character)

    img_files = sorted(glob.glob(os.path.join(img_dir, '*.png')))
    print(alphabet, '-->', character, '-->', rotation)

    for index, img_file in enumerate(img_files):
        values = 1. - np.array(Image.open(img_file).rotate(rotation).resize((img_width, img_height)), np.float32, copy=False)
        dataset[label, index] = values

        if label==100:
            im=Image.fromarray(dataset[label][index])
            im=im.convert("L")
            im.save('img'+str(index)+'.png')

np.save(save_file_name, dataset)
