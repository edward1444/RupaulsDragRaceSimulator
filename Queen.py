# George Juarez

import collections, operator, random
from random import shuffle

# Stats will be declared as floats at the moment (5 options):
# (A) Amazing = 0.8
# (B) Great = 0.6
# (C) Average = 0.5
# (D) Bad = 0.4
# (F) Awful = 0.3

class Queen:
    def __init__(self, name, sewStat, danceStat, singStat, actStat, humorStat, minWinCt = 0, winCt = 0, lipsyncCt = 0):
        self.__name = name
        self.__sewStat = sewStat
        self.__danceStat = danceStat
        self.__singStat = singStat
        self.__actStat = actStat
        self.__humorStat = humorStat
        self.__minWinCt = minWinCt
        self.__winCt = winCt
        self.__lipsyncCt = lipsyncCt

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
    def get_minWinCt(self):
        return self.__minWinCt
    def get_winCt(self):
        return self.__winCt
    def get_lipsyncCt(self):
        return self.__lipsyncCt

    def set_name(self,name):
        self.__name = name
    def set_sewStat(self,sewStat):
        self.__sewStat = sewStat
    def set_danceStat(self, danceStat):
        self.__danceStat = danceStat
    def set_singStat(self, singStat):
        self.__singStat = singStat
    def set_actStat(self, actStat):
        self.__actStat = actStat
    def set_humorStat(self, humorStat):
        self.__humorStat = humorStat
    def set_minWinCt(self, minWinCt):
        self.__minWinCt = minWinCt
    def set_winCt(self, lipsyncCt):
        self.__lipsyncCt = lipsyncCt
    def set_lipsyncCt(self, lipsyncCt):
        self.__lipsyncCt = lipsyncCt

    name = property(get_name, set_name)
    sewStat = property (get_sewStat, set_sewStat)
    danceStat = property (get_danceStat, set_danceStat)
    singStat = property (get_singStat, set_singStat)
    actStat = property (get_actStat, set_actStat)
    humorStat = property (get_humorStat, set_humorStat)
    minWinCt = property (get_minWinCt, set_minWinCt)
    winCt = property (get_winCt, set_winCt)
    lipsyncCt = property (get_lipsyncCt, set_lipsyncCt)

#--------------------End of Queen class (yay) -----------------------------

# fuck this shit, I gotta do this I guess
class Challenge:
    def __init__(self,name,challengeType, isElim):
        self.__name = name
        self.__challengeType = challengeType
        self.__isElim = isElim

    def get_name(self):
        return self.__name
    def get_challenge_type(self):
        return self.__challengeType
    def get_isElim(self):
        return self.__isElim

    def set_name(self, name):
        self.__name = name
    def set_challenge_type(self, challengeType):
        self.__challengeType = challengeType
    def set_isElim(self, isElim):
        self.__isElim = isElim

    name = property(get_name, set_name)
    challengeType = property(get_challenge_type, set_challenge_type)
    isElim = property(get_isElim, set_isElim)

#------------------ End of Challenge class (yay^2) -------------------------

#------------------- In order to save myself the headache -------------------
#------------------- Here is a TeamChallenge class, (subclass) --------------

class TeamChallenge(Challenge):
    def __init__(self, name, challengeType, isElim, teamCount, countIndiv):
        super(TeamChallenge,self).__init__(name,challengeType, isElim)
        self.__teamCount = teamCount
        self.__countIndiv = countIndiv

    def get_teamCount(self):
        return self.__teamCount
    def get_countIndiv(self):
        return self.__countIndiv

    def set_teamCount(self,teamCount):
        self.__teamCount = teamCount
    def set_countIndiv(self,countIndiv):
        self.__countIndiv = countIndiv

    teamCount = property(get_teamCount, set_teamCount)
    countIndiv = property(get_countIndiv, set_countIndiv)

#------------------ End of TeamChallenge class (yay^3) -----------------------

# Remember: Challenge = Name, ChallengeType, isElim
# TeamChallenge = Name, ChallengeType, isElim, TeamCount, CoundIndividualsOnEachTeam

