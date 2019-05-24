#This is an experimental project to find the central personality of a group of people
#This is based on the Page Rank Algorithm
#I implemented something similar during my internship as well

import csv

csv.register_dialect('myDialect', delimiter='\t')

init_scores = {}
edge_weights = {}
with open('friends.csv', 'r', encoding='ISO-8859-1') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            continue
        sum = 0
        init_scores[row[0]] = 100
        edge_weights[row[0]] = []
        for i in range(1, len(row)):
            row[i] = int(row[i])
            sum += row[i]
        row.insert(len(row), sum)
        #print(row)
        # normalize scores on the scale of 1
        for i in range(1, len(row)):
            row[i] /= sum
            edge_weights[row[0]].insert(len(edge_weights[row[0]]), row[i])
        print(row)
    print(init_scores)
    print(edge_weights)
csvFile.close()
