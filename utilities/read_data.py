import csv

def getCSVData(fileName):
#create an empty list to store data
    rows=[]
#open the CSV file
    dataFile = open(fileName,'r')
#create a reader from CSV file
    reader = csv.reader(dataFile)
#skip the header
    next(reader)
#add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows
