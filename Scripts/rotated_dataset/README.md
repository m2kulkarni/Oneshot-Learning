Run this script to get all dataset containing all images rotated 0,90,180,270 degrees.

Saved as omniglot.npy file
omniglot.npy.shape = [num_classes*4, 20, 28, 28]
omniglot[0:4, 1] = line 0:4 from txt file.

run script
`python3 make_dataset.py [root_dir] [txt name]`
