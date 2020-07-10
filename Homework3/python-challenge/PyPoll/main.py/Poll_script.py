import os
import csv

vote_count = []
total_votes = 0
candidate_ls = []

csvpath = os.path.join('..','Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_in = (row[2])
        if candidate_in in candidate_ls:
            candidate_index = candidate_ls.index(candidate_in)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidate_ls.append(candidate_in)
            vote_count.append(1)


pct = []
max_votes = vote_count[0]
max_index = 0

for x in range(len(candidate_ls)):

    vote_pct = round(vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if vote_count[x] > max_votes:
        max_votes = vote_count[x]
        max_index = x

election_winner = candidate_ls[max_index] 

print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidate_ls)):
    print(f'{candidate_ls[x]} : {pct[x]}% ({vote_count[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


Poll_file = os.path.join("..","analysis", "results.txt")
with open(Poll_file, "w") as out_file:
    out_file.write('======================================================\n')
    out_file.write('|                  Election Results                  |\n')
    out_file.write('======================================================\n')
    out_file.write(f'Total Votes: {total_votes}\n')
    out_file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidate_ls)):
        out_file.write(f'{candidate_ls[x]} : {pct[x]}% ({vote_count[x]})\n')
    out_file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    out_file.write(f'Election winner: {election_winner.upper()}\n')
    out_file.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    out_file.write("---END OF REPORT---")
