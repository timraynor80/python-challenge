import os
import csv

ElectionData = 'election_data.csv'
VoterID  = []
Candidate = []
VoteFor = []

with open(ElectionData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        # print(csv_header)

    print("Election Results")
    print("------------------------------")

    for row in csvreader:
        VoterID.append(row[0])
        TotalVotes = len(VoterID)
        VoteFor.append(row[2])

        if row[2] not in Candidate:
            Candidate.append(row[2])
  
    print("Total Votes: " + str(TotalVotes))
    print("------------------------------")

    for CandidateName in Candidate:
        # print(VoteFor.count(str(CandidateName)))
        print(f'{CandidateName}: ({VoteFor.count(str(CandidateName))})')
    print("------------------------------")
    print("Winner :")
    print("------------------------------")