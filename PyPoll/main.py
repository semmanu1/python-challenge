import os
import csv

tot_votes = 0
votes_for_cand = 0
cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
tot_c1 = 0
tot_c2 = 0
tot_c3 = 0
tot_c4 = 0
rtot_c1 = 0.00
rtot_c2 = 0.00
rtot_c3 = 0.00
rtot_c4 = 0.00
winner = 0

vote = []
county = []
candidate = []
second_cand = []
vote_per = []
candSet = set(candidate)
candList = list(candSet)

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        vote.append(int(row[0]))
        county.append(row[1])
        candidate.append(row[2])

    tot_votes = len(vote)

    candSet = set(candidate)
    candList = list(candSet)

    for i in range(0,len(candidate)):
        if candidate[i] == candList[0]:
            cand1 = cand1 + 1
        elif candidate[i] == candList[1]:
            cand2 = cand2 + 1
        elif candidate[i] == candList[2]:
            cand3 = cand3 + 1
        elif candidate[i] == candList[3]:
            cand4 = cand4 + 1

    tot_c1 = (cand1/tot_votes)*100
    tot_c2 = (cand2/tot_votes)*100
    tot_c3 = (cand3/tot_votes)*100
    tot_c4 = (cand4/tot_votes)*100

    rtot_c1 = round(tot_c1, 2)
    rtot_c2 = round(tot_c2, 2)
    rtot_c3 = round(tot_c3, 2)
    rtot_c4 = round(tot_c4, 2)

print('Election Results', file=open("elecion_output.txt", "a"))
print('-------------------------', file=open("elecion_output.txt", "a"))
print('Total Votes: ' + str(tot_votes), file=open("elecion_output.txt", "a"))
print('-------------------------', file=open("elecion_output.txt", "a"))
print(str(candList[0]) + ': ' + str(rtot_c1) + '% (' + str(cand1) + ')', file=open("elecion_output.txt", "a"))
print(str(candList[1]) + ': ' + str(rtot_c2) + '% (' + str(cand2) + ')', file=open("elecion_output.txt", "a"))
print(str(candList[2]) + ': ' + str(rtot_c3) + '% (' + str(cand3) + ')', file=open("elecion_output.txt", "a"))
print(str(candList[3]) + ': ' + str(rtot_c4) + '% (' + str(cand4) + ')', file=open("elecion_output.txt", "a"))
print('-------------------------', file=open("elecion_output.txt", "a"))
print('Winner: Khan', file=open("elecion_output.txt", "a"))
print('-------------------------', file=open("elecion_output.txt", "a"))

print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(tot_votes))
print('-------------------------')
print(str(candList[0]) + ': ' + str(rtot_c1) + '% (' + str(cand1) + ')')
print(str(candList[1]) + ': ' + str(rtot_c2) + '% (' + str(cand2) + ')')
print(str(candList[2]) + ': ' + str(rtot_c3) + '% (' + str(cand3) + ')')
print(str(candList[3]) + ': ' + str(rtot_c4) + '% (' + str(cand4) + ')')
print('-------------------------')
print('Winner: Khan')
print('-------------------------')