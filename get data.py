# Note that the last line in the cinema_links data set is empty, this needs to be resolved.
# Note that the postal codes might be incorrect. Maybe delete all postal codes containing letters.

import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import pandas 

def remove_tags(soup): #Removes tags from the description
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

my_index = 1
max_results = 13828

url_stub = "http://cinematreasures.org"

# header = ("name," + "street_address," + "city," + "state," + "status," + "description," + "\n")

my_cols = ("name", "street_address", "city", "state", "postal_code", "status", "description", "url")

# file = open('cinematreasures_raw_v1.csv', "w")
# file.write(header)
# file.close()

my_data = list()

with open("cinema_links_1947_ACCEPT.csv", "r") as a_file:
    for line in a_file:

        stripped_line = line.strip()

        # print(stripped_line)

        url = url_stub + stripped_line

        r = requests.get(url)

        soup = BeautifulSoup(r.content, 'html.parser')

        # Variables to get: Name, Street, City (Locality), State (Region), Postal Code, Status, Description, URL

        # Theater name
        try:
            my_name = soup.findAll("h1")[0].text
        except:
            my_name = " "
        # print(my_name)

        # Street address
        try:
            my_street = soup.findAll("div", {"class": "street-address"})[0].text.replace(",", "")
        # print(my_street)
        except:
            my_street = " "

        # City (locality)
        try:
            my_city = soup.findAll("span",
                                   {"class": "locality"})[0].text.replace(",", "").replace("\n", "").lstrip().rstrip()
        except:
            my_city = " "
        # print(my_city)

        # State (region)
        try:
            my_state = soup.findAll("span", {"class": "region"})[0].get_text()
        except:
            my_state = " "
        # print(my_state)

        # Postal code
        try:
            my_postcode = soup.findAll("span", {"class": "postal-code"})[0].get_text()
        except:
            my_postcode = " "

        # Status
        try:
            my_status = soup.findAll("div", {"id": "facts"})[0].contents[1].text
        except:
            my_status = " "
        # print(my_status)

        # Description
        try:
            my_descr = soup.findAll("div", {"id": "description"})[0]
            my_descr = remove_tags(my_descr)
        except:
            my_descr = " "
        # print(my_descr)

        # URL
        try:
            my_url = r.url
        except:
            my_url = " "

        new_row = (my_name, my_street, my_city, my_state, my_postcode, my_status, my_descr, my_url)

        my_data.append(new_row)
        # print(my_data)

        my_index += 1

        if my_index > max_results:
            print("Reached max")
            break

        print("Page " + str(my_index) + " of " + str(max_results))

df = pandas.DataFrame(data=my_data, columns=my_cols)

df.to_csv("cinematreasures_1947_data.csv", sep=";", index=False)