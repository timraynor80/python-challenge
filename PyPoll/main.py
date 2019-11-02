import os
import csv

ElectionData = 'election_data.csv'
VoterID  = []
Candidate = []
VoteFor = []
output = open("output.txt", "w")

with open(ElectionData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    print("Election Results", file=output)
    print("------------------------------", file=output)
    print("Election Results")
    print("------------------------------")
   
    for row in csvreader:
        VoterID.append(row[0])
        TotalVotes = len(VoterID)
        VoteFor.append(row[2])

        if row[2] not in Candidate:
            Candidate.append(row[2])
  
    print("Total Votes: " + str(TotalVotes), file=output)
    print("------------------------------", file=output)
    print("Total Votes: " + str(TotalVotes))
    print("------------------------------")

    for CandidateName in Candidate:
        VoteCount = VoteFor.count(str(CandidateName))
        VotePercentage = VoteCount / TotalVotes
        VotePercentage = '{0:.3f}%'.format(VotePercentage*100)
        print(f'{CandidateName}: {VotePercentage} ({VoteCount})', file=output)
        print(f'{CandidateName}: {VotePercentage} ({VoteCount})')
        curr_frequency = VoteFor.count(CandidateName)
        
    print("------------------------------", file=output)
    print("------------------------------")
    def Winner(VoteFor):
        return max(set(VoteFor), key = VoteFor.count)
    print(f'Winner: {Winner(VoteFor)}', file=output)
    print("------------------------------", file=output)
    print(f'Winner: {Winner(VoteFor)}')
    print("------------------------------")