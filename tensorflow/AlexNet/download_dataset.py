# Downloads ImageNet Dataset
import os

DATASET_DIR_NAME = 'imagenet_2012'
DATASET_PREFIX = '../../datasets/' 
DATASET_DIR_PATH = DATASET_PREFIX + DATASET_DIR_NAME

if not os.path.exists(DATASET_DIR_PATH):
	os.makedirs(DATASET_DIR_PATH)
else:
	print('ImageNet directory already exists')