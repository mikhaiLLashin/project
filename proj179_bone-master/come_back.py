import os
from random import randint
from PIL import Image

path_1 = 'C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\'
path_tr = "C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\train\\"
path_val = "C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\val\\"

directory = os.fsencode(path_tr + "images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if str(filename[-4:]) != ".npy":
        os.rename(path_tr + "images\\" + str(filename), path_1 + "images\\" + str(filename))
        os.rename(path_tr + "labels\\" + str(filename[:-4]) + ".txt", path_1 + "labels\\" + str(filename[:-4]) + ".txt")
directory = os.fsencode(path_val + "images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if str(filename[-4:]) != ".npy":
        os.rename(path_val + "images\\" + str(filename), path_1 + "images\\" + str(filename))
        os.rename(path_val + "labels\\" + str(filename[:-4]) + ".txt", path_1 + "labels\\" + str(filename[:-4]) + ".txt")
