import os
import random

trainval_percent = 1
train_percent = 0.5
xmlfilepath = 'red1/images'
txtsavepath = 'red1/ImageSets'
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
print(num)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
print(tv,tr)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)
print(train)
ftrainval = open('red1/ImageSets/trainval.txt', 'w')
ftest = open('red1/ImageSets/test.txt', 'w')
ftrain = open('red1/ImageSets/train.txt', 'w')
fval = open('red1/ImageSets/val.txt', 'w')
print(fval)
print(trainval)
for i in list:
    name = total_xml[i][:-4] + '\n'
    print(name)
    if 'ipynb' in name:
        continue
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