s4_challenges = [ Challenge("RuPocalypse Now!","sew", True), \
                 TeamChallenge("WTF: Wrestling Trashiest Fighters" , "humor", True, 3, [4]), \
                 TeamChallenge("Glamazons vs. Champions", "act", True, 2, [5,6]), \
                 TeamChallenge("Queens Behind Bars", "act", True, 2, [5,5]), \
                 Challenge("Snatch Game", "humor", True), \
                 Challenge("Float Your Boat", "sew", True), \
                 Challenge("Dragazines", "act", True), \
                 TeamChallenge("Frenemies", "sing", False, 3, [2,2,2]), \
                 Challenge("Frock the Vote!", "humor", True), \
                 Challenge("DILFs: Dads I'd Like To Frock", "sew", True), \
                 Challenge("The Fabulous Bitch Ball", "sew", True), \
                 Challenge("The Final Three", "none", False), \
                 Challenge("Reunited!", "none", False) ]

# Remember: Queen = Name, Sew, Dance, Sing, Act, Humor

s4_preset_contest_obj = [ Queen("Alisa Summers", 'F', 'D', 'C', 'C', 'C', 0, 0, 0), \
                          Queen("Chad Michaels", 'B', 'B', 'B', 'B', 'B', 0, 0, 0), \
                          Queen("DiDa Ritz", 'C', 'A', 'C', 'B', 'C', 0, 0, 0), \
                          Queen("Jiggly Caliente", 'F', 'A', 'C', 'C', 'B', 0, 0, 0), \
                          Queen("Lashauwn Beyond", 'A', 'D', 'C', 'B', 'C', 0, 0, 0), \
                          Queen("Latrice Royale", 'B', 'A', 'A', 'B', 'A', 0, 0, 0), \
                          Queen("Madame LaQueer", 'C', 'D', 'C', 'D', 'C', 0, 0, 0),
                          Queen("Milan", 'C', 'A', 'C', 'C', 'C', 0, 0, 0), \
                          Queen("Phi Phi O'Hara", 'B', 'A', 'B', 'C', 'B', 0, 0, 0), \
                          Queen("The Princess", 'B', 'C', 'C', 'D', 'C', 0, 0, 0), \
                          Queen("Sharon Needles", 'A', 'B', 'B', 'B', 'B', 0, 0, 0), \
                          Queen("Willam", 'B', 'B', 'A', 'A', 'A', 0, 0, 0) ]

def main():

    keep_going = 'y'
    s4_obj_COPY = s4_preset_contest_obj
    print("Hello, and welcome to the Rupaul's Drag Race simulator!", \
          "\nFor the moment, we will just be using a preset season: Season 4. \nHere are the following contestants" \
          " from Season 4 of Rupaul's Drag Race.")
    printRemaining(s4_obj_COPY)

    while(keep_going.lower() == 'y'):
        keep_going = sanitised_input("Would you like to continue? [y/n]:", str.lower, range_=('y','n'))
        if(keep_going == 'n'):
            print("Bye.")
            break
        else:
            print("This week's Challenge will be:", s4_challenges[0].name)
            s4_obj_COPY = miniChallenge(s4_obj_COPY)
            results = mainChallenge(s4_obj_COPY, s4_challenges[0])
            sortedResults = sorted(results.items(), key = operator.itemgetter(1))
            parsedResults = processTopBottomSafe(sortedResults, True)
            announceSafeQueens(parsedResults[1])
            announceWinner(parsedResults[0])
            announceBottomQueens(parsedResults[2])
            loser = lipsync(s4_obj_COPY,parsedResults[2])
            s4_obj_COPY = deleteQueen(loser, s4_obj_COPY)
            printRemaining(s4_obj_COPY)

    '''
    # testcList to test out the changing bounds once len(cList) < 8
    testcList = [("Jiggly Caliente", 0.444444), ("Madame LaQueer", 0.644444), ("Willam", 0.744444), \
    ("Phi Phi O'Hara",1.444444), ("DiDa Ritz", 2.444444), ("Chad Michaels", 3.444444), ("Sharon Needles", 4.44444)]
    parsed_cList = processTopBottomSafe(testcList, False)
    elimQueen = lipsync(s4_preset_contest_obj, parsed_cList[2])
    print(elimQueen, ",sashay away.", sep = "")
    print("\n\n\n")
    deleteQueen(elimQueen, s4_preset_contest_obj)
    printRemaining(s4_preset_contest_obj)
    '''
