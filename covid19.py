# Covid-19 

import csv

path = "WHO COVID-19 global table data July 14th 2021 at 6.32.17 AM.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)

greatest = 0
for row in reader:
    if int(row[2]) > greatest:
        greatest = int(row[2])
        country = row[0]
    
print(country, greatest)




