import json
import csv
f = open("covid_cases.json")
myjson = json.load(f)


csv_file = open('records.csv','w')

csv_writer = csv.writer(csv_file)
count=0
for i in myjson['records']:
    if count == 0:
        columns = i.keys()
        csv_writer.writerow(columns)
        count+=1
    csv_writer.writerows(i["dateRep"])
    csv_writer.writerows(i["countriesAndTerritories"])
    csv_writer.writerows(i["cases"])
    csv_writer.writerows(i["deaths"])
csv_file.close()
    