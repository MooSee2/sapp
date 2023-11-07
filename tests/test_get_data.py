from src.sapp.utils import get_data as gd


def test_parse_nwis_json():
    data = gd.parse_nwis_json()
    return


def test_query_nwis_gwlevels_1sites():
    data = gd.query_nwis(
        "gwlevels",
        format="json",
        sites="433613110443501",
        startDT="2022-01-01",
        endDT="2023-10-26",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 15


def test_query_nwis_gwlevels_2sites():
    data = gd.query_nwis(
        "gwlevels",
        format="json",
        sites=["433613110443501", "433615110440001"],
        startDT="2022-01-01",
        endDT="2023-10-26",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 36


def test_query_nwis_dv_1sites_q():
    data = gd.query_nwis(
        "dv",
        format="json",
        sites="12323233",
        startDT="2022-01-01",
        endDT="2022-01-15",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 15


def test_query_nwis_dv_2sites_q():
    data = gd.query_nwis(
        "dv",
        format="json",
        sites=["12323233", "12323242"],
        startDT="2022-01-01",
        endDT="2022-01-15",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 30


def test_query_nwis_dv_1sites_q_turb_temp():
    data = gd.query_nwis(
        "dv",
        format="json",
        sites="12323233",
        startDT="2022-7-01",
        endDT="2022-07-15",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 93


def test_query_nwis_dv_2sites_q_turb_temp():
    data = gd.query_nwis(
        "dv",
        format="json",
        sites=["12323233", "12323242"],
        startDT="2022-7-01",
        endDT="2022-07-15",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 180


def test_query_nwis_iv_1sites_q():
    data = gd.query_nwis(
        "iv",
        format="json",
        sites="12323233",
        startDT="2022-1-01",
        endDT="2022-01-02",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 384


def test_query_nwis_iv_2sites_q():
    data = gd.query_nwis(
        "iv",
        format="json",
        sites=["12323233", "12323242"],
        startDT="2022-1-01",
        endDT="2022-01-02",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 768


def test_query_nwis_iv_1sites_q_turb_temp():
    data = gd.query_nwis(
        "iv",
        format="json",
        sites="12323233",
        startDT="2022-07-01",
        endDT="2022-07-02",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 768


def test_query_nwis_iv_2sites_q_turb_temp():
    data = gd.query_nwis(
        "iv",
        format="json",
        sites=["12323233", "12323242"],
        startDT="2022-07-01",
        endDT="2022-07-02",
        siteStatus="all",
        agencyCd="USGS",
    )
    assert data.empty is False
    assert len(data) == 1422


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