# Print remaining contestants' names
def printRemaining(contest_obj):
    for i in range(0, len(contest_obj)):
        print(contest_obj[i].name)

# Count the length of the contestant object list, returns int
def countRemaining(contest_obj):
    return len(contest_obj)

# Pick a random winner for the mini-challenge, the reason it is random
# is because in the show, the mini-challenge doesn't affect the Queen's overall weekly score
def miniChallenge(contest_obj):
    seed = random.randint(0, countRemaining(contest_obj))
    print("The winner of the mini-challenge is: ", contest_obj[seed].name, "!", sep = "")
    contest_obj[seed].minWinCt += 1
    return contest_obj

# I guess I took this from stackoverflow too...ugh
# But the only thing atm to be used, in terms of prompt is making sure the user
# just continues with the flow, y'know ?
def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join((", ".join(map(str,
                                                                     range_[:-1])),
                                                       str(range_[-1])))))
        else:
            return ui

# shoutout to @Borealid from stackoverflow who wrote this for me because i was too dumb
# to do it lmao, returns a list of list of different sizes, each of them have shuffled
# Queens' names
def sortIntoTeams(contest_obj, numTeams):
    # Create a randomly-ordered copy of the contestants' names
    random_contestants = [x.name for x in contest_obj]
    random.shuffle(random_contestants)
    result = []
    for teamsize in numTeams:
        # Take the first <teamsize> contestants from the list
        result.append(random_contestants[:teamsize])
        # Remove those contestants, since they now have a team
        random_contestants = random_contestants[teamsize:]
    return result

# MainChallenge(contestant object, challenge object)
# calculate general ranking based off the type of challenge presented this week
# returns a unordered dictionary with the Queen's name as the key and their score as the value
# TODO: figure out how to alter this so it takes TeamChallenges into account
def mainChallenge(contest_obj,current_challenge_obj):
    # So I guess the plan is to figure out a way to rank the Queens based on their performances
    # Each week, there's a certain number of Queens who are safe, and those who are on the top-bottom
    queenPerformanceList = {}
    for i in range(0, countRemaining(contest_obj)):
        currentQueen = contest_obj[i]
        queenPerformanceList[currentQueen.name] = getQueenPerformance(currentQueen, current_challenge_obj.challengeType)
        # Now that we have all the queen's performances for the main challenge, we should add additional points for the runway
        runwayScore = stat_to_float(currentQueen.sewStat)
        queenPerformanceList[currentQueen.name] += runwayScore
    return queenPerformanceList


def teamMainChallenge(queenperformanceList, teamChallengeObj):
    print(0)

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

def processTopBottomSafe(cList, containSafe):

    # REMINDER: topQueens, safeQueens, and bottomQueens are DESCENDING, so that means topQueens[0] is the winner of the challenge
    # bottomQueens[0] is "LOW" and bottomQueens[1] and bottomQueens[2] are the "BTM2"
    # safeQueens order doesn't really matter tbh

    topQueens = []
    safeQueens = []
    bottomQueens = []
    parseTopBtm = nittyGritty(len(cList))

    for i in range(parseTopBtm[1] - 1, -1, -1):
        bottomQueens.append(cList[i][0])
        del cList[i]
    for i in range(len(cList) - 1, len(cList) - (parseTopBtm[0] + 1), -1):
        topQueens.append(cList[i][0])
        del cList[i]
    if(containSafe):
        print("Will the following Queens please step forward. \n")
        for i in range(len(cList) - 1, -1, -1):
            safeQueens.append(cList[i][0])

    return [topQueens, safeQueens, bottomQueens]

# We have to make certain cases for bounds once len(cList) < 8
# Case 7: 4 top, 3 bottom
# Case 6: 3 top, 3 bottom
# Case 5: 2 top, 3 bottom
# Case 4: 2 top, 2 bottom
# Default: 3 top, 3 bottom, rest safe

