import os
import csv

ElectionData = 'election_data.csv'
VoterID  = []
Candidate = []
VoteFor = []

#create and open output.txt file
output = open("output.txt", "w")

with open(ElectionData, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    print("Election Results", file=output)
    print("------------------------------", file=output)
    print("Election Results")
    print("------------------------------")
   
    for row in csvreader:
        #update VoterID to use later in TotalVotes
        VoterID.append(row[0])
        #Calculate TotalVotes by using len(list) on VoterID for a count of values in the VoterID list. 
        TotalVotes = len(VoterID)
        #update VoteFor with list.append(row[i]) to get a list of all the Votes cast.
        VoteFor.append(row[2])

        #loop through the row of votes cast and add unique values to Candidate list. 
        if row[2] not in Candidate:
            Candidate.append(row[2])
  
    print("Total Votes: " + str(TotalVotes), file=output)
    print("------------------------------", file=output)
    print("Total Votes: " + str(TotalVotes))
    print("------------------------------")

    #for each unique value in Candidate:
    for CandidateName in Candidate:
        #calculate how many votes each candidate received by using list.count(str(i))
        VoteCount = VoteFor.count(str(CandidateName))
        #calculate the percentage of TotalVotes each candidate received by dividing VoteCount by TotalVotes
        VotePercentage = VoteCount / TotalVotes
        #set VotePercentage to proper decimal format
        VotePercentage = '{0:.3f}%'.format(VotePercentage*100)
        print(f'{CandidateName}: {VotePercentage} ({VoteCount})', file=output)
        print(f'{CandidateName}: {VotePercentage} ({VoteCount})')
        
    print("------------------------------", file=output)
    print("------------------------------")

    #determine Winner by defining Winner(VoteFor)
    def Winner(VoteFor):
        #returning max(set(list)), key = list.count
        return max(set(VoteFor), key = VoteFor.count)
    print(f'Winner: {Winner(VoteFor)}', file=output)
    print("------------------------------", file=output)
    print(f'Winner: {Winner(VoteFor)}')
    print("------------------------------")