# Dublin Bikes API Scraper

This is a simple API scraper for the availability data of Dublin Bikes.

***

## Installation  

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dbikesScraper.

```bash
pip install git+"https://github.com/yik000/dublinBikes_scraper.git"
```

***

## Usage
Create `dbinfo.py` file in `~/miniconda3/envs/enviroment/bin/dbikes_scraper` with database URI, database PASS, database USER and APIKEY.

Run module in the background.

```bash
dbikes_scraper >/dev/null &
```

***
