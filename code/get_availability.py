# CPCBCCR Data Scraper – get_availability.py
# Author: Gurjot Sidhu (github.com/gsidhu)
# Thanks to: Thejesh GN (github.com/thejeshgn)
#
# This script gets the list of months for which data is available for a certain site and stores it the data_availability column in the sites table of the db.
# This data is parsed using check_availability.py

import requests
import dataset
import json
import base64

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    'Accept': 'q=0.8;application/json;q=0.9',
    'Accept-Language': 'en-GB,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://app.cpcbccr.com/ccr/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://app.cpcbccr.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'TE': 'trailers',
    'Cookie' : '_ga=GA1.2.330110338.1689056954; _gid=GA1.2.1756499807.1689056954; _ga_40XB5TDTEW=GS1.2.1689058995.2.1.1689060166.0.0.0; ccr_captcha="2+42Qgole10ioTtRQt1q18TRHNXcPtjya7VK0R6c3xToGxfIxUhxg9n/j5j8ukKH8VuMQ+MBQlJ0ridO8It5voD0Eq0fEJPKy7WoAcK5OnoYSzzYBcvPFOQVCjevZdFX2JRPQaQ/+b3/qTWHJMZZpF8W/icVyZ0wUaIMI/OcIdrENHbO9xnJV6GO8pHXKR9YgbMGKkHxmyzzOICSlL1z4dj7MgDnBIw1Yb4tsSiUzFAuhMFq1Yeqbf6EYMVvbHD5uW/HisKhk9t8nYbqYyxgCg=="; ccr_public="TopoB5rHZLDv5v83vpunNSMCUZA70zol1fyVpxYaXQnB6w+UKgYz8SGmvCZz+vO+ZevpaJ+FGcXP1qGzOLs9L/rTfawGHHP8S1+QmiGxS0ksjIvrkrg57b9QiYQExC9wiJSEAafvGShgLLFMSYnXOLL1h/4DirmgIXw1ArQr+Mc0BchEqdhOOyC0IORsP55lDrED69DBn2Irw/zpNwG3tEj1UHc2I5NcXEqcOpCObw7jqZI+QW9lGWeps0uVUXgJWzBaRPAOG9099VVFh+onBeFRs0+ID1JTBCi0dwafAjowRFRit7m1LvWI0db65YbodtEn1TAdyB9Ujzxmy7ern13Xkc/uniMa7+0Lup9AWmk="; _xsrf=ba382b26ab7644c494d8c1530fb8f742'
}

db = dataset.connect("sqlite:///../data/db/data.db")
site_table = db["sites"]

for site_row in site_table:
    site = site_row["site"]
    state = site_row["state"]
    city = site_row["city"]
    print(site)
    query = {"state": state, "city": city, "station_id": site}
    data = base64.b64encode(str(query).replace("'", '"').encode("UTF8"))

    response = requests.post('https://app.cpcbccr.com/caaqms/Year_summarization', headers=headers, data=data)

    raw_json = json.dumps(eval(base64.b64decode(response.text)))
    site_row["data_availability"] = raw_json
    site_table.update(site_row, ["site"])

db.commit()
