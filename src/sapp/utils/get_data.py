# from loguru import logger
import pandas as pd
import requests
import json


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

