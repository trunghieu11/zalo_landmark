import os
from os import listdir
from os.path import isfile, join

my_path = "/zserver/java-projects/zudm/deep-learning-projects/zalo_landmark/data/recognition/train/"

for i in range(103):
    path = my_path + str(i)
    for f in listdir(path):
        if isfile(join(path, f)):
            if os.path.getsize(join(path, f)) == 0:  # zero-byte files
                print(join(path, f))