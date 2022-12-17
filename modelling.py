from visualisation import GraphVisualization

def score_in_pair(dec_1, dec_2):
        if dec_1 == "G" and dec_2 == "G":
            return 5
        if dec_1 == "G" and dec_2 == "B":
            return -10
        if dec_1 == "B" and dec_2 == "G":
            return 10
        if dec_1 == "B" and dec_2 == "B":
            return -5

#General decision function
def decision_function(rounds = [], friends = []):
    return "G" # returns "G" or "B"

def always_good(index, rounds =[], friends=[]):
    return "G"

def always_bad(index, rounds=[], friends=[]):
    return "B"

def strategic_thinker(index, rounds=[], friends=[]):
    if rounds == []: return "G"

    score_good = 0
    for i in friends[index]:
        score_good += score_in_pair("G", rounds[-1][i])
    score_bad = 0
    for i in friends[index]:
        score_bad += score_in_pair("B", "B")
    
    if score_good >= score_bad: 
        return "G"
    return "B"

n_players = 3    
players_list = []
#populate with behaviours
players_friends = {}
for i in range(n_players):
    players_friends[i] = []

class Game:
    def __init__(self, behaviours: 'list of Agents', friends: 'list of pairs'):
        self.players = behaviours
        self.n = len(behaviours)
        self.scores = [0]*self.n
        self.round_scores = []

        self.friends = {}
        for i in range(self.n):
            self.friends[i] = []

        for i in friends:
            self.add_friends(i[0], i[1])
        self.rounds = []


    def add_friends(self, friend_1, friend_2):
        self.friends[friend_1].append(friend_2)
        self.friends[friend_2].append(friend_1)

    def play_round(self):
        round_responses = []
        round_scores = []
        for i in range(self.n):
            round_responses.append(self.players[i](i, rounds = self.rounds, friends = self.friends))

        for i in range(self.n):
            round_scores.append(0)
            for j in self.friends[i]:
                round_scores[i] += self.score_in_pair(round_responses[i], round_responses[j])
                self.scores[i] += self.score_in_pair(round_responses[i], round_responses[j])
        self.rounds.append(round_responses)
        self.round_scores.append(round_scores)

        
    def score_in_pair(self, dec_1, dec_2):
        if dec_1 == "G" and dec_2 == "G":
            return 5
        if dec_1 == "G" and dec_2 == "B":
            return -10
        if dec_1 == "B" and dec_2 == "G":
            return 10
        if dec_1 == "B" and dec_2 == "B":
            return -5

    def visualize(self):
        graph = GraphVisualization()
        for i in range(self.n):
            for j in self.friends[i]:
                if j > i: graph.addEdge(f'{i} ({self.scores[i]})', f'{j} ({self.scores[j]})')
        graph.visualize()


game1 = Game([always_bad, always_bad, always_bad, always_bad], [[0,1], [1,2], [1,3], [2,3]])
for i in range(10):
    game1.play_round()
game1.visualize()
