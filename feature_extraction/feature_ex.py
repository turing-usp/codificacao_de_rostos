import cv2
import landmarks as ld
import os
import matplotlib.pyplot as plt
import pandas as pd
dataset_folder = './data'

os.chdir(dataset_folder)
folders = os.listdir('.')
df = dict()
for folder in folders:
    path = os.chdir(folder)
    for img in os.listdir('.'):
        img_array = cv2.imread(img)
        features = ld.marks(img_array)
        df[img] = features
    os.chdir('..')
os.chdir('..')
df = pd.DataFrame(df)
df = df.T
print(df.head())
df.to_csv("dataset.csv")