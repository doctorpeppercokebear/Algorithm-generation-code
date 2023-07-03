import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

with open("C:/Users/user/머신러닝/딥러닝/배추예상/가을배추.html", "r") as file:
    html_data = file.read()
