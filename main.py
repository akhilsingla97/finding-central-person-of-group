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
    order_of_people = []
    for row in reader:
        if firstLine:
            firstLine = False
            for i in range(1, len(row)):
                order_of_people.insert(len(order_of_people),row[i])
            continue
        sum = 0
        init_scores[row[0]] = 100
        edge_weights[row[0]] = {}
        for i in range(1, len(row)):
            row[i] = int(row[i])
            sum += row[i]
        row.insert(len(row), sum)
        #print(row)
        # normalize scores on the scale of 1
        for i in range(1, len(row)-1):
            row[i] /= sum
            # edge_weights[row[0]].insert(len(edge_weights[row[0]]), row[i])
            edge_weights[row[0]][order_of_people[i-1]] = row[i]
        print(row)
    print(init_scores)
    print(edge_weights)

csvFile.close()

final_scores = {}

for i in range(100):
    for person in init_scores:
        final_scores[person] = 0.15 * init_scores[person]
        other_contri = 0.0
        for weight in edge_weights:
            # print(edge_weights[weight][person])
            # print(init_scores[person])
            other_contri += edge_weights[weight][person] * init_scores[weight]
        final_scores[person] += 0.85 * other_contri
    for i in init_scores:
        init_scores[i] = final_scores[i]
    print(final_scores)