import requests
from bs4 import BeautifulSoup
import re
import time
import pandas 
import csv

def remove_tags(soup): #Remove tags from the description
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


url = "https://cinematreasures.org/theaters/1066"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

my_descr = soup.findAll("div", {"id": "description"})[0]

print(my_descr)

my_descr = remove_tags(my_descr)

print(my_descr)

numbers_str = re.findall(r'\b\d+\b', my_descr)

print(numbers_str)

numbers = [int(x) if x.isdigit() else float(x) for x in numbers_str]

print(numbers)

# dates = [x for x in numbers if 1800<=x<=2100]

# y = [1,2,3]

# z =[x for x in y if 1800<=x<=2100]
# print(y)
# print(z)

# print(dates)

# print(type(dates))

# #print(my_descr)

# if "opened" in my_descr or "oepening" in my_descr:
#     print("Yep")
# else:
#     print("Nop")