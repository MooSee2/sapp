import tomli
import datetime as dt
from dataclasses import dataclass
from typing import Union


@dataclass
class AppDates:
    wateryear: Union[int, None] = None
    start_pull: Union[str, None] = None
    end_pull: Union[str, None] = None
    start_apportionment: Union[str, None] = None
    start_evaportation: Union[str, None] = None
    now: Union[dt.datetime, None] = None
    _start_apportionment: str = "04-01"
    _start_evaporation: str = "04-15"
    _start_pull: str = "01-01"
    _end_pull: str = "10-31"

    def __post_init__(self):
        if self.now is None:
            self.now = dt.datetime.now()
        if self.wateryear is None:
            self.wateryear = self.now.year
        if self.start_pull is None:
            self.start_pull = f"{self.now.year}-{self._start_pull}"
        if self.end_pull is None:
            self.end_pull = f"{self.now.year}-{self._end_pull}"
        if self.start_apportionment is None:
            self.start_apportionment = f"{self.now.year}-{self._start_apportionment}"
        if self.start_evaportation is None:
            self.start_evaportation = f"{self.now.year}-{self._start_evaporation}"
        self._validate()

    def _validate(self):
        dt.datetime.strptime(str(self.wateryear), "%Y")
        dt.datetime.strptime(self.start_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.end_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.start_apportionment, "%Y-%m-%d")
        dt.datetime.strptime(self.start_evaportation, "%Y-%m-%d")


@dataclass
class AppConfig:
    access: Union[int, None] = 1
    source: Union[str, None] = "nwis"
    realtime: Union[bool, None] = True
    wateryear: Union[int, None] = None
    canal_dates: Union[dict, None] = None
    start_pull: Union[str, None] = None
    end_pull: Union[str, None] = None
    start_apportionment: Union[str, None] = None
    start_evaporation: Union[str, None] = None
    now: Union[dt.datetime, None] = None

    _start_apportionment: str = "04-01"
    _start_evaporation: str = "04-15"
    _start_pull: str = "01-01"
    _end_pull: str = "10-31"

    def __post_init__(self):
        """Assemble default dates if not provided.
        """
        if self.now is None:
            self.now = dt.datetime.now()
        if self.wateryear is None:
            self.wateryear = self.now.year
        if self.start_pull is None:
            self.start_pull = f"{self.wateryear}-{self._start_pull}"
        if self.end_pull is None:
            self.end_pull = f"{self.wateryear}-{self._end_pull}"
        if self.start_apportionment is None:
            self.start_apportionment = f"{self.wateryear}-{self._start_apportionment}"
        if self.start_evaporation is None:
            self.start_evaporation = f"{self.wateryear}-{self._start_evaporation}"
        self._validate_dates()

    def _validate_dates(self):
        """Simple date validation
        """
        dt.datetime.strptime(str(self.wateryear), "%Y")
        dt.datetime.strptime(self.start_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.end_pull, "%Y-%m-%d")
        dt.datetime.strptime(self.start_apportionment, "%Y-%m-%d")
        dt.datetime.strptime(self.start_evaporation, "%Y-%m-%d")

    @classmethod
    def load_config(cls, cfg_path: str):
        """Load config file.

        Parameters
        ----------
        cfg_path : str
            Path to config file.

        Returns
        -------
        AppConfig
            Dataclass containing app configuration.
        """
        with open(cfg_path, mode="rb") as f:
            cfg = tomli.load(f)
        wateryear = cfg.get("wateryear", None)
        access = cfg.get("access", None)
        source = cfg.get("source", None)
        realtime = cfg.get("realtime", None)
        canal_dates = cfg.get("canal_dates", None)
        start_evaporation = cfg.get("start_evaporation", None)

        return cls(
            wateryear=wateryear,
            access=access,
            source=source,
            realtime=realtime,
            canal_dates=canal_dates,
            start_evaporation=start_evaporation,
        )

    def make_dates(self):
        if self.now is None:
            self.now = dt.datetime.now()
        if self.wateryear is None:
            self.wateryear = self.now.year
        if self.start_pull is None:
            self.start_pull = f"{self.wateryear}-{self._start_pull}"
        if self.end_pull is None:
            self.end_pull = f"{self.wateryear}-{self._end_pull}"
        if self.start_apportionment is None:
            self.start_apportionment = f"{self.wateryear}-{self._start_apportionment}"
        if self.start_evaporation is None:
            self.start_evaporation = f"{self.wateryear}-{self._start_evaporation}"
        self._validate_dates()


