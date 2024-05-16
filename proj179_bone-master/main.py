from ultralytics import YOLO
import os

path = 'C:\\Users\\lashi\\Desktop\\bones\\images\\'

model = YOLO('yolov8n.pt')
path_tr = "C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\train\\images\\"
path_val = "C:\\Users\\User\\Desktop\\proj179_bone-master\\proj179_bone-master\\val\\images\\"
dir_tr = os.fsdecode(path_tr)
dir_val = os.fsdecode(path_val)
arr = []
for file in os.listdir(dir_tr):
    filename = os.fsdecode(file)
    arr.append(path_tr + "\\" + filename)
for file in os.listdir(dir_val):
    filename = os.fsdecode(file)
    arr.append(path_val + filename)
def main():
    results = model.train(data='data.yaml', epochs=10000, imgsz=1024, patience=0, batch=2, device=0)
if __name__ == '__main__':
    main()

