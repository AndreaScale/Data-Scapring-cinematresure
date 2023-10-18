import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import pandas 

# We create a new data set containg only the movie theaters we belive to be open in 1947. 

def remove_tags(soup): #Removes tags from the description
 
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

# Create two new datasets, accepted theaters and to be manually checked

accepted = open('cinema_links_1947_ACCEPT.csv',"w")
accepted.close()

# to_check = open('cinema_links_1947_CHECK.csv',"w") 
# to_check.close()


# Open the old one and inspect all of the cinemas

my_links_accep = list()
# my_links_check = list()

url_stub = "http://cinematreasures.org"

my_theater = 0

with open("cinema_links_v1.csv", "r") as a_file:
    for line in a_file:

        stripped_line = line.strip()
        url = url_stub + stripped_line

        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        my_descr = soup.findAll("div", {"id": "description"})[0]
        my_descr = remove_tags(my_descr)

        if "opened" in my_descr or "opening" in my_descr or "Opened" in my_descr or "Opening" in my_descr:
            
            print(my_descr)

            numbers_str = re.findall(r'\b\d+\b', my_descr)
            numbers = [int(x) if x.isdigit() else float(x) for x in numbers_str]
            dates = [x for x in numbers if 1800<=x<=2100]

            print(dates)
            
            # if dates==[]: 
            #     my_links_check.append(stripped_line)
            #     print('To be checked ' + stripped_line)
            if len(dates)==1: #If there's only one number (between 1800 and 2100) which is less than 1947 we consider it to be open in 1947
                if dates[0]<=1947: 
                    my_links_accep.append(stripped_line)
                    print(stripped_line)
            if dates!=[] and min(x for x in dates)<=1947<=max(x for x in dates): #If min e max contengono 1947 we store it
                my_links_accep.append(stripped_line) 
                print(stripped_line)

        print("Theater " + str(my_theater))
        my_theater += 1
        time.sleep(3)


           
# my_links_check = list(dict.fromkeys(my_links_check))
my_links_accep = list(dict.fromkeys(my_links_accep))

file_acc = open('cinema_links_1947_ACCEPT.csv',"a")

for link in my_links_accep:
    new_line = link + "\n"
    file_acc.write(new_line)

file_acc.close()

# file_check = open('cinema_links_1947_CHECK.csv',"a")

# for link in my_links_check:
#     new_line = link + "\n"
#     file_check.write(new_line)

# file_check.close()