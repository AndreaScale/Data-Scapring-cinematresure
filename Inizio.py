import requests
from bs4 import BeautifulSoup
import re
import time


# First Part: Get all links of cinemas in the US stored 
file = open('cinema_links_v1.csv', "w")
file.close()

my_links = list()

max_pages = 1301

my_page = 1

url_stub = "http://cinematreasures.org/theaters/united-states?status=all&page="


while my_page <= max_pages:

    url = url_stub + str(my_page)

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')


    refs = soup.find_all('a')                            #find all numbers of the cinemas
    for i in refs:                                       #loop on all the possible cinemas
        if i.has_attr('href'):                           #select only those which have href, that is only cinemas
            if re.match(r"/theaters/[0-9]+", i['href']): #select those which are actually cinemas
                #print(i['href'])
                my_links.append(i['href'])

    my_page += 1
    #time.sleep(3)
    #print("Now starting with page:" + str(my_page))

my_links = list(dict.fromkeys(my_links))

file = open('cinema_links_v1.csv', "a")

for link in my_links:
    new_line = link + "\n"
    file.write(new_line)

file.close()