from dash import Input, Output, dcc, callback


@callback(
    Output("out", "data"),
    Input("in", "value"),
)
def test_callback(data):
    pass
