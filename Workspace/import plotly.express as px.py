import geocoder # pip install geocoder
import pandas
import numpy
import plotly.express as px
import json


x = None
y = []
print(not(x is None))
print(not(y is None))

# file = pandas.read_excel('cinematreasures_1947_data.xlsx')


# addresses = []
# no_address = []
# no_city = []
# no_state = []
# for i in range(1,13827): 
#     if file['street_address'][i] == " ": no_address += [[i,file['name'][i]]]
#     if file['city'][i] == " ": no_city += [[i,file['name'][i]]]
#     if file['state'][i] == " ": no_state += [[i,file['name'][i]]]
#     else: addresses += [[file['name'][i] + ", " + str(i), file['street_address'][i] + ', ' + file['city'][i] + ', ' + file['state'][i]]]



# print(no_address)
# print(no_city)
# print(no_state)

# print("The cinemas without address are:")
# print(numpy.size(addresses,0))

# coordinates = []
# county = []
# lat = []
# lng = []
# i = 0
# n = numpy.size(addresses,0)
# for i in range(0,10):
#     g = geocoder.bing(addresses[i][1], key='AkJEePEi3Se7CEInH-99-V6M5ZpmxsBk-OK5HKBLzpxkylj2_mPJBNZ2j2t7fjYC')
#     results = g.json
#     print(results['raw']['address'])
#     lat += [results['lat']]
#     lng += [results['lng']]
#     if 'adminDistrict2' in list(results['raw']['address'].keys()): county += [[addresses[i][0],results['raw']['address']['adminDistrict2']]]
#     coordinates += [[addresses[i][0], results['lat'],results['lng']]]
#     print(str(i) + "/" + str(n) + " - name, number in csv: " + str(addresses[i][0]))


# df1 = pandas.DataFrame(coordinates, columns=['Movie theater','Lat','Lng'])
# print(df1)

# df1['gatto'] = ["topo","topo","topo","topo","topo","topo","topo","topo","topo","topo"]
# print(df1)

# df1 = df1[['gatto','Lat','Lng']]
# print(df1)

# dataset1 = open("coord_till_50.html","w")
# dataset1.write(pandas.DataFrame.to_html(df1))
# dataset1.close()