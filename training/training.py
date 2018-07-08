# -*- coding: UTF-8 -*-
import scipy
from sklearn.linear_model import LogisticRegression
import numpy as np
import train_model
def get_data_process():
    data = train_model.model_enter("10")
   #print len(data["WIN"]) + len(data["LOST"]) + len(data["DRAW"])
    # print 'WIN_ORI:', len(data["WIN"])
    # print 'DRAW_ORI:', len(data["DRAW"])
    # print 'LOST_ORI:', len(data["LOST"])
    train_set = []
    train_set = win_data_process(data, train_set)
    train_set = draw_data_process(data, train_set)
    train_set = lost_data_process(data, train_set)
    # train_set.append(win_data)
    # train_set.append(draw_data)
    # train_set.append(lost_data)
    print len(train_set)
    train_set = np.array(train_set, dtype=object)
    train_label = add_lable(data)
    print len(train_label)
    train_label = np.array(train_label, dtype=object)
    test_data = np.array([[1.59, 3.88, 6.66]],  dtype=object)
    train_data_process(train_set, train_label, test_data)
def win_data_process(data, train_set):
    #print 'WIN:', len(data["WIN"])
    for i in range(len(data["WIN"])):
        train_set.append(data["WIN"][i])
    return train_set
    #return np.array(data["WIN"])

def draw_data_process(data, train_set):
    #print "DRAW",len(data["DRAW"])
    for i in range(len(data["DRAW"])):
        train_set.append(data["DRAW"][i])
    return train_set
    #return np.array(data["DRAW"])

def lost_data_process(data, train_set):
    #print "LOST", len(data["LOST"])
    for i in range(len(data["LOST"])):
        train_set.append(data["LOST"][i])
    return train_set
    #return np.array(data["LOST"])

def add_lable(data):
    result = ["WIN", "DRAW", "LOST"]
    label = []
    for i in range(len(result)):
        tmp_len = len(data[result[i]])
        for j in range(tmp_len):
            label.append(result[i])
    return label


def train_data_process(train_data, train_label, t_data):
    clf = LogisticRegression()
    #print train_label
    clf.fit(train_data, train_label)
    #result
    result = clf.predict_proba(t_data)
    #print clf.predict(t_data)
    #print(clf.predict_proba(t_data))
    # print '克罗地亚:', result[0][0]
    # print 'Draw:', result[0][1]
    # print '英格兰', result[0][2]
    print result
    return result

def trainning_process():
    data = train_model.model_train_enter("10")
    # print len(data["WIN"]) + len(data["LOST"]) + len(data["DRAW"])
    # print 'WIN_ORI:', len(data["WIN"])
    # print 'DRAW_ORI:', len(data["DRAW"])
    # print 'LOST_ORI:', len(data["LOST"])
    train_set = []
    train_set = win_data_process(data, train_set)
    train_set = draw_data_process(data, train_set)
    train_set = lost_data_process(data, train_set)
    # train_set.append(win_data)
    # train_set.append(draw_data)
    # train_set.append(lost_data)
    #print len(train_set)
    train_set = np.array(train_set, dtype=object)
    train_label = add_lable(data)
    #print len(train_label)
    train_label = np.array(train_label, dtype=object)

    test_set = []
    test_label = []
    test_data = train_model.get_test_data("10")
    #print test_data
    test_set, test_label = train_win_data_process(test_data, test_set, test_label)
    test_set, test_label = train_draw_data_process(test_data, test_set, test_label)
    test_set, test_label = train_lost_data_process(test_data, test_set, test_label)
    print test_set
    #print test_label
    test_data_model = np.array(test_set, dtype=object)
    result = train_data_process(train_set, train_label  , test_data_model)
    # for i in range(len(result)):
    #     win = np.where(np.max(result[i]))
    #     print win

def train_win_data_process(data, data_set, data_label):
    for i in range(len(data["WIN"])):
        data_set.append(data["WIN"][i])
        data_label.append("WIN")
    return data_set, data_label

def train_draw_data_process(data, data_set, data_label):
    for i in range(len(data["DRAW"])):
        data_set.append(data["DRAW"][i])
        data_label.append("DRAW")
    return data_set, data_label

def train_lost_data_process(data, data_set, data_label):
    for i in range(len(data["LOST"])):
        data_set.append(data["LOST"][i])
        data_label.append("LOST")
    return data_set, data_label
trainning_process()