import os
from loguru import logger
from dash import Dash, html
from components.layout import make_layout
from dotenv import load_dotenv
# from flask_cache import Cache

# TODO caching and performance: https://dash.plotly.com/performance

load_dotenv()
logger.debug(f"ENV DATA_SOURCE value:  {os.getenv('DATA_SOURCE')}")

app = Dash(__name__)

app.layout = html.Div(
    children=make_layout(),
    id="first_div",
)
