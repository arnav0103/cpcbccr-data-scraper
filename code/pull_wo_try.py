# CPCBCCR Data Scraper – setup_pull.py
# Author: Gurjot Sidhu (github.com/gsidhu)
# Thanks to: Thejesh GN (github.com/thejeshgn)
#
# This script sends the encoded requests to the CPCBCCR server and stores the JSON response in the request_status_data table.

import requests
import json
import sqlite3
import hashlib
import time
import warnings
import base64
warnings.filterwarnings("ignore") # just to ignore the SSL warning

headers = {"Origin": "https://app.cpcbccr.com"}
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
headers["Content-Type"] = "application/x-www-form-urlencoded"
headers["Accept"] = "application/json, text/plain, */*"
headers["Referer"] = "https://app.cpcbccr.com/ccr/"
headers["Connection"] = "keep-alive"
headers["Host"] = "app.cpcbccr.com"
headers["Cookie"] = '_ga=GA1.2.1993625390.1688894903; _gid=GA1.2.673081329.1689148473; _ga_40XB5TDTEW=GS1.2.1689154277.6.1.1689155695.0.0.0; _xsrf=04fb1d3490924e898147d04a4eed95ec; ccr_captcha="dz4tz8nFlrMNyeetnpMKdMh30s6tfz1dJNbqJMSoMx7aIa19SkYgd+L28KemUVRofOkJ4vaK61JGOFGMwUdQLssqAY0QAARMbJv9I4w1LSC4DW8kIEU/QAQQZzz93T6uWPz/PdRVDMX+J8/DQ7a/e5ENJkuiFRzPsk9bCUI7z22xtL5q0OIiAv6Gksyrj4qukH50p6qlx2O+BmjiJPYOe6ZhGqRiPxpiGByUVN3/HjPfgNNgMGZ5mkZILJq3eEIDdJIGvbIR2MClGeDSYkdMWA=="; ccr_public="e+Szwsub63tbgkWcWnxVa9qrSYKu6DPUfpQOIkooMoRetuyd8TAeVYAmI4pyDvE07YcKu7TR9BVypnqPc2iCnhQC4vJKJCn92mXIFNjTxilP47CruPcpnFSNPOMnrRczqe/jRej/6bs5XLgxI2qWFeDEHNNV0yTiJ+LbMqzDS+XV741XaP9AgiDAyMuzX/gX63+9TVCRiJNhM1YJx3VoM9hPXA2bJ8sSQjNQMURYuJ/ceKHMuKYFY7npBkDYFiXaHX7/zWmiBXswSqJ6ydQDDpb/TuysQ1TUVx2+XGIsG2ooPdOA4xnrox3ZnbNoerQU9eHGmtbnbKdx6KO7NKDKhYRLVrzIZWqkoJo6xu4scPE="'
con = sqlite3.connect('../data/db/data.db')
print("Connected")
cur = con.cursor()
query = "SELECT id, encoded_data, status_code FROM request_status_data WHERE status_code = 1 OR status_code = 404 or status_code = 400 or status_code = 504 LIMIT 100"
n = 0
print(n)
while n < 1:
  sample = []
  
  for r in cur.execute(query):
    sample.append(r)

  for row in sample:
    n = row[0]
    print(n)
    encoded_data = row[1]

    r = requests.post(
        "https://app.cpcbccr.com/caaqms/fetch_table_data",
        headers=headers,
        data=encoded_data,
        verify=False, # turning it on hangs the request randomly
      )
    print(r.request.url)


    if r.status_code == 200:
        print("Awesome response code 200")
#        print(r.json)
#        base64_string = base64.b64decode(r.text)
#        print(base64_string)
        t=base64.b64decode(r.text)
        k=eval(eval(str(t).replace('null',"None")))
        json_data = json.dumps(k)
        print(json_data)
#        json_data = json.dumps(eval(eval(str(base64_string).replace('null',"None"))))
        json_data_hash = hashlib.md5(json_data.encode("UTF8"))
        json_data_hash = json_data_hash.hexdigest()
        status_code = r.status_code
    else:
        print("Response code %s", r.status_code)
        json_data = ""
        json_data_hash = ""
        status_code = r.status_code

    print("UPDATING")
    cur.execute("UPDATE request_status_data SET json_data = ?, json_data_hash = ?, status_code = ? WHERE id=?", (json_data, json_data_hash, status_code, row[0]))
    con.commit()


    time.sleep(20)
con.close()
