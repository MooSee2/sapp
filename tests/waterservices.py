import requests
import pandas as pd
import json
from dataclasses import dataclass
from models import WaterServiceModel
import dataclass_wizard as dw


class WaterServiceAdapter:
    def __init__(self, service: str) -> None:
        self.__model = WaterServiceModel
        self._url = f"https://waterservices.usgs.gov/nwis/{service}"
        self._data = None

    def _get(self, params: dict) -> None:
        if "sites" in params and isinstance(params["sites"], list):
            params["sites"] = ",".join(params["sites"])

        response = requests.get(self._url, params=params)

        if response.status_code >= 200 and response.status_code <= 299:
            self.data = response.json()
        raise Exception(f"Error: {response.url}")

    def _load_model(self):
        data = dw.fromdict(self.__model, self._data)
        self._data = data
        return None

    # def _parse_data(self):
    #     """Parse json data from nwis into a pandas DataFrame.

    #     Parameters
    #     ----------
    #     data : json
    #         json data from nwis.

    #     Returns
    #     -------
    #     pd.DataFrame
    #         The data
    #     """
    #     parsed_data = []
    #     for series in self.data["value"]["timeSeries"]:
    #         site_data = series["sourceInfo"]
    #         site_code = site_data["siteCode"][0]
    #         variable = series["variable"]
    #         parsed_data.extend(
    #             (
    #                 {
    #                     "value": point["value"],
    #                     "qualifiers": point["qualifiers"],
    #                     "dateTime": point["dateTime"],
    #                     "variableName": variable["variableName"],
    #                     "latitude": site_data["geoLocation"]["geogLocation"]["latitude"],
    #                     "longitude": site_data["geoLocation"]["geogLocation"]["longitude"],
    #                     "siteName": site_data["siteName"],
    #                 }
    #                 for point in series["values"][0]["value"]
    #             )
    #         )
    #     return parsed_data

    def _to_pandas(self):
        return pd.DataFrame(self._data)

    def get(self, params: dict) -> dict:
        self._get(params=params)
        # return self._to_pandas()
        return self._load_model()


class LocalJsonAdapter:
    def __init__(self, *args, **kwargs) -> None:
        self.__model = WaterServiceModel

    def _get(self, *args, **kwargs):
        with open("tests/test_data/test_data.json", "r") as f:
            return json.load(f)

    def _load_model(self, data):
        return dw.fromdict(self.__model, data)

    def to_pandas(self, data) -> pd.DataFrame:
        return pd.DataFrame(data)

    def get(self, *args, **kwargs) -> dict:
        data = self._get()
        return self._load_model(data)
        # return self._to_pandas()


class Rivers:
    def __init__(self, service: str, adapter) -> None:
        self._waterservice = adapter(service=service)
        self.data = None
        self.url = None

    def get(self, params: dict):
        data = self._waterservice.get(params=params)
        return


params = {
    "sites": "12323233",
    "startDt": "2023-05-01",
    "endDt": "2023-05-05",
    "parameterCd": "00060",
    "format": "json",
}
mary_EC_WC = Rivers("dv", adapter=LocalJsonAdapter)
my_data = mary_EC_WC.get(params=params)
mouse = 2

# def parse_data(self):
#     """Parse json data from nwis into a pandas DataFrame.

#     Parameters
#     ----------
#     data : json
#         json data from nwis.

#     Returns
#     -------
#     pd.DataFrame
#         The data
#     """
#     parsed_data = []
#     for series in self.data["value"]["timeSeries"]:
#         site_data = series["sourceInfo"]
#         site_code = site_data["siteCode"][0]
#         variable = series["variable"]
#         parsed_data.extend(
#             (
#                 {
#                     "value": point["value"],
#                     "qualifiers": point["qualifiers"],
#                     "dateTime": point["dateTime"],
#                     "variableName": variable["variableName"],
#                     "latitude": site_data["geoLocation"]["geogLocation"]["latitude"],
#                     "longitude": site_data["geoLocation"]["geogLocation"]["longitude"],
#                     "siteName": site_data["siteName"],
#                 }
#                 for point in series["values"][0]["value"]
#             )
#         )
#     return parsed_data
