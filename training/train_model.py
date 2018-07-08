# -*- coding: UTF-8 -*-
import json

def model_train_enter(team):
    original_data = get_data_process(team, True)
    split_data = split_data_process(original_data, team)
    format_data = format_data_process(split_data)
    return format_data

def model_enter(team):
    original_data = get_data_process(team)
    split_data = split_data_process(original_data, team)
    format_data = format_data_process(split_data)
    return format_data

def get_data_process(team, train=False):
    file_path = '/Users/francis/Documents/worldCup/data/history/allteam/' + team + '.json'
    file_ori = open(file_path,'r+')
    file_ori = file_ori.read()
    file_content = json.loads(file_ori)
    if train == True:
        test_data_size = len(file_content) / 10
        return  file_content[test_data_size:]

    #file_ori.close()
    return file_content    

def split_data_process(data, team):
    split_set = {}
    split_set["WIN"] = []
    split_set["DRAW"] = []
    split_set["LOST"] = []
    data_len = len(data)
    for i in range(data_len):
        info = data[i]['lpl_on']
        info = info.encode('UTF-8').decode('string_escape')
        #print info["HOMETI"]
        # print 'home',data[i]["HOMETEAMID"]
        # print 'team', team
        # print data[i]["HOMETEAMID"] == team
        # print '>>>>>>>>>>>>>>>>'
        if data[i]["HOMETEAMID"] != team:
            #print 'passhere', info, '>>>'
            tmp_win = data[i]["WIN"]
            tmp_lost = data[i]["LOST"]
            data[i]["WIN"] = tmp_lost
            data[i]["LOST"] = tmp_win

        #print info,'========='
        if info == "胜":
            split_set["WIN"].append(data[i])
        elif info == "负":
            split_set["LOST"].append(data[i])
        elif info == '平':
            split_set["DRAW"].append(data[i])
    return split_set

def format_data_process(data):
    result = ["WIN", "LOST", "DRAW"]
    formatted_data = {}
    formatted_data["WIN"] = []
    formatted_data["DRAW"] = []
    formatted_data["LOST"] = []
    for j in range(len(result)):
        data_cate = data[result[j]]
        cate = result[j]
        for i in range(len(data_cate)):
            single_formatted_data = []
            if data_cate[i]["WIN"] == None or data_cate[i]["WIN"] == "":
                continue
            single_formatted_data.append(float(data_cate[i]["WIN"]))
            single_formatted_data.append(float(data_cate[i]["DRAW"]))
            single_formatted_data.append(float(data_cate[i]["LOST"]))
            formatted_data[cate].append(single_formatted_data)
    return formatted_data

def get_test_data(team):
    file_path = '/Users/francis/Documents/worldCup/data/history/allteam/' + team + '.json'
    file_ori = open(file_path, 'r+')
    file_ori = file_ori.read()
    file_content = json.loads(file_ori)
    test_data_size = len(file_content) / 10
    test_data = file_content[0: test_data_size]
    split_data = split_data_process(test_data, team)
    format_data = format_data_process(split_data)
    return format_data

# 测试的时候开启
#model_train_enter("7")