from dash import html, dcc


def make_layout():
    return [
        html.Div(
            children="Hello World1",
            style={"width": "100%", "height": "50px"},
            id="box1",
            className="box1",
        ),
        html.Div(
            children="Hello World2",
            style={"width": "100%", "height": "50px"},
            id="box2",
            className="box",
        ),
        html.Div(
            children="Hello World3",
            style={"width": "100%", "height": "50px"},
            id="box3",
            className="box",
        ),
        html.Div(
            children="Hello World4",
            style={"width": "100%", "height": "50px"},
            id="box4",
            className="box",
        ),
        html.P(
            children=["mouse"],
            id="out",
        ),
        html.Button(
            "A Button",
            id="in",
        ),
        html.Button(
            id="signal",
            style={"display": "none"},
        ),
    ]
