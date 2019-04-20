#This is an experimental project to find the central personality of a group of people
#This is based on the Page Rank Algorithm
#I implemented something similar during my internship as well

import csv

csv.register_dialect('myDialect', delimiter='\t')

with open('friends.csv', 'r', encoding='ISO-8859-1') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            continue
        for i in range(len(row)):
            if i!=0:
                print(row[i], end="")
                row[i] = int(row[i])
        print(row)
csvFile.close()
