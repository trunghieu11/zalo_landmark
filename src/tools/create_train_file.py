from os import listdir
from os.path import isfile, join

import shutil

train_file = open("/home/trunghieu11/Work/zalo_landmark/data/train.csv", "a+")

my_path = "/home/trunghieu11/Work/zalo_landmark/data/TrainVal/"
all_folder_path = "/home/trunghieu11/Work/zalo_landmark/data/all/"

for i in range(103):
    path = my_path + str(i)
    for f in listdir(path):
        if isfile(join(path, f)):
            # train_file.write(f + "," + str(i) + "\n")
            shutil.copyfile(path + "/" + f, all_folder_path)

train_file.close()