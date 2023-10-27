import pandas
import statistics
import numpy

file = pandas.read_html('counties.html')

counties = []
for k in range(0,13503):
    if file[0]['county'][k] not in counties: counties += [file[0]['county'][k]]


index = pandas.Series(file[0]['county'])
index = index.value_counts()
# print(index.value_counts())

county_numbers = index.tolist()

#Statistics

stat = [[statistics.mean(county_numbers),max(county_numbers),min(county_numbers),statistics.stdev(county_numbers)]]

county_stats = pandas.DataFrame(stat,columns=['Mean','Max','Min','Standard deviation'])

print("Statistics per county:")
print(county_stats)

counties_stat = open("Counties_stat.html","w")
counties_stat.write(pandas.DataFrame.to_html(county_stats))
counties_stat.close()

#Counties without cinemas

n_counties_total = 3224

n_counties_cinema = numpy.size(counties)

n_counties_no_cinema = n_counties_total - n_counties_cinema

print("Number of counties without movie theaters: " + str(n_counties_no_cinema))

#Counties with only 2 cinemas

counties_2_cinemas = int()
for k in range(0,1550):
    if index.iloc[k] == 2: counties_2_cinemas += 1

print("Number of counties with 2 movie theaters: " + str(counties_2_cinemas))

##Counties with only 4 cinemas


counties_4_cinemas = int()
for k in range(0,1550):
    if index.iloc[k] == 4: counties_4_cinemas += 1

print("Number of counties with 4 movie theaters: " + str(counties_4_cinemas))