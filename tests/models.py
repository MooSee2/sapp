from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TimeParam:
    begin_date_time: Optional[datetime] = None
    end_date_time: Optional[datetime] = None


@dataclass
class Criteria:
    location_param: Optional[str] = None
    variable_param: Optional[str] = None
    time_param: Optional[TimeParam] = None
    parameter: Optional[list[str]] = None


@dataclass
class Note:
    value: Optional[str] = None
    title: Optional[str] = None


@dataclass
class QueryInfo:
    query_url: Optional[str] = None
    criteria: Optional[Criteria] = None
    note: Optional[list[Note]] = None


@dataclass
class GeogLocation:
    srs: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class GeoLocation:
    geog_location: Optional[GeogLocation] = None
    local_site_xy: Optional[list[str]] = None


@dataclass
class SiteCode:
    value: Optional[int] = None
    network: Optional[str] = None
    agency_code: Optional[str] = None


@dataclass
class SiteProperty:
    value: Optional[str] = None
    name: Optional[str] = None


@dataclass
class TimeZone:
    zone_offset: Optional[str] = None
    zone_abbreviation: Optional[str] = None


@dataclass
class TimeZoneInfo:
    default_time_zone: Optional[TimeZone] = None
    daylight_savings_time_zone: Optional[TimeZone] = None
    site_uses_daylight_savings_time: Optional[bool] = None


@dataclass
class SourceInfo:
    site_name: Optional[str] = None
    site_code: Optional[list[SiteCode]] = None
    time_zone_info: Optional[TimeZoneInfo] = None
    geo_location: Optional[GeoLocation] = None
    note: Optional[list[str]] = None
    site_type: Optional[list[str]] = None
    site_property: Optional[list[SiteProperty]] = None


@dataclass
class Method:
    method_description: Optional[str] = None
    method_id: Optional[int] = None


@dataclass
class Qualifier:
    qualifier_code: Optional[str] = None
    qualifier_description: Optional[str] = None
    qualifier_id: Optional[int] = None
    network: Optional[str] = None
    vocabulary: Optional[str] = None


@dataclass
class ValueValue:
    value: Optional[str] = None
    qualifiers: Optional[list[str]] = None
    date_time: Optional[datetime] = None


@dataclass
class TimeSeryValue:
    value: Optional[list[ValueValue]] = None
    qualifier: Optional[list[Qualifier]] = None
    quality_control_level: Optional[list[str]] = None
    method: Optional[list[Method]] = None
    source: Optional[list[str]] = None
    offset: Optional[list[str]] = None
    sample: Optional[list[str]] = None
    censor_code: Optional[list[str]] = None


@dataclass
class Option:
    name: Optional[str] = None
    option_code: Optional[str] = None


@dataclass
class Options:
    option: Optional[list[Option]] = None


@dataclass
class Unit:
    unit_code: Optional[str] = None


@dataclass
class VariableCode:
    value: Optional[str] = None
    network: Optional[str] = None
    vocabulary: Optional[str] = None
    variable_id: Optional[int] = None
    default: Optional[bool] = None


@dataclass
class Variable:
    oid: Optional[int] = None
    variable_code: Optional[list[VariableCode]] = None
    variable_name: Optional[str] = None
    variable_description: Optional[str] = None
    value_type: Optional[str] = None
    unit: Optional[Unit] = None
    options: Optional[Options] = None
    note: Optional[list[str]] = None
    no_data_value: Optional[int] = None
    variable_property: Optional[list[str]] = None


@dataclass
class TimeSery:
    source_info: Optional[SourceInfo] = None
    variable: Optional[Variable] = None
    values: Optional[list[TimeSeryValue]] = None
    name: Optional[str] = None


@dataclass
class WaterServiceModelValue:
    query_info: Optional[QueryInfo] = None
    time_series: Optional[list[TimeSery]] = None


@dataclass
class WaterServiceModel:
    name: Optional[str] = None
    declared_type: Optional[str] = None
    scope: Optional[str] = None
    value: Optional[WaterServiceModelValue] = None
    nil: Optional[bool] = None
    global_scope: Optional[bool] = None
    type_substituted: Optional[bool] = None
