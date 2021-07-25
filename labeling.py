import csv
from random import randrange
import numpy as np

def datasets(id_1=0,id_2=0):
    list = [8, 13, 17]
    dates = ["2021-07-23-15-03-49", "2021-07-23-15-04-08", "2021-07-23-15-04-27", "2021-07-23-15-04-58"]
    
    id_1 = randrange(12)
    id_2 = randrange(12)
    if id_1 == id_2:
        id_2 = (id_2 + 1) % 12
    
    
    fname = dates[int(id_1/4)] + "_people_" + str(list[id_1%3]) + "_j_diff.csv"
    print(fname)
    file = open("./" + fname , "r")
    data_1 = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    data_1 = [row for row in data_1]
    fname = dates[int(id_2/4)] + "_people_" + str(list[id_2%3]) + "_j_diff.csv"
    print(fname)
    file = open("./" + fname , "r")
    data_2 = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    data_2 = [row for row in data_2]
    
    label = 0
    if int(id_1/4) == int(id_2/4):
        label = 1

    dataset = []
    itr = 0
    tmp_list = []
    tmp_list.append(data_1[1:46])
    tmp_list.append(data_2[1:46])
    tmp_list.append(label)
    # print(tmp_list)
    dataset.append(tmp_list)
    print(np.sqrt(np.sum(np.square(np.array(data_1[1:46]).astype(np.float) - np.array(data_2[1:46]).astype(np.float)))))
 
    while(True):
        itr += 3
        if (len(data_1)> itr + 45 or len(data_2)> itr + 45):
            break
        tmp_list = []
        tmp_list.append(data_1[itr:45+itr])
        tmp_list.append(data_2[itr:45+itr])
        tmp_list.append(label)
        dataset.append(tmp_list)

    return dataset


datasets()
# for i in range(4):
#     j = i*3
#     datasets(i, i+1)
#     datasets(i, i+2)
#     datasets(i+1, i+2)
#     print ("----------")