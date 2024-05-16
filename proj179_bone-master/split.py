import os
from random import randint

path_1 = 'C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\'
path_tr = 'C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\train\\'
path_val = 'C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\val\\'

directory = os.fsencode(path_1 + "images")
cnt = 0
for file in os.listdir(directory):
     cnt += 1
     filename = os.fsdecode(file)
     if (randint(1, 15) >= 3):
          os.rename(path_1 + "images\\" + str(filename), path_tr + "images\\" + f"a{cnt}.jpg")
          os.rename(path_1 + "labels\\" + str(filename[:-4]) + ".txt", path_tr + "labels\\" + f"a{cnt}.txt")
     else:
          os.rename(path_1 + "images\\" + str(filename), path_val + "images\\" + f"a{cnt}.jpg")
          os.rename(path_1 + "labels\\" + str(filename[:-4]) + ".txt", path_val + "labels\\" + f"a{cnt}.txt")