#import
import csv
import numpy as np
import random
import os.path
import urllib.request

## check if the forecast data exists and download if it doesn't
if os.path.exists('fivethirtyeight_ncaa_forecasts.csv') == False:
    url = "https://projects.fivethirtyeight.com/march-madness-api/2022/fivethirtyeight_ncaa_forecasts.csv"
    urllib.request.urlretrieve(url, 'fivethirtyeight_ncaa_forecasts.csv')

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

#create dictionaries for team name and team id
team_name_dict = {}
team_id_dict = {}
for i in range(len(team_id)):
    team_name_dict[team_id[i]] = team_name[i]
    team_id_dict[team_name[i]] = team_id[i]

def win_prob(rating1, rating2):
    diff = rating1 - rating2
    prob = 1 / ( 1 + 10 ** ( -1 * diff * 30.464 / 400))
    return prob
                 
class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.pos1 = np.where(team_id == team1)
        self.pos2 = np.where(team_id == team2)
        self.team1rating = team_rating[self.pos1]
        self.team2rating = team_rating[self.pos2]
        self.team1prob = win_prob(team_rating[self.pos1], team_rating[self.pos2])
        self.team2prob = 1.0 - self.team1prob
        self.winner = 0
    
    def win_prob(self, rating1, rating2):
        diff = rating1 - rating2
        prob = 1 / ( 1 + 10 ** ( -1 * diff * 30.464 / 400))
        return prob
    
    def Simulate(self):
        if random.random() < self.team1prob:
            self.winner = self.team1
        else:
            self.winner = self.team2
        

class Bracket:
    #simulate 74,325,939 brackets if possible
    def __init__(self):
        #remember to delete these from memory once you get the results
        self.games1 = [] #32 games 64 teams
        self.games2 = [] #16 games 32 teams
        self.games3 = [] #8 games 16 teams
        self.games4 = [] #4 games 8 teams
        self.games5 = [] #2 games 4 teams
        self.games6 = [] #1 game 2 teams
        self.prob = 0 #calculate probability of the whole situation happening
        self.score = 0 #calculate score
        self.adjusted_score = 0 #product of prob and score
        # code to create games based on 17
    
    def SimulateRound(self, roundnum):
        #code simulate a round and make games for next round
        return
    
    def Score(self):
        #code to calculate bracket score
        return
    
    def Prob(self):
        #code to find product of all probabilities
        return
    
    def Output(self):
        # return an array for storing in a list so
        #the objects can get deleted from memory
        return np.array( self.games2, self.games3, self.games4, self.games5, self.games6, self.prob, self.score, self.adjusted_score )
        
    def PrintBracket(self):
        #code to print winners with prob + score
        return


x = Game(team_id_dict['Kentucky'], team_id_dict["Saint Peter's"])
x.Simulate()
print(x.team1prob)
for i in range (100):
    x.Simulate()
    print(team_name_dict[x.winner])

