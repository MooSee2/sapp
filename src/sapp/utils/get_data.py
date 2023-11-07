# from loguru import logger
# from multiprocessing import Pool
import pandas as pd
import requests
import json
import re


def dump_nwis_to_json(path="test_data.json"):
    url = "https://waterservices.usgs.gov/nwis/dv/?sites=12323233&parameterCd=00060&startDT=2023-10-14&endDT=2023-10-21&format=json"
    response = requests.get(url=url)
    jdata = response.json()
    with open(path, mode="w") as f:
        json.dump(jdata, f)


def parse_nwis_json(data) -> pd.DataFrame:
    """Parse json data from nwis into a pandas DataFrame.

    Parameters
    ----------
    data : json
        json data from nwis.

    Returns
    -------
    pd.DataFrame
        The data
    """
    parsed_data = []
    for series in data["value"]["timeSeries"]:
        site_data = series["sourceInfo"]
        site_code = site_data["siteCode"][0]
        variable = series["variable"]
        parsed_data.extend(
            (
                {
                    "value": point["value"],
                    "qualifiers": point["qualifiers"],
                    "dateTime": point["dateTime"],
                    "agencyCode": site_code["agencyCode"],
                    "variableName": variable["variableName"],
                    "unitCode": variable["unit"]["unitCode"],
                    "latitude": site_data["geoLocation"]["geogLocation"]["latitude"],
                    "longitude": site_data["geoLocation"]["geogLocation"]["longitude"],
                    "siteName": site_data["siteName"],
                }
                for point in series["values"][0]["value"]
            )
        )
    return pd.DataFrame(parsed_data)


def query_nwis(service: str, **kwargs) -> pd.DataFrame:
    """Query an nwis service for data.
    Tested services are: "iv", "dv", and "gwlevels"
    kwargs are any valid nwis query parameters.

    Parameters
    ----------
    service : str
        "iv" or "dv" or "gwlevels"

    Returns
    -------
    pd.DataFrame
        The data
    """
    if "sites" in kwargs and isinstance(kwargs["sites"], list):
        kwargs["sites"] = ",".join(kwargs["sites"])

    response = requests.get(
        url=f"https://waterservices.usgs.gov/nwis/{service}",
        params=kwargs,
    )
    return parse_nwis_json(response.json())


""""""


""" 
    # parsed_data is the list to return that will go into df = pd.DataFrame(data)
    parsed_data = []
    for series in data["value"]["timeSeries"]:
        # data is a reference to the json data that has been turned into a python dictionary.
        # We need to go through the list at data["value"]["timeSeries"].
        # These are the different time-series available from the query.
        # Each of them is a dictionary.
        # References to references is faster than making the computer read through each time

        # for point in series["values"][0]["value"]:
        #     parsed_data.append(
        #         {
        #             "value": point["value"],
        #             "qualifiers": point["qualifiers"],
        #             "dateTime": point["dateTime"],
        #             "agencyCode": site_code["agencyCode"],
        #             "variableName": variable["variableName"],
        #             "unitCode": variable["unit"]["unitCode"],
        #             "latitude": site_data["geoLocation"]["geogLocation"]["latitude"],
        #             "longitude": site_data["geoLocation"]["geogLocation"]["longitude"],
        #             "siteName": site_data["siteName"],
        #         }
        #     )
Python list extend can accept generator objects as arguments. 
This means that the list will be extended by the values yielded
by the generator object, without creating an intermediate list. 
However, this also means that the generator object will 
be exhausted after the extend operation, and cannot be reused.

We need a list of dictionaries to pass to pd.DataFrame
to get the data into a format we can easily manipulate.
The dictionary keys will be the column names and the values
will be rows """


# def parser_default_none(data: list, result=None):
#     if result is None:
#         result = []

#     result.extend(data)
#     return tuple(result)


# def parser_default_list(data: list, result: list = []):
#     result.extend(data)
#     return tuple(result)


# def parser_no_default(data: list):
#     result = []
#     result.extend(data)
#     return tuple(result)