def nittyGritty(size):
    return {
        4: [2,2],
        5: [2,3],
        6: [3,3],
        7: [4,3],
    }.get(size, [3,3])

def announceSafeQueens(safeQueens):
    for i in range(0, len(safeQueens) - 1):
        print(safeQueens[i], ", ", sep = "", end = "")
    print(safeQueens[len(safeQueens) - 1], ". You are all safe. You may leave the stage.", sep = "")

def announceWinner(topQueens):
    print(topQueens[1], ", great job. You are safe!\n", \
         topQueens[0], ", conDragulations you are the winner of this week's challenge!", sep = "")
    if(len(topQueens) > 2):
        print(topQueens[2], ", nice work. You are safe.", sep = "")

def announceBottomQueens(bottomQueens):
    print(bottomQueens[1], ", I'm sorry my dear but you are up for elimination.")
    if(len(bottomQueens) > 2):
        print(bottomQueens[0], "\n.\n.\n.\n.\n.\nYou\n.\n.\nare safe.")
    print(bottomQueens[2], ", I'm sorry my dear but you are up for elimination.")

# For the actual lipsync, the bottom 2 queens must lipsync for their lives to impress Ru
# as this is their last chance to save themselves from elimination
# The rules are: both the Queens' danceStat is used to generate a random number between
# whatever the stat_to_float generator makes, and +1 of that
# the winCt will help them, giving them an extra .3 for every win to their final score
# their lipsyncCt will harm them, giving them a minus .25 for every previous lipsync to their final score
# the highest of the scores will be safe, and the other is declared the eliminated Queen

# TODO: find a way to try and access the object again without having to do it through the lipsync function
# maybe write a seperate search function ?
# or rewrite how you pass parameters to the function

def lipsync(contest_obj, bottomQueens):
    bottomStats = []
    elimQueen = ""
    # TODO: Figure out how to make these 2 for loops merge into one, to find both names
    # of the bottom 2 queens
    # UPDATE: oh wait shit
    for i in range(0, len(contest_obj)):
        currentQueen = contest_obj[i]
        if(currentQueen.name == bottomQueens[len(bottomQueens) - 1] ):
            bottomStats.append([currentQueen.name, currentQueen.danceStat, currentQueen.winCt, currentQueen.lipsyncCt])
    for i in range(0, len(contest_obj)):
        currentQueen = contest_obj[i]
        if(currentQueen.name == bottomQueens[len(bottomQueens) - 2] ):
            bottomStats.append([currentQueen.name, currentQueen.danceStat, currentQueen.winCt, currentQueen.lipsyncCt])

    for i in range(0, len(bottomStats)):
        for j in range(0, len(bottomStats[i])):
            print(bottomStats[i][j])

    baseOut = { bottomStats[0][0] : random.uniform(stat_to_float(bottomStats[0][1]), stat_to_float(bottomStats[0][1]) + 1) ,
                bottomStats[1][0] : random.uniform(stat_to_float(bottomStats[1][1]), stat_to_float(bottomStats[1][1]) + 1)
    }

    print("\n\n\n")

    for key in baseOut:
        print(key, baseOut[key])

    # an attempt to implement the said pluses and minuses lel

    baseOut[bottomStats[0][0]] = baseOut[bottomStats[0][0]] + (.25 * bottomStats[0][2]) - (.3 * bottomStats[0][3])
    baseOut[bottomStats[1][0]] = baseOut[bottomStats[1][0]] + (.25 * bottomStats[1][2]) - (.3 * bottomStats[1][3])

    print("\n\n\n")

    for key in baseOut:
        print(key, baseOut[key])

    if(baseOut[bottomStats[0][0]] < baseOut[bottomStats[1][0]]):
        elimQueen = bottomStats[0][0]
    else:
        elimQueen = bottomStats[1][0]

    return elimQueen

def deleteQueen(name, contest_obj):
    for i in range(0, countRemaining(contest_obj)):
        currentQueen = contest_obj[i]
        if(name == contest_obj[i].name):
            del contest_obj[i]
            break
    return contest_obj

#call main
main()
