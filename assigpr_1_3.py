# Assignment 1

# Problem 3 (2pts) Implement the exact solution knn for the dataset 1. Find the best k using 5 fold cross validation. Don’t forget to shuﬄe your dataset. Create a table with results for k from 1 to 11, for the validation fold and test set.
# There are two folders in your dataset 1: training validation should be used to ﬁnd the best k; test should be used to test the classiﬁer after your ﬁnd the best k using the training validation set.


import csv
import random
import math
import operator
import os
import numpy as np

basepath = 'C:/Users/Abhishek Nagrecha/Desktop/SEM1/PATTERN_RECOGNITION/data set1/training_validation/'
final_train = []


def genrate_datas():
    for entry in os.listdir(basepath):
        all_whole = []
        ff = os.path.join(basepath, entry)
        if os.path.isfile(ff):
            whole_array = []
            with open(ff, 'r') as f:
                for line in f:
                    singl_array = []
                    for line_character in line:
                        singl_array.append(line_character)
                    singl_array.remove('\n')
                    whole_array.append(singl_array)
                all_whole.append(whole_array)
                all_whole.append(entry[0:7])
        final_train.append(all_whole)


#
# # print(final_train[0][0])
# testpath = 'C:/Users/Abhishek Nagrecha/Desktop/SEM1/PATTERN_RECOGNITION/data set1/'
# final_test = []
# for entry in os.listdir(testpath):
#     all_whole = []
#     ff = os.path.join(basepath, entry)
#     if os.path.isfile(ff):
#         whole_array = []
#         with open(ff, 'r') as f:
#             for line in f:
#                 singl_array = []
#                 for line_character in line:
#                     singl_array.append(line_character)
#                 singl_array.remove('\n')
#                 whole_array.append(singl_array)
#             all_whole.append(whole_array)
#             all_whole.append(entry[0:7])
#     final_test.append(all_whole)
# final_test.remove([])
# final_test.remove([])


def get_neighbours(train_set, testInstance, k):
    # print("In get neigbous 2")
    distances = []
    for z in range(len(train_set)):
        dist = euclidean_dist(train_set[z][0], testInstance)
        distances.append((train_set[z], dist))
    distances.sort(key=operator.itemgetter(1))
    # print(distances)
    neigh = []
    # print("len of distance: ", distances[0][1])
    # print(len(distances[0]))
    for z in range(k):
        neigh.append(distances[z][0][1])
        # print(distances[z][0][1])
    return neigh


def euclidean_dist(trainn_list, new_list):
    zz = (np.array(trainn_list)).astype(int) - (np.array(new_list)).astype(int)
    zz = zz ** 2
    res = np.sum(zz)
    return math.sqrt(res)


def shffle_values():
    random.shuffle(final_train)


def get_resp(neigh):
    set = {}
    for z in range(len(neigh)):
        resp = neigh[z]
        # print("resp: ", resp)
        if resp in set:
            set[resp] += 1
        else:
            set[resp] = 1
    typevalue = sorted(set.items(), key=operator.itemgetter(1), reverse=True)
    # print(set)
    return typevalue[0][0]


def get_accuracy(testt_set, predict):
    true = 0
    false = []
    # print(predict)
    for z in range(len(testt_set)):
        if testt_set[z][1] == predict[z]:
            true += 1
        else:
            temp = "original: " + str(testt_set[z][1]) + " predicted: " + str(predict[z])
            false.append(temp)
    print(false)
    return (true / float(len(testt_set))) * 100.0


def main():
    genrate_datas()
    shffle_values()
    len_data = int(len(final_train))
    all_fold = int(len_data / 5)
    # print(len_data)
    # print(all_fold)
    # print(all_fold * 2)
    # print(all_fold * 3)
    # print(all_fold * 4)
    # print(all_fold * 5)
    res_table = []

    # test_datas1 = final_train[0:all_fold]
    # trainn_datas1 = final_train[all_fold:]
    # test_datas2 = final_train[all_fold:(all_fold*2)]
    # trainn_datas2 = final_train[:all_fold]
    # trainn_datas2.extend(final_train[all_fold*2:])
    # test_datas3 = final_train[(all_fold*2):(all_fold*3)]
    # trainn_datas3 = final_train[:all_fold*2]
    # trainn_datas3.extend(final_train[all_fold*3:])
    # test_datas4 = final_train[all_fold*3:(all_fold*4)]
    # trainn_datas4 = final_train[:all_fold*3]
    # trainn_datas4.extend(final_train[all_fold * 4:])
    # test_datas5 = final_train[all_fold*4:]
    # trainn_datas5 = final_train[:(all_fold*4)]
    #
    # testing_lst = [test_datas1,test_datas2,test_datas3,test_datas4,test_datas5]
    # training_lst = [trainn_datas1,trainn_datas2,trainn_datas3,trainn_datas4,trainn_datas5]
    for tt in range(5):
        for k in range(1, 12):
            all_k = {}
            test_datas = testing_lst[tt]
            trainn_datas = training_lst[tt]
            # print(len(test_datas))
            predict = []
            for i in range(len(test_datas)):
                # print(test_datas[i][1])
                # print("In get neigbous 1")
                neighbours = get_neighbours(trainn_datas, test_datas[i][0], k)
                # print("neighbours: ",neighbours)
                results = get_resp(neighbours)
                # print("results: ",results)
                predict.append(results)
                # print('> predicted=' + repr(results) + ', actual=' + repr(test_datas[i][1]))
            accuracy = get_accuracy(test_datas, predict)
            all_k[k] = accuracy
            res_table.append(all_k)
            print("Accuracy: ", accuracy)
        for i in res_table:
            for k, v in i.items():
                print("for  the given values of ", k, ": accuracy is shown as follows ", v)
            # print(v)
    #
    # test_datas = final_train[all_fold:all_fold * 2]
    # trainn_datas = final_train[0:all_fold].eztent(final_train[all_fold * 2:])
    #
    # test_datas = final_train[all_fold * 2 : all_fold * 3]
    # trainn_datas = final_train[0:all_fold*2].eztent(final_train[all_fold * 3:])


main()
