#Name: Maxim Chopivskyy
#ID number: 118364841

#Question 3

#(a)
f = open('voting.txt', 'r')

f.readline()

voting = []

for line in f:

    l = line.split()
    constituency = [int(i) for i in l]

    voting.append(constituency)

#(b)
total_votes = 0
for con in voting:
    for votes in con[1:]:
        total_votes += votes

print('Total Votes Cast:', total_votes)


#(c)
for index, con in enumerate(voting):
    con_votes = 0
    for votes in con[1:]:
        con_votes+=votes
    print('The votes for constituency %i are  %i' % (index+1, con_votes))

#(d)
td_votes_list = []
for td in range(1,len(voting[0])):
    td_votes = 0
    for con in voting:
        td_votes+=con[td]
    print('The votes for candidate TD %s are  %i' % (chr(64+td), td_votes))
    td_votes_list.append(td_votes)


#(e)
percent_list = []
for index, td_votes in enumerate(td_votes_list):
    percentage = td_votes/total_votes * 100
    percent_list.append(percentage)
    print('The votes for TD {} as a percentge of the overall are {:.6f} percent'.format(chr(65+index), percentage))


#(f)
tie=True

for p in range(len(percent_list)):
    if percent_list[p] >= 50:
        print('Candidate TD %s won' % (chr(65+p)))
        tie = False

td_dictionary = {}
for index, td_percent in enumerate(percent_list):
    candidate = 'TD ' + chr(65+index)
    td_dictionary[candidate] = td_percent


sorted_percent = sorted(percent_list)
for td, value in td_dictionary:
    if value == sorted_percent[-1]:
        first = td

print(first)

