import requests
import multiprocessing
import pandas as pd
import json

def get_nwis():
    url = "https://waterservices.usgs.gov/nwis/dv/?sites=12323233&parameterCd=00060&startDT=2023-10-14&endDT=2023-10-21&format=json"
    response = requests.get(url=url)
    jdata = response.json()
    with open("test_data.json", mode="w") as f:
        json.dump(jdata, f)
