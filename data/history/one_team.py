import urllib2
import json
import time

FIXTUREID_STR = ''
team = "6"
def enter():
  global FIXTUREID_STR
  global team
  file_path = '/Users/francis/Documents/worldCup/data/history/allteam/' + team + '.json'
  file_content = open(file_path, 'r+')
  file_content = file_content.read()
  file_content = json.loads(file_content)
  FIXTUREID_STR = find_match(file_content, FIXTUREID_STR)
  data_path = 'http://liansai.500.com/index.php?c=teams&a=ajax_pl&cid=293&hoa=0&fids=' + FIXTUREID_STR
  result_williamhill = get_williamhill(data_path)
  change_result(file_content, result_williamhill)
  #print result_williamhill
  #print file_content

def find_match(data, FIXTUREID_STR):
  #print type(data)
  for i in data:
    FIXTUREID_STR = FIXTUREID_STR + i["FIXTUREID"] + ','
  return FIXTUREID_STR

def get_williamhill(url):
  new_williamhill = {}
  resp = urllib2.Request(url)
  resp = urllib2.urlopen(resp)
  resp = resp.read()
  resp = json.loads(resp)
  resp = resp["list"]
  #resp = json.dumps(resp)
  for i in resp:
    key = str(i["FIXTUREID"])
    new_williamhill[key] = i
  return new_williamhill

def change_result(ori_result, willam_result):
  for i in ori_result:
    key = str(i["FIXTUREID"])
    if willam_result.has_key(key):
      i["WIN"] = willam_result[key]["WIN"] 
      i["DRAW"] = willam_result[key]["DRAW"]
      i["LOST"] = willam_result[key]["LOST"]
  ori_result = json.dumps(ori_result)
  file_path = '/Users/francis/Documents/worldCup/data/history/team/william_hill/' + team + '.json'
  create_file(file_path)
  file_content = open(file_path, 'r+')
  file_content.write(ori_result)
  file_content.close()

def create_file(file_path):
  file_ori = open(file_path, 'w')
  file_ori.close()

enter()