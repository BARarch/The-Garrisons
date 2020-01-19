#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 200118

def alternatingSums(a):
    teamA = 0
    teamB = 0
    for i, weight in enumerate(a):
        if i % 2 == 0:
            teamA += weight
        else:
            teamB += weight
            
    return [teamA, teamB]
