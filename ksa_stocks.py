import csv
from datetime import datetime

path = "tasi_2.csv"
file = open(path, newline="")
reader = csv.reader(file)
header = next(reader)


path = "tasi_adjusted.csv"
file = open(path, "w")
writer = csv.writer(file)
writer.writerow(["Date", "Closing", "Openning", "High", "Low", "Volume"])
data = []
for row in reader:
    mydate = row[0][3:5]+"/"+row[0][:2]+"/"+row[0][6:11]
    date = datetime.strptime(mydate, '%m/%d/%Y')
    closing = float(row[1])
    openning = float(row[2])
    high = float(row[3])
    low = float(row[4])
    volume = float(row[5][0:-1])
    change = float(row[6][0:-1])
    data.append([date, closing, openning, high, low, volume])
    writer.writerow([date, closing, openning, high, low, volume, change])
    print(mydate, closing, openning, high, low, volume, change)



# Find the daily return of Tasi
for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_closing = todays_row[1]
    yesterdays_row = data[i+1]
    yesterdays_closing = yesterdays_row[1]

    daily_return = (todays_closing - yesterdays_closing) / yesterdays_closing
    print(todays_date, daily_return)
