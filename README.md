# CPCBCCR Data Scraper
Scrapes data from CPCB's CCR dashboard.

## Disclaimer
The work in this repo builds on top of the [work done by Gurjot](https://github.com/gsidhu/cpcbccr-data-scraper). I take no responsibility for their work. Please contact individual authors for any queries. In this repo I wanted to get teh yearly data from the cpcbccr ste. So the setup_pull.py has been modified accordingly for the query.

## Code
This code uses the [`data.db`](./data/db/data.db) file for everything. 

First order of business is to set up the **sites** table in the db.

### 1. How to set up sites in DB
**Add your sites to CSV**

1. Go to [CPCB's CCR website](https://app.cpcbccr.com/AQI_India/) and select the state, city and station of your choice.
2. Open the Network tab in Dev Tools.
3. In the Network tab, click on the request called `aqi_all_Paramters`. Under the Payload tab, copy the Form Data and put it in a XML decoder. This would look something like -> {"station_id":"site_301","date":"2023-07-12T22:00:00Z"}
4. Edit [`sites.csv`](./sites.csv) and add the station_id.
5. Leave the header row as is. Leave the remaining columns blank.
{ Note -> To create various site_<state>.xls file -> I picked up the Stations.xls from [ccpb site] (https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing). Picked up the state and Station Name from there. Added it in the required format in site_<state>.xls and then added the station id.

**Add the sites data to db**
1. Download and install a tool like [DB Browser for SQLite](https://sqlitebrowser.org/)
2. Open the [`data.db`](./data/db/data.db) file using DB Browser
3. Click on Import > Table from CSV and select the `site_<state>.csv` file from before. 
4. Copy data in columns -> params, params_query, params_ids and data_availability from sites.xls to teh new sites_<state.xls>

### 2. Scrape the data
Now that your sites are set up, you can begin to scrape data.

0. Use python3 and install the `requests`, `dataset` and `sqlite3` modules using pip. (Ideally inside a [virtualenv](https://python.land/virtual-environments/virtualenv) using [`requirements.txt`](./requirements.txt))

Run the following scripts in the given order –
1. Open`setup_pull.py`: edit this script to setup the dates for which you need to get data ([lines 37-39](./code/setup_pull.py#L37)); running this script sets up all the requests that needs to be called to pull the data. Edit the xls file to point to the correct site_<state>.xls. Run it
2. `pull_wo_try.py`: pulls the data setup in the previous script; data received is a JSON. Remember to change the "Cookie" in this script.
To get Cookie -> Open [CPCB site](https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data). Fill form. Run Submit. In Network tab, from headers tab, pick teh cookie and paste in the file.
6. `parse.py`: parses the JSON data and creates the final **data** table in db

## Notes
While all scripts should run quite swiftly, `pull_wo_try.py` is going to be the slowest. Pinging the CPCB server takes time so be patient. And be kind and leave some timeout between subsequent pings. If you see timeouts, stop the script. Recheck if cookie has changed and re-run.

You can browse the data for all stations in Delhi, Mumbai and Chennai from 01-01-2010 till 31-12-2020 in the [reports](./data/reports/) directory. No need to fetch that again.

## License
- This code is licensed under GNU GPL v3.
- Please credit by linking to https://thatgurjot.com and https://thejeshgn.com
