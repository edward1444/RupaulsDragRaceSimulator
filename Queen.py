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
        self.__lipsyncCt = lipsyncCt

    name = property(get_name, set_name)
    sewStat = property (get_sewStat, set_sewStat)
    danceStat = property (get_danceStat, set_danceStat)
    singStat = property (get_singStat, set_singStat)
    actStat = property (get_actStat, set_actStat)
    humorStat = property (get_humorStat, set_humorStat)
    lipsyncCt = property (get_lipsyncCt, set_lipsyncCt)

#--------------------End of Queen class (yay) -----------------------------

# fuck this shit, I gotta do this I guess
class Challenge:
    def __init__(self,name,challengeType):
        self.__name = name
        self.__challengeType = challengeType

    def get_name(self):
        return self.__name
    def get_challenge_type(self):
        return self.__challengeType

    def set_name(self, name):
        self.__name = name
    def set_challenge_type(self, challengeType):
        self.__challengeType = challengeType

    name = property(get_name, set_name)
    chalengeType = property(get_challenge_type, set_challenge_type)

#------------------ End of Challenge class (yay^2) -------------------------

# Remember: Challenge = Name, ChallengeType

s4_challenges = [ Challenge("RuPocalypse Now!","sew"), \
                 Challenge("WTF: Wrestling Trashiest Fighters" , "humor"), \
                 Challenge("Glamazons vs. Champions", "act"), \
                 Challenge("Queens Behind Bars", "act"), \
                 Challenge("Snatch Game", "humor"), \
                 Challenge("Float Your Boat", "sew"), \
                 Challenge("Dragazines", "act"), \
                 Challenge("Frenemies", "sing"), \
                 Challenge("Frock the Vote!", "humor"), \
                 Challenge("DILFs: Dads I'd Like To Frock", "sew"), \
                 Challenge("The Fabulous Bitch Ball", "sew"), \
                 Challenge("The Final Three", "none"), \
                 Challenge("Reunited!", "none") ]

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

    keep_going = 'y'

    print("Hello, and welcome to the Rupaul's Drag Race simulator!", \
          "\nFor the moment, we will just be using a preset season: Season 4. \nHere are the following contestants" \
          " from Season 4 of Rupaul's Drag Race.")
    '''
    
    cList = mainChallenge(s4_preset_contest_obj,"humor")
    # sorted_cList will be a list of tuples sorted by the second element in each tuple
    sorted_cList = sorted(cList.items(), key = operator.itemgetter(1))
    processTopBottomSafe(sorted_cList)
    

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

def printRemaining(contest_obj):
    for i in range(0, len(contest_obj)):
        print(contest_obj.name)

def countRemaining(contest_obj):
    return len(contest_obj)

def miniChallenge(contest_obj):
    seed = random.randint(0, countRemaining(contest_obj))
    print("The winner of the mini-challenge is: ", contest_obj[seed].name, "!", sep = "")

def mainChallenge(contest_obj,challengeType):
    # So I guess the plan is to figure out a way to rank the Queens based on their performances
    # Each week, there's a certain number of Queens who are safe, and those who are on the top-bottom

    # The first thing we should do is calculate a general ranking based off the type of challenge presented this week
    queenPerformanceList = {}
    for i in range(0, countRemaining(contest_obj)):
        currentQueen = contest_obj[i]
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

def processTopBottomSafe(cList):
    
    # REMINDER: topQueens, safeQueens, and bottomQueens are DESCENDING, so that means topQueens[0] is the winner of the challenge
    # bottomQueens[0] is "LOW" and bottomQueens[1] and bottomQueens[2] are the "BTM2"
    # safeQueens order doesn't really matter tbh
    
    topQueens = []
    safeQueens = []
    bottomQueens = []
    
    if( len(cList) >= 8 ):
        for i in range(2,-1,-1):
            bottomQueens.append(cList[i][0])
            del cList[i]
        for i in range(len(cList) - 1, len(cList) - 4, -1):
            topQueens.append(cList[i][0])
            del cList[i]
        for i in range(len(cList) - 1, -1, -1):
            safeQueens.append(cList[i][0])

        for i in range(0, len(topQueens)):
            print(topQueens[i])                      
                            
        print("\n\n")
        
        for i in range(0, len(safeQueens)):
             print(safeQueens[i]) 
    
        print("\n\n")
             
        for i in range(0, len(bottomQueens)):
            print(bottomQueens[i])
            
#call main
main()
