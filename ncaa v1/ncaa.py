import numpy as np
import csv

with open('ncaa_forecasts.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

teams = np.genfromtxt('ncaa_forecasts.csv', dtype=str, delimiter=',', usecols= (7, 8 ,9, 4, 5) ,skip_header = 1)
#forecast = np.genfromtxt('ncaa_forecasts.csv', delimiter=',')

#print(teams[0][3])

#print(len(teams))

east = []
for x in range(len(teams)):
      if teams[x][1] == 'East':
          east.append(teams[x][0])
#print(east)

west = []
for x in range(len(teams)):
      if teams[x][1] == 'West':
          west.append(teams[x][0])
#print(west)

south = []
for x in range(len(teams)):
      if teams[x][1] == 'South':
          south.append(teams[x][0])
#print(south)

midwest = []
for x in range(len(teams)):
      if teams[x][1] == 'Midwest':
          midwest.append(teams[x][0])
#print(midwest)

regions = [east, west, south, midwest]

scenarios = []
matchup = []
for i in east:
    for x in west:
        for y in south:
            for z in midwest:
                matchup.append(i)
                matchup.append(x)
                matchup.append(y)
                matchup.append(z)
                scenarios.append(matchup)
                matchup = []

print(len(scenarios))
print()

scenario_scores = []
matchup_scores = []
for i in scenarios:
    for x in i:
        for y in range(len(teams)):
            if x == teams[y][0]:
                matchup_scores.append(float(teams[y][2]) * 8)
    scenario_scores.append( matchup_scores[0] + matchup_scores[1] + matchup_scores[2] + matchup_scores[3] )
    matchup_scores = []

# scenario_adj_score = []
# matchup_adj_score = []
# for i in scenario_scores

scenario_prob = []
matchup_prob = []
for i in scenarios:
    for x in i:
        for y in range(len(teams)):
            if x == teams[y][0]:
                matchup_prob.append(teams[y][3])
    scenario_prob.append( float(matchup_prob[0]) * float(matchup_prob[1]) * float(matchup_prob[2]) * float(matchup_prob[3]))
    matchup_prob = []
    
# print(scenario_prob[0])
# print(scenarios[0])
# print(scenario_scores[0])
# 
# print(scenario_prob[30])
# print(scenarios[30])
# print(scenario_scores[30])

adj_scenario_score = []
for i in range(len(scenario_scores)):
    adj_scenario_score.append( scenario_scores[i] * scenario_prob[i])

#print(adj_scenario_score[0])
                
for x in range(len(scenarios)):
    scenarios[x].append(adj_scenario_score[x])
# print()
# print(scenarios[0])
# print(scenarios[1])
# print()

def myFunc(e):
    return e[4]

scenarios.sort(reverse=True, key=myFunc)

# for i in range (10):
#     print(scenarios[i])
    
# with open('predictions.csv', 'w') as f:
#       
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
#       
#     write.writerows(scenarios)
    
scenarios2 = []

for x in range(len(scenarios)):
    y = []
    y.append(scenarios[x][0])
    y.append(scenarios[x][1])
    y.append(scenarios[x][2])
    y.append(scenarios[x][3])
    y.append(scenarios[x][4])
    y.append(scenarios[x][0])
    y.append(scenarios[x][2])
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val1 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val2 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val3 = float(teams[i][4])
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val4 = float(teams[i][4])
    y.append((val1+val2)*val3*val4)
    y.append(scenarios[x][4]+(val1+val2)*val3*val4)
    scenarios2.append(y)
    y = []
    y.append(scenarios[x][0])
    y.append(scenarios[x][1])
    y.append(scenarios[x][2])
    y.append(scenarios[x][3])
    y.append(scenarios[x][4])
    y.append(scenarios[x][1])
    y.append(scenarios[x][2])
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val1 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val2 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val3 = float(teams[i][4])
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val4 = float(teams[i][4])
    y.append((val1+val2)*val3*val4)
    y.append(scenarios[x][4]+(val1+val2)*val3*val4)
    scenarios2.append(y)
    y = []
    y.append(scenarios[x][0])
    y.append(scenarios[x][1])
    y.append(scenarios[x][2])
    y.append(scenarios[x][3])
    y.append(scenarios[x][4])
    y.append(scenarios[x][0])
    y.append(scenarios[x][3])
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val1 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val2 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val3 = float(teams[i][4])
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val4 = float(teams[i][4])
    y.append((val1+val2)*val3*val4)
    y.append(scenarios[x][4]+(val1+val2)*val3*val4)
    scenarios2.append(y)
    y = []
    y.append(scenarios[x][0])
    y.append(scenarios[x][1])
    y.append(scenarios[x][2])
    y.append(scenarios[x][3])
    y.append(scenarios[x][4])
    y.append(scenarios[x][1])
    y.append(scenarios[x][3])
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val1 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val2 = float(teams[i][2])*16
    for i in range(len(teams)):
        if y[5] == teams[i][0]:
            val3 = float(teams[i][4])
    for i in range(len(teams)):
        if y[6] == teams[i][0]:
            val4 = float(teams[i][4])
    y.append((val1+val2)*val3*val4)
    y.append(scenarios[x][4]+(val1+val2)*val3*val4)
    scenarios2.append(y)

def myFunc2(e):
    return e[8]

scenarios2.sort(reverse=True, key=myFunc2)

print()
for i in range (20):
    print(scenarios2[i])
print()

# scenario_scores = []
# matchup_scores = []
# for i in range(len(scenarios2)):
#     for y in range(len(teams)): 
#         if scenarios2[i][1][] == teams[y][0]:
#             scenario_scores.append(float(teams[y][2]) * 16)

with open('predictions_ff_final.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerows(scenarios2)
    



