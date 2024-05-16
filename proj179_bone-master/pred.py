from ultralytics import YOLO
import os

model = YOLO('runs/detect/train2/weights/best.pt')
path_tr = "test_photo"
path_val = "C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\val\\images\\"
dir_tr = os.fsdecode(path_tr)
dir_val = os.fsdecode(path_val)
arr = []
for file in os.listdir(dir_tr):
    filename = os.fsdecode(file)
    arr.append(path_tr + "/" + filename)
'''for file in os.listdir(dir_val):
    filename = os.fsdecode(file)
    arr.append(path_val + filename)'''
for n in arr:
    model.predict(n, save=True, imgsz=1024, conf=0.3)