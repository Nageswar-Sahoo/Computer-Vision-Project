import time

import cv2
import numpy as np
from sklearn.model_selection import train_test_split

path = 'IMagenet/tiny-imagenet-200/'


def get_id_dictionary():
    id_dict = {}
    for i, line in enumerate(open(path + 'wnids.txt', 'r')):
        id_dict[line.replace('\n', '')] = i
    return id_dict


def get_class_to_id_dict():
    id_dict = get_id_dictionary()
    all_classes = {}
    result = {}
    for i, line in enumerate(open(path + 'words.txt', 'r')):
        n_id, word = line.split('\t')[:2]
        all_classes[n_id] = word
    for key, value in id_dict.items():
        result[value] = (key, all_classes[key])
    return result


def get_data(id_dict):
    print('starting loading data')
    train_data, test_data = [], []
    train_labels, test_labels = [], []
    t = time.time()
    for key, value in id_dict.items():
        train_data += [cv2.imread( path + 'train/{}/images/{}_{}.JPEG'.format(key, key, str(i))) for i in range(500)]
        train_labels_ = np.array([[0] * 200] * 500)
        train_labels_[:, value] = 1
        train_labels += train_labels_.tolist()

    for line in open(path + 'val/val_annotations.txt'):
        img_name, class_id = line.split('\t')[:2]
        test_data.append(cv2.imread( path + 'val/images/{}'.format(img_name)))
        test_labels_ = np.array([[0] * 200])
        test_labels_[0, id_dict[class_id]] = 1
        test_labels += test_labels_.tolist()

    print('finished loading data, in {} seconds'.format(time.time() - t))
    return np.array(train_data), np.array(train_labels), np.array(test_data), np.array(test_labels)


def get_splited_data():
    train_data, train_labels, test_data, test_labels = get_data(get_id_dictionary())
    # 70 % 30 Split
    train_data_u, train_data_20, train_labels_u, train_labels_20 = train_test_split(train_data, train_labels,
                                                                                test_size=0.20, random_state=42)
    test_data=np.concatenate((train_data_20 , test_data))
    test_labels=np.concatenate((train_labels_20 , test_labels))


    print("test data shape: ", test_data.shape)
    print("test_labels.shape: ", test_labels.shape)
    print( "train data shape: ",  train_data_u.shape )
    print( "train label shape: ", train_labels_u.shape )
    return train_data_u,train_labels_u,test_data,test_labels