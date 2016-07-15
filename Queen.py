# George Juarez

import collections, operator, random

# Stats will be declared as floats at the moment (5 options):
# (A) Amazing = 0.8
# (B) Great = 0.6
# (C) Average = 0.5
# (D) Bad = 0.4
# (F) Awful = 0.3

class Queen:

    def __init__(self, name, sewStat, danceStat, singStat, actStat, humorStat, lipsyncCt = 0):
        self.__name = name
        self.__sewStat = sewStat
        self.__danceStat = danceStat
        self.__singStat = singStat
        self.__actStat = actStat
        self.__humorStat = humorStat

    def get_name(self):
        return self.__name
    def get_sewStat(self):
        return self.__sewStat
    def get_danceStat(self):
        return self.__danceStat
    def get_singStat(self):
        return self.__singStat
    def get_actStat(self):
        return self.__actStat
    def get_humorStat(self):
        return self.__humorStat
    def get_lipsyncCt(self):
        return self.__lipsyncCt

    def set_name(self,name):
        self.__name = name
    def set_sewStat(sewStat):
        self.__sewStat = sewStat
    def set_danceStat(danceStat):
        self.__danceStat = danceStat
    def set_singStat(singStat):
        self.__singStat = singStat
    def set_actStat(actStat):
        self.__actStat = actStat
    def set_humorStat(humorStat):
        self.__humorStat = humorStat
    def set_lipsyncCt(lipsyncCt):
        print("Lipsync count is read-only. Sorry!")

    name = property(get_name, set_name)
    sewStat = property (get_sewStat, set_sewStat)
    danceStat = property (get_danceStat, set_danceStat)
    singStat = property (get_singStat, set_singStat)
    actStat = property (get_actStat, set_actStat)
    humorStat = property (get_humorStat, set_humorStat)
    lipsyncCt = property (get_lipsyncCt, set_lipsyncCt)

s4_key_val_pairs = [("RuPocalyse Now!" , "sew"),
                    ("WTF: Wrestling Trashiest Fighters" , "humor"),
                    ("Glamazons vs. Champions" , "act"),
                    ("Queens Behind Bars", "act"),
                    ("Snatch Game", "humor"),
                    ("Float Your Boat", "sew"),
                    ("Dragazines", "act"),
                    ("Frenemies", "sing"),
                    ("Frock the Vote!", "humor"),
                    ("DILFs: Dads I'd Like To Frock", "sew"),
                    ("The Fabulous Bitch Ball", "sew"),
                    ("The Final Three", "none"),
                    ("Reunited", "none")]

s4_ordered_dict = collections.OrderedDict(s4_key_val_pairs)

s4_preset_contest = ["Alisa Summers", "Chad Michaels", "DiDa Ritz", "Jiggly Caliente", \
                     "LaShauwn Beyond", "Latrice Royale", "Madame LaQueer", "Milan", \
                     "Phi Phi O'Hara", "The Princess", "Sharon Needles", "Willam" ]

# Remember: Queen = Name, Sew, Dance, Sing, Act, Humor
s4_preset_contest_obj = [ Queen("Alisa Summers", 'F', 'D', 'C', 'C', 'C'), \
                          Queen("Chad Michaels", 'B', 'B', 'B', 'B', 'B'), \
                          Queen("DiDa Ritz", 'C', 'A', 'C', 'B', 'C'), \
                          Queen("Jiggly Caliente", 'F', 'A', 'C', 'C', 'B'), \
                          Queen("Lashauwn Beyond", 'A', 'D', 'C', 'B', 'C'), \
                          Queen("Latrice Royale", 'B', 'A', 'A', 'B', 'A'), \
                          Queen("Madame LaQueer", 'C', 'D', 'C', 'D', 'C'),
                          Queen("Milan", 'C', 'A', 'C', 'C', 'C'), \
                          Queen("Phi Phi O'Hara", 'B', 'A', 'B', 'C', 'B'), \
                          Queen("The Princess", 'B', 'C', 'C', 'D', 'C'), \
                          Queen("Sharon Needles", 'A', 'B', 'B', 'B', 'B'), \
                          Queen("Willam", 'B', 'B', 'A', 'A', 'A') ]

def main():
    '''
    # commented out for now

    for i in range(0,len(s4_preset_contest)) :
        print(s4_preset_contest[i])
    print(s4_preset_contest_obj[1].get_name())
    '''

    keep_going = 'y'

    print("Hello, and welcome to the Rupaul's Drag Race simulator!", \
          "\nFor the moment, we will just be using a preset season: Season 4. \nHere are the following contestants" \
          " from Season 4 of Rupaul's Drag Race.")
    cList = mainChallenge("sew")
    for key in cList:
        print(key, cList[key])
    print("\n\n")
    # sorted_cList will be a list of tuples sorted by the second element in each tuple
    sorted_cList = sorted(cList.items(), key = operator.itemgetter(1))
    for i in range(0,len(sorted_cList)):
        for j in range(0, len(sorted_cList[i])):
            print(sorted_cList[i][j])
    '''
    printRemaining()
    miniChallenge()
    mainChallenge("sew")
    '''

    '''
    while(keep_going.lower() == 'y'):
        print(0)
        keep_going = input("Enter y to exit: ")
    '''

def printRemaining():

    for i in range(0, len(s4_preset_contest_obj)):
        print(s4_preset_contest_obj[i].name)

def countRemaining():
    return len(s4_preset_contest_obj)

def miniChallenge():
    seed = random.randint(0, countRemaining())
    print("The winner of the mini-challenge is: ", s4_preset_contest_obj[seed].name, "!", sep = "")

def mainChallenge(challengeType):
    # So I guess the plan is to figure out a way to rank the Queens based on their performances
    # Each week, there's a certain number of Queens who are safe, and those who are on the top-bottom

    # The first thing we should do is calculate a general ranking based off the type of challenge presented this week
    queenPerformanceList = {}
    for i in range(0, countRemaining()):
        currentQueen = s4_preset_contest_obj[i]
        queenPerformanceList[currentQueen.name] = getQueenPerformance(currentQueen, challengeType)
        # Now that we have all the queen's performances for the main challenge, we should add additional points for the runway
        runwayScore = stat_to_float(currentQueen.sewStat)
        queenPerformanceList[currentQueen.name] += runwayScore
        
    return queenPerformanceList

def getQueenPerformance(currentQueen, challengeType):
    specifiedStat = ''
    if(challengeType == "sew"):
        specifiedStat = currentQueen.sewStat
    elif(challengeType == "dance"):
        specifiedStat = currentQueen.danceStat
    elif(challengeType == "sing"):
        specifiedStat = currentQueen.singStat
    elif(challengeType == "act"):
        specifiedStat == currentQueen.actStat
    elif(specifiedStat == "humor"):
        specifiedStat == currentQueen.humorStat
    randPerformance = random.uniform(stat_to_float(specifiedStat), stat_to_float(specifiedStat) + 1)
    return randPerformance

def stat_to_float(specifiedStat):
    return {
            'A' : 0.8,
            'B' : 0.6,
            'C' : 0.5,
            'D' : 0.4,
            'F' : 0.3,
        }.get(specifiedStat,0.0)
    
#call main
main()