def test_AppConfig_happy():
    cfg = AppConfig(
        wateryear=2020,
        access=2,
        source="source",
        realtime=False,
    )
    assert cfg.wateryear == 2020
    assert cfg.access == 2
    assert cfg.source == "source"
    assert cfg.realtime is False
    assert cfg.start_pull == "2020-01-01"
    assert cfg.end_pull == "2020-10-31"


def test_AppConfig_make_dates():
    cfg = AppConfig.load_config(cfg_path="tests/test_data/test_config.toml")
    cfg.make_dates()
    assert cfg.start_pull == "2022-01-01"
    assert cfg.end_pull == "2022-10-31"
    assert cfg.source == "nwis"
    assert cfg.wateryear == 2022
    assert cfg.access == 1


def test_AppConfig_defaults():
    cfg = AppConfig()
    assert cfg.wateryear == dt.datetime.now().year
    assert cfg.access == 1
    assert cfg.source == "nwis"
    assert cfg.realtime is True


def test_AppConfig_partial_defaults():
    cfg = AppConfig(wateryear=2024)
    assert cfg.wateryear == 2024
    assert cfg.realtime is True


# def test_AppDates_make_dates_happy():
#     dates = AppDates(2023)
#     assert dates.wateryear == 2023
#     assert dates.start_pull == "2023-01-01"
#     assert dates.end_pull == "2023-10-31"


# def test_AppDates_make_dates_defaults():
#     dates = AppDates(
#         wateryear=None,
#         start_evaportation="2023-04-20",
#     )
#     assert dates.wateryear == 2023
#     assert dates.start_pull == "2023-01-01"
#     assert dates.end_pull == "2023-10-31"
#     assert dates.start_apportionment == "2023-04-01"
#     assert dates.start_evaportation == "2023-04-20"


# url = "https://waterservices.usgs.gov/nwis/gwlevels/?format=json&sites=433613110443501,433615110440001&startDT=2022-01-01&endDT=2023-10-26&siteStatus=all&agencyCd=USGS"
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
# def test_parser_default_none():
#     expected = (1, 2, 3, 4)
#     input_data = [1, 2, 3, 4]
#     output1 = gd.parser_default_none(input_data)
#     output2 = gd.parser_default_none(input_data)
#     output3 = gd.parser_default_none(input_data)
#     output4 = gd.parser_default_none(input_data)

#     assert output1 == expected
#     assert output2 == expected
#     assert output3 == expected
#     assert output4 == expected


# def test_parser_default_list():
#     expected1 = (1, 2, 3, 4)
#     expected2 = (1, 2, 3, 4, 1, 2, 3, 4)
#     expected3 = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
#     expected4 = (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

#     input_data = [1, 2, 3, 4]
#     output1 = gd.parser_default_list(input_data)
#     output2 = gd.parser_default_list(input_data)
#     output3 = gd.parser_default_list(input_data)
#     output4 = gd.parser_default_list(input_data)

#     assert output1 == expected1
#     assert output2 == expected2
#     assert output3 == expected3
#     assert output4 == expected4


# def test_parser_no_default():
#     expected = (1, 2, 3, 4)
#     input_data = [1, 2, 3, 4]
#     output1 = gd.parser_no_default(input_data)
#     output2 = gd.parser_no_default(input_data)
#     output3 = gd.parser_no_default(input_data)
#     output4 = gd.parser_no_default(input_data)

#     assert output1 == expected
#     assert output2 == expected
#     assert output3 == expected
#     assert output4 == expected
