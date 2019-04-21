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

with open(base_dir + all_file + ".csv", "w") as f:
    f.write("contestId, Problem_name, type, rating, tags, level\n")

with open(base_dir + "problem_stat"+ ".csv", "w") as f:
    f.write("contestId, level,solvedCount\n")

if raw_data['status'] == 'OK':
    print("Conform")
    with open(base_dir + all_file + ".csv", "a") as f:
        i = 0
        for k in raw_data['result']['problems']:
            #print(k)
            st = ""
            try:
                st += str(k['contestId']).replace(",", "/")
            except KeyError:
                st += "NoID"
            st += ","
            try:
                st += str(k['name']).replace(",", "/")
            except KeyError:
                st += "NoName"
            st += ","
            try:
                st += str(k['type']).replace(",", "/")
            except KeyError:
                st += "NaN"
            st += ","
            try:
                st += str(k['rating']).replace(",", "/")
            except KeyError:
                st += "NaN"
            st += ","
            try:
                st += str(k['tags']).replace(",", "/")
            except KeyError:
                st += "NaN"
            st += ","
            try:
                st += str(k['index']).replace(",", "/")
            except KeyError:
                st += "NaN"

            
            f.write(st+"\n")
            #print(i)
            i += 1
    print(i, " number of rows added in problemsetall_data.csv")
    with open(base_dir + "problem_stat" + ".csv", "a") as f:
        i = 0
        for k in raw_data['result']['problemStatistics']:
            st = ""
            try:
                st += str(k['contestId'])
            except KeyError:
                st += "NoID"
            st += ","
            try:
                st += str(k['index']).replace(",", "/")
            except KeyError:
                st += "NaN"
            st += ","
            try:
                st += str(k['solvedCount'])
            except KeyError:
                st += "NoName"
            f.write(st+"\n")
            #print(i)
            i += 1
    print(i, " number of rows added in problemsetall_data.csv")

