import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url_base = "https://www.basketball-reference.com/leagues/NBA_2024.html"

html = requests.get(url_base)

parsed_content = bs(html.content, 'html.parser')

table = parsed_content.find_all('table', id='per_game-team')

