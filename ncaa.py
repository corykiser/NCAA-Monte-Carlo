#import
import csv
import numpy as np

#import csv
with open('fivethirtyeight_ncaa_forecasts.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
a = np.array(data)[2:]

#narrow to mens pretourn forecast from csv
mens = []
for line in a:
    if line[0] == 'mens':
        if line[1] == '2022-03-16':
            if line[3] == '1.0':
                mens.append(line)

#convert to numpy arrays of proper types
#everything is a string until conversion
mens = np.array(mens)
team_rating = mens[:,14].astype(np.float_)
team_id = mens[:,12].astype(np.int_)
team_name = mens[:,13]
team_region = mens[:,15]
#team_seed needs cleanup
team_seed = mens[:,16]
for i in range(len(team_seed)):
        if team_seed[i][-1] == 'a':
            team_seed[i] = team_seed[i][:-1]
        if team_seed[i][-1] == 'b':
            team_seed[i] = team_seed[i][:-1]
team_seed = team_seed.astype(np.int_)

def win_prob(rating1, rating2):
    diff = rating1 - rating2
    prob = 1 / ( 1 + 10 ** ( -1 * diff * 30.464 / 400))
    return prob
                 



print(win_prob(81.2,81.8))