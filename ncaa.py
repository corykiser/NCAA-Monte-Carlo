#import
import csv
import numpy as np
import random
import os.path
import urllib.request
from multiprocessing import Process

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

round1 = [ [1,16], [2,15] , [3,14], [4,13], [5,12], [6,11], [7,10], [8,9] ]
round2 = [ [1,16,8,9] , [5,12,4,13], [6,11,3,14], [7,10,2,15]]
round3 = [ [1,16,8,9,5,12,4,13], [6,11,3,14,7,10,2,15]]
round4 = [ [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]


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

region_names = ['East', 'West', 'South', 'Midwest']
regions = [[],[],[],[]]
for i in range(4):
    for index in np.where(team_region == region_names[i]):
        regions[i].append(team_id[index])



#create dictionaries for team name and team id for convenience
team_name_dict = {}
team_id_dict = {}
team_seed_dict = {}
team_region_dict = {}
for i in range(len(team_id)):
    team_name_dict[team_id[i]] = team_name[i]
    team_id_dict[team_name[i]] = team_id[i]
    team_seed_dict[team_id[i]] = team_seed[i]
    team_region_dict[team_id[i]] = team_region[i]
    

def win_prob(rating1, rating2):
    #takes power ranking elo scores and outputs win probability
    diff = rating1 - rating2
    prob = 1 / ( 1 + 10 ** ( -1 * diff * 30.464 / 400))
    return prob
                 
class Game:
    # class that will contain data needed to simulate one game
    # these objects will live in another object called a Bracket
    # that will be responsible for simulating a whole tournament
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
        #takes power ranking elo scores and outputs win probability
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
        # fill games1 based on seeds adding to 17
        for j in range(4):
            checklist = []
            for i in range(16):
                pair = 17 - team_seed_dict[regions[j][0][i]]
                for team in team_id:
                    if team_region_dict[team] == region_names[j]:
                        if team_seed_dict[team] == pair:
                            if team not in checklist:
                                if pair not in checklist:
                                    self.games1.append( Game(regions[j][0][i], team) )
                                    checklist.append(regions[j][0][i])
                                    checklist.append(pair)

    
    def Simulate(self):
        games1_winners = []
        for i in self.games1:
            i.Simulate()
            games1_winners.append(i.winner)
        for j in range(4):
            for x in round2:
                t = []
                for team in games1_winners:
                    if team_region_dict[team] == region_names[j]:
                        if team_seed_dict[team] in x:
                            t.append(team)
                self.games2.append( Game(t[0],t[1]))
        
        games2_winners = []
        for i in self.games2:
            i.Simulate()
            games2_winners.append(i.winner)
        for j in range(4):
            for x in round3:
                t = []
                for team in games2_winners:
                    if team_region_dict[team] == region_names[j]:
                        if team_seed_dict[team] in x:
                            t.append(team)
                self.games3.append( Game(t[0],t[1]))
        games3_winners = []
        for i in self.games3:
            i.Simulate()
            games3_winners.append(i.winner)
        for j in range(4):
            for x in round4:
                t = []
                for team in games3_winners:
                    if team_region_dict[team] == region_names[j]:
                        if team_seed_dict[team] in x:
                            t.append(team)
                self.games4.append( Game(t[0],t[1]))
        games4_winners = []
        for i in self.games4:
            i.Simulate()
            games4_winners.append(i.winner)
        
        self.games5.append( Game(games4_winners[0], games4_winners[1]))
        self.games5.append( Game(games4_winners[2], games4_winners[3]))
        games5_winners = []            
        for i in self.games5:
            i.Simulate()
            games5_winners.append(i.winner)
        self.games6.append(Game(games5_winners[0], games5_winners[1]))
        self.games6[0].Simulate()
        self.Score()
        self.Prob()
        self.adjusted_score = self.score * self.prob
                
        #code simulate a round and make games for next round
    
    def Score(self):
        score = 0
        for game in self.games1:
            score += 1 + team_seed_dict[game.winner]
        for game in self.games2:
            score += 2 + team_seed_dict[game.winner]
        for game in self.games3:
            score += 4 + team_seed_dict[game.winner]
        for game in self.games4:
            score += 8 * team_seed_dict[game.winner]
        for game in self.games5:
            score += 16 * team_seed_dict[game.winner]
        for game in self.games6:
            score += 32 * team_seed_dict[game.winner]
        self.score = score
    
    def Prob(self):
        #code to find product of all probabilities
        prob = 1
        for game in self.games1:
            prob *= game.team1prob
        for game in self.games2:
            prob *= game.team1prob
        for game in self.games3:
            prob *= game.team1prob
        for game in self.games4:
            prob *= game.team1prob
        for game in self.games5:
            prob *= game.team1prob
        for game in self.games6:
            prob *= game.team1prob
        self.prob = prob
    
    def Output(self):
        # return an array for storing in a list so
        #the objects can get deleted from memory
        return np.array( [self.games2, self.games3, self.games4, self.games5, self.games6, self.prob, self.score, self.adjusted_score] )
        
    def PrintBracket(self):
        for i in self.games1:
            print(team_name_dict[i.winner])
            #print(team_name_dict[i.team1], team_name_dict[i.team2])
        print()
        for i in self.games2:
            print(team_name_dict[i.winner])
            #print(team_name_dict[i.team1], team_name_dict[i.team2])
        print()
        for i in self.games3:
            print(team_name_dict[i.winner])
            #print(team_name_dict[i.team1], team_name_dict[i.team2])
        print()
        for i in self.games4:
            print(team_name_dict[i.winner])
            #print(team_name_dict[i.team1], team_name_dict[i.team2])
        print()
        for i in self.games5:
            print(team_name_dict[i.winner])
            #print(team_name_dict[i.team1], team_name_dict[i.team2])
        print()
        print(team_name_dict[self.games6[0].winner])
        print(self.score)
        print('-----')
        return




def myFunc(e):
  return e[1]

toplist = []
for i in range(100000):
    y = Bracket()
    y.Simulate()
    if len(toplist) > 10:
        max = 0;
        for x in toplist:
            if x[1] > max:
                max = x[1]
        if y.score > max:
            toplist.pop(-1)
            toplist.append([y,y.adjusted_score])
            
    else:
        toplist.append([y,y.adjusted_score])

toplist.sort(reverse=True, key=myFunc)
for i in range(9):
    toplist[i][0].PrintBracket()
# f = open("results.txt", "a")
# for i in toplist:
#     f.write()
# f.close()
