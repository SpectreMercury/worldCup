import urllib2
import json
import time

def get_country_data():
  file_ori = open("/Users/francis/Documents/worldCup/data/country.json", "r+")
  #file_ori.close()
  #all_team = json.loads(file_ori)
  all_team = json.load(file_ori)
  for team in all_team:
    team_str = str(team)
    url = "http://liansai.500.com/index.php?c=teams&a=ajax_fixture&records=100&8&hoa=0&tid=" + team_str
    get_request(url, team_str)
    time.sleep(2)



def get_request(url, team):
  resp = urllib2.Request(url)
  resp = urllib2.urlopen(resp)
  resp = resp.read()
  resp = json.loads(resp)
  resp = list_filter(resp["list"])
  resp = json.dumps(resp)
  file_path = '/Users/francis/Documents/worldCup/data/history/allteam/' + team + '.json'
  create_file(file_path)
  file_ori = open(file_path,'r+')
  file_ori.write(resp)
  file_ori.close()
  

def list_filter(data):
  filter_data = []
  data_len = len(data)
  for i in range(data_len):
    single_info = {}
    single_data = data[i]
    single_info["AWAYTEAMID"] = single_data["AWAYTEAMID"]
    single_info["FIXTUREID"] = single_data["FIXTUREID"]
    single_info["HOMETEAMID"] = single_data["HOMETEAMID"]
    single_info["MATCHID"] = single_data["MATCHID"]
    single_info["WIN"] = single_data["WIN"]
    single_info["DRAW"] = single_data["DRAW"]
    single_info["LOST"] = single_data["LOST"]
    single_info["lpl_on"] = single_data["lpl_on"]
    filter_data.append(single_info)
  return filter_data


def create_file(file_path):
  file_ori = open(file_path, 'w')
  file_ori.close()


get_country_data()