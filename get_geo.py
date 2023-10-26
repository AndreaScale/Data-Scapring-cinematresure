import geocoder # pip install geocoder
import pandas
import numpy
import plotly.express as px
import json

file = pandas.read_excel('cinematreasures_1947_data.xlsx')


addresses = []
no_address = []
no_city = []
no_state = []
for i in range(1,13827): 
    if file['street_address'][i] == " ": no_address += [[i,file['name'][i]]]
    if file['city'][i] == " ": no_city += [[i,file['name'][i]]]
    if file['state'][i] == " ": no_state += [[i,file['name'][i]]]
    else: addresses += [[file['name'][i] + ", " + str(i), file['street_address'][i] + ', ' + file['city'][i] + ', ' + file['state'][i]]]



# print(no_address)
# print(no_city)
# print(no_state)

# print("The cinemas without address are:")
# print(numpy.size(addresses,0))

coordinates = []
county = []
lat = []
lng = []
i = 0
n = numpy.size(addresses,0)
for i in range(0,13824):
    g = geocoder.bing(addresses[i][1], key='AkJEePEi3Se7CEInH-99-V6M5ZpmxsBk-OK5HKBLzpxkylj2_mPJBNZ2j2t7fjYC')
    results = g.json
    if not (results is None): 
        lat += [results['lat']]
        lng += [results['lng']]
        if 'adminDistrict2' in list(results['raw']['address'].keys()): county += [[addresses[i][0],results['raw']['address']['adminDistrict2']]]
        coordinates += [[addresses[i][0], results['lat'],results['lng']]]
        print(str(i) + "/" + str(n) + " - name, number in csv: " + str(addresses[i][0]))


df1 = pandas.DataFrame(coordinates, columns=['Movie theater','Lat','Lng'])
print(df1)

dataset1 = open("coord.html","w")
dataset1.write(pandas.DataFrame.to_html(df1))
dataset1.close()

df2 = pandas.DataFrame(county, columns=['Movie theater','county'])
print(df2)

dataset2 = open("counties.html","w")
dataset2.write(pandas.DataFrame.to_html(df2))
dataset2.close()

# print(coordinates)
# print(county)

#Updating dataset

file['lat'] = lat
file['lng'] = lng
file['county'] = county

file = file[['name', 'street_address', 'city', 'state', 'postal_code', 'lat', 'lng', 'county', 'status', 'description', 'url']]
file.to_csv("cinematreasures_1947_data_coord.csv", sep=";", index=False)
print(file)

#Dataset for map 

df = pandas.DataFrame(coordinates, columns=['Movie theater,Lat,Lng'])
print(df)

dataset = open("Dataset_map.html","w")
dataset.write(pandas.DataFrame.to_html(df))
dataset.close()





# g = geocoder.bing('1600 Buchanan Street, Little Chute, WI', key='AkJEePEi3Se7CEInH-99-V6M5ZpmxsBk-OK5HKBLzpxkylj2_mPJBNZ2j2t7fjYC')
# results = g.json
# print(results)
# print(results['raw']['address']['adminDistrict2'])
# # del results["address"]
# # print(results)
# # print(results['address']['adminDistrict2'])
# # print(results['address': 'addressLine'])
# # print(results['address'][1])
# # print(results['address'][2])
# # print(results['address'][3]