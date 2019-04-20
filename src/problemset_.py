import requests
import json
#from bs4 import BeautifulSoup

base_dir = "../data/problemset"
base_url = "http://codeforces.com/api/"
problem_subUrl = "problemset.problems"
all_file = "all_data"
url = base_url + problem_subUrl


http_proxy  = "http://10.32.0.1:8080"
https_proxy = "https://10.32.0.1:8080"
ftp_proxy   = "ftp://10.32.0.1:8080"

proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

res = requests.get(url, proxies=proxyDict)

if res.status_code == 200:
    print("Link Got")
raw_data = dict(res.json())

with open(base_dir + all_file + ".csv", "a") as f:
    f.write("contestId, Problem_name, type, rating, tags, level")

if raw_data['status'] == 'OK':
    print("Conform")
    with open(base_dir+all_file, "a") as f:
        for k in raw_data['result']['problems'][:3]:
            print(k)
            '''
            st = ""
            st += str(k['contestID']) + "," + str(k['name']) + "," + str(k['type']) + "," + \
            str(k['rating']) + "," + str(k['tags']) + "," + str(k['index'])
            f.write(st)
'''

