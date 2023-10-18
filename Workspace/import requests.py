import requests
from bs4 import BeautifulSoup
import re
import time
import csv


# First Part: Get all links of cinemas in the US stored 


with open('B1.1 - Journal de classe - 05 10 2023.csv') as topo:
    
    print(topo.read())