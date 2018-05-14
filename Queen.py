# George Juarez - Rupaul's Drag Race Simulator

import collections, operator, random
from random import shuffle

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
    def set_winCt(self, winCt):
        self.__winCt = winCt
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
    def __init__(self, name, challengeType, isElim, countIndiv):
        super(TeamChallenge,self).__init__(name,challengeType, isElim)
        self.__countIndiv = countIndiv

    def get_countIndiv(self):
        return self.__countIndiv

    def set_countIndiv(self,countIndiv):
        self.__countIndiv = countIndiv

    countIndiv = property(get_countIndiv, set_countIndiv)

#------------------ End of TeamChallenge class (yay^3) -----------------------

# Remember: Challenge = Name, ChallengeType, isElim
# TeamChallenge = Name, ChallengeType, isElim, CountIndividualsOnEachTeam

s4_challenges = [Challenge("RuPocalypse Now!","sew", True), \
                 TeamChallenge("WTF: Wrestling Trashiest Fighters" , "humor", True, [4,4,4]), \
                 TeamChallenge("Glamazons vs. Champions", "act", True, [5,6]), \
                 TeamChallenge("Queens Behind Bars", "act", True, [5,5]), \
                 Challenge("Snatch Game", "humor", True), \
                 Challenge("Float Your Boat", "sew", True), \
                 Challenge("Dragazines", "act", True), \
                 TeamChallenge("Frenemies", "sing", False, [2,2,2]), \
                 Challenge("Frock the Vote!", "humor", True), \
                 Challenge("DILFs: Dads I'd Like To Frock", "sew", True), \
                 Challenge("The Fabulous Bitch Ball", "sew", True), \
                 Challenge("The Final Three", "none", False), \
                 Challenge("Reunited!", "none", False) ]

s5_challenges = [Challenge("RuPaullywood or Bust", "sew", True), \
                 TeamChallenge("Lip Synch Extravangza Eleganza", "act", True, [4,5,4]), \
                 TeamChallenge("Draggle Rock", "act", True, [6,6]), \
                 TeamChallenge("Black Swan, Why It Gotta Be Black?", "dance", True, [6,5]), \
                 Challenge("Snatch Game", "humor", True), \
                 TeamChallenge("Can I Get An Amen?", "sing", True, [3,3,3]), \
                 Challenge("RuPaul Roast", "humor", True), \
                 Challenge("Scent of a Drag Queen", "act", True), \
                 TeamChallenge("Drama Queens", "act", True, [3,3]), \
                 Challenge("Super Troopers", "sew", True), \
                 Challenge("Sugar Ball", "sew", True), \
                 Challenge("The Final Three, Hunty", "none", False), \
                 Challenge("Reunited!", "none", False) 

s4_lipsyncs = ["Britney Spears - Toxic", "Donna Summer - Bad Girls", \
                "Natalie Cole - This Will Be (An Everlasting Love", "Pink - Trouble", \
                "Madonna - Vogue", "Lady Gaga - Born This Way", "Pam Tillis - Mi Vida Loca (My Crazy Life)",
                "Martha Wash & RuPaul - It's Raining Men (The Sequel)", \
                "Gladys Knight - I've Got to Use My Imagination", \
                "Aretha Franklin - You Make Me Feel Like a Natural Woman", \
                "Wynonna Judd - No One Else on Earth", "RuPaul - Glamazon"]

s5_lipsyncs = ["Miley Cyrus - Party in the U.S.A", "Rihanna - Only Girl in the World", \                "The Pussycat Dolls - When I Grow Up", "Britney Spears - Oops!...I Did it Again", \
                "Cher - Take Me Home", "The Pointer Sisters - I'm So Excited", \
                "Willow Smith - Whip My Hair", "Gwen Guthrie - Ain't Nothing Goin' on But the Rent" \
                "Paula Abdul - Cold Hearted", "Seduction - (It Takes) Two to Make it Right", \
                "Yma Sumac - Malambo No. 1", "RuPaul - The Beginning" ]

# Remember: Queen = Name, Sew, Dance, Sing, Act, Humor
s4_preset_contest_obj = [ Queen("Edward", 'F', 'D', 'C', 'C', 'C'), \
                          Queen("Eilish", 'B', 'B', 'B', 'B', 'B'), \
                          Queen("Becky", 'C', 'A', 'C', 'B', 'C'), \
                          Queen("Georgia", 'F', 'A', 'C', 'C', 'B'), \
                          Queen("Mary", 'B', 'A', 'C', 'D', 'B'), \
                          Queen("Liv", 'A', 'D', 'C', 'B', 'C'), \
                          Queen("Sammy", 'B', 'A', 'A', 'B', 'A'), \
                          Queen("Michael", 'C', 'D', 'C', 'D', 'C'),
                          Queen("Sean", 'C', 'A', 'C', 'C', 'C'), \
                          Queen("Stacey", 'B', 'A', 'B', 'C', 'B'), \
                          Queen("Claudia", 'B', 'C', 'C', 'D', 'C'), \
                          Queen("Klaudia", 'A', 'B', 'B', 'B', 'B'), \
                          Queen("Grace", 'B', 'B', 'A', 'A', 'A') ]

s5_preset_contest_obj = [ Queen("Alaska", 'A', 'B', 'B', 'B', 'A'), \
                          Queen("Alyssa Edwards", 'B', 'A', 'C', 'C', 'B'), \
                          Queen("Coco Montrese", 'B', 'A', 'C', 'C', 'B'), \
                          Queen("Detox", 'B', 'B', 'B', 'A', 'B'), \
                          Queen("Honey Mahogany", 'C', 'D', 'B', 'B', 'C'), \
                          Queen("Ivy Winters", 'B', 'C', 'B', 'B', 'B'), \
                          Queen("Jade Jolie", 'C', 'C', 'C', 'B', 'B'), \
                          Queen("Jinkx Monsoon", 'C', 'B', 'A', 'A', 'A'), \
                          Queen("Lineysha Sparx", 'A', 'B', 'C', 'C', 'C'),
                          Queen("Monica Beverly Hillz", 'C', 'B', 'C', 'D', 'C'), \
                          Queen("Penny Tration", 'D', 'C', 'C', 'C', 'B'), \
                          Queen("Roxxxy Andrews", 'A', 'B', 'B', 'B', 'C'), \
                          Queen("Serena ChaCha", 'D', 'B', 'C', 'D', 'B'), \
                          Queen("Vivienne Pinay", 'B', 'D', 'C', 'B', 'C') ]


def main():
    keep_going = 'y'
    testQueenObj = s5_preset_contest_obj
    testChallengeObj = s5_challenges
    testLipsyncs = s5_lipsyncs
    loserQueens = [] * len(testQueenObj)
    isSafeFlag = True
    counter = 0
    print("Hello, and welcome to the Rupaul's Drag Race simulator!", \
          "\nFor the moment, we will just be using a preset season: Season 5.\n")
    while(keep_going.lower() == 'y'):
        if(countRemaining(testQueenObj) < 8):
            isSafeFlag = False
        keep_going = sanitised_input("Would you like to continue? [y/n]: ", str.lower, range_=('y','n'))
        print("\nHere are the remaining contestants: ")
        printRemaining(testQueenObj)
        if(keep_going == 'n'):
            print("Alright, beat it Queen!")
            break
        else:
            print("This week's Challenge will be:", testChallengeObj[counter].name)
            if((counter == len(testChallengeObj) - 2) and testChallengeObj[counter].isElim == False):
                print("The Final 3 are set to compete in Rupaul's new music video!")
                musicVideoTimeNonElim(testChallengeObj[counter])
            elif(counter == len(testChallengeObj) - 1):
                lastChunk = grandFinaleTwoRU(testQueenObj, testChallengeObj[counter])
                for chunk in lastChunk:
                    loserQueens.append(chunk)
            else:
                keep_going = sanitised_input("Time to move forward to the Mini-Challenge! [y to continue]: ", \
                                            str.lower, range_ = ('y','Y'))
                testQueenObj = miniChallenge(testQueenObj)
                keep_going = sanitised_input("Time to move forward to the Main-Challenge! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                if(type(testChallengeObj[counter]) is TeamChallenge):
                    keep_going = sanitised_input("This week is a Team Challenge, so teams must be formed! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                    teamQueenList = sortIntoTeams(testQueenObj, testChallengeObj[counter].countIndiv)
                    print("These are the teams for the week:\n")
                    for i in range(0, len(teamQueenList)):
                        print("On Team ", i + 1, ":", sep = "")
                        currTeam = teamQueenList[i]
                        for currMem in range(0, len(currTeam)):
                            print(currTeam[currMem])
                        print("\n")
                    totalScores = teamMainChallenge(testQueenObj, testChallengeObj[counter], teamQueenList)
                    parsedResults = processTeamTopBottomSafe(teamQueenList, totalScores, isSafeFlag)
                else:
                    print("We are now calculating the Performance of each of the Queens!")
                    results = mainChallenge(testQueenObj, testChallengeObj[counter])
                    sortedResults = sorted(results.items(), key = operator.itemgetter(1))
                    parsedResults = processTopBottomSafe(sortedResults, isSafeFlag)
                    keep_going = sanitised_input("Now we must calculate the Runway Scores! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                keep_going = sanitised_input("Time for the moment of truth! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                if(isSafeFlag):
                    announceSafeQueens(parsedResults[1])
                keep_going = sanitised_input("Time to announce the Winner! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                s4_obj_COPY = announceWinner(testQueenObj,parsedResults[0])
                keep_going = sanitised_input("Time to announce the Bottom 2! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                announceBottomQueens(parsedResults[2])
                print("The Queens faced off to the lipsync of the week:", testLipsyncs[counter])
                keep_going = sanitised_input("The lipsync was intense, but the Queens showed no mercy! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
                # Remember: lipsync function returns a list, with the savedQueen as the first member and the loser
                # as the second member
                btmList = lipsync(testQueenObj,parsedResults[2])
                loserObj = getQueenObjFromName(testQueenObj, btmList[1])
                survObj = getQueenObjFromName(testQueenObj, btmList[0])
                survObj.lipsyncCt += 1
                loserObj.lipsyncCt += 1
                if(testChallengeObj[counter].isElim):
                    print(btmList[1], ",sashay away.", sep = "")
                    loserQueens.append(loserObj)
                    testQueenObj = deleteQueen(btmList[1], testQueenObj)
                else:
                    print(btmList[1], ", shantay you also stay! You will compete for one more week!")
                    keep_going = sanitised_input("How intense! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
            counter += 1
            if(counter == len(testChallengeObj)):
               runFinalStats(loserQueens)
               break

# Print remaining contestants' names
def printRemaining(contest_obj):
    for i in range(0, len(contest_obj)):
        print(contest_obj[i].name)

# Count the length of the contestant object list, returns int
def countRemaining(contest_obj):
    return len(contest_obj)

# returns the Queen object by identifying it by their name
def getQueenObjFromName(contest_obj, name):
    for i in range(0, countRemaining(contest_obj)):
        if(contest_obj[i].name == name):
            return contest_obj[i]

# Pick a random winner for the mini-challenge, the reason it is random
# is because in the show, the mini-challenge doesn't affect the Queen's overall weekly score
def miniChallenge(contest_obj):
    seed = random.randint(0, countRemaining(contest_obj) - 1)
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

# calculate general ranking based off the type of challenge presented this week
# returns a unordered dictionary with the Queen's name as the key and their score as the value
def mainChallenge(contest_obj, challenge_obj):
    # So I guess the plan is to figure out a way to rank the Queens based on their performances
    # Each week, there's a certain number of Queens who are safe, and those who are on the top-bottom
    queenPerformanceList = {}
    for i in range(0, countRemaining(contest_obj)):
        currentQueen = contest_obj[i]
        queenPerformanceList[currentQueen.name] = getQueenPerformance(currentQueen, challenge_obj.challengeType)
        # Now that we have all the queen's performances for the main challenge,
        # we should add additional points for the runway
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

# Stats will be declared as floats at the moment (5 options):
# (A) Amazing = 0.8
# (B) Great = 0.6
# (C) Average = 0.5
# (D) Bad = 0.4
# (F) Awful = 0.3
def stat_to_float(specifiedStat):
    return {
            'A' : 0.8,
            'B' : 0.6,
            'C' : 0.5,
            'D' : 0.4,
            'F' : 0.3,
        }.get(specifiedStat,0.0)

# takes in a contestant object, current team challenge object, and
# a list of lists that contains the Queens' names (emulating teams)
# and a performance dictionary with each of the queen's individual scores
# returns a dictionary of Team Total Scores, mirroring the shuffled teamQueenList list
def teamMainChallenge(contest_obj, curr_team_challenge_obj, teamQueenList):
    queenPerformanceList = mainChallenge(contest_obj, curr_team_challenge_obj)
    teamTotalScores = {}
    counter = 0
    for i in range(0,len(teamQueenList)):
        teamTotalScores[i] = 0
    # search through the teamQueenList and append the current Team to the currentTeam list
    for currentTeam in teamQueenList:
        # now search for the current Queen in the current Team in the performance list
        for currentMem in currentTeam:
            # print(currentMem, "\n")
            teamTotalScores[counter] += findQueen(currentMem, queenPerformanceList)
        counter += 1
        # print("-----------------------")
    """
    for key in teamTotalScores:
        print(teamTotalScores[key])
    """
    return teamTotalScores

# used in conjunction with teamMainChallenge, takes in the currentMember and the queenPerformanceList
# from there, fill a variable called currTeamTotal to the currentMember that corresponds to the matching
# names from the queenPerformanceList (Ex: if currentMem = "Jiggly Caliente", the function will search
# for "Jiggly Caliente in the queenPerformanceList dict and then add Jiggly's corresponding score
# to the current team's total Score")
def findQueen(currentMem, queenPerformanceList):
    currTeamTotal = 0
    for key in queenPerformanceList:
        if(key == currentMem):
            currTeamTotal = currTeamTotal + queenPerformanceList[key]
    return currTeamTotal

# takes in a list of list that contains queens, emulating teams
# and a dictionary that contains the total scores for each team
# now we need to declare the top scores, bottom scores, and safe scores, and then place the
# queens in the top and bottom teams to the LOW, BTM2 or the Winner
def processTeamTopBottomSafe(teamQueenList, teamTotalScores, containSafe):
    topQueens = []
    safeQueens = []
    bottomQueens = []
    maxIdx = max(teamTotalScores, key=teamTotalScores.get)
    minIdx = min(teamTotalScores, key=teamTotalScores.get)

    random.shuffle(teamQueenList[maxIdx])
    random.shuffle(teamQueenList[minIdx])

    topQueens = teamQueenList[maxIdx][:3]
    bottomQueens = teamQueenList[minIdx][:3]

    if(len(teamQueenList[maxIdx]) > 3 or len(teamQueenList[minIdx]) > 3):
        containSafe = True
        safeQueens.extend(teamQueenList[maxIdx][3:])
        safeQueens.extend(teamQueenList[minIdx][3:])
    if(containSafe):
        for i in range(0, len(teamQueenList)):
            if((i != maxIdx) and (i != minIdx)):
                safeQueens.extend(teamQueenList[i])
    return [topQueens, safeQueens, bottomQueens]

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

def announceWinner(contest_obj, topQueens):
    print(topQueens[1], ", great job. You are safe!\n", \
         topQueens[0], ", conDragulations you are the winner of this week's challenge!", sep = "")
    if(len(topQueens) > 2):
        print(topQueens[2], ", nice work. You are safe.", sep = "")
    winner = getQueenObjFromName(contest_obj, topQueens[0])
    winner.winCt += 1
    return contest_obj

def announceBottomQueens(bottomQueens):
    print(bottomQueens[1], ", I'm sorry my dear but you are up for elimination.")
    if(len(bottomQueens) > 2):
        print(bottomQueens[0], ",you,")
        for count in range(0,2):
            keep_going = sanitised_input(". [y to continue]: ", \
            str.lower, range_ = ('y','Y'))
        keep_going = sanitised_input("are safe. [y to continue]: ", \
        str.lower, range_ = ('y','Y'))
        print(bottomQueens[2], ", I'm sorry my dear but you are up for elimination.")
    else:
        print(bottomQueens[0], ", I'm sorry my dear but you are also up for elimination.")

# For the actual lipsync, the bottom 2 queens must lipsync for their lives to impress Ru
# as this is their last chance to save themselves from elimination
# The rules are: both the Queens' danceStat is used to generate a random number between
# whatever the stat_to_float generator makes, and +1 of that
# the winCt will help them, giving them an extra .3 for every win to their final score
# their lipsyncCt will harm them, giving them a minus .25 for every previous lipsync to their final score
# the highest of the scores will be safe, and the other is declared the eliminated Queen
# returns a list with the savedQueen as the first member and the loserQueen as the next member
def lipsync(contest_obj, bottomQueens):
    elimQueen = ""
    savedQueen = ""
    queen1 = getQueenObjFromName(contest_obj, bottomQueens[len(bottomQueens) - 1])
    queen2 = getQueenObjFromName(contest_obj, bottomQueens[len(bottomQueens) - 2])

    """
    # Debug code
    for i in range(0, len(bottomStats)):
        for j in range(0, len(bottomStats[i])):
            print(bottomStats[i][j])
    """
    baseOut = { queen1.name : random.uniform(stat_to_float(queen1.danceStat), stat_to_float(queen1.danceStat) + 1) ,
                queen2.name : random.uniform(stat_to_float(queen2.danceStat), stat_to_float(queen2.danceStat) + 1) }

    # an attempt to implement the said pluses and minuses lel
    baseOut[queen1.name] = baseOut[queen1.name] + (.25 * queen1.winCt) - (.3 * queen1.lipsyncCt)
    baseOut[queen2.name] = baseOut[queen2.name] + (.25 * queen2.winCt) - (.3 * queen2.lipsyncCt)

    if(baseOut[queen1.name] < baseOut[queen2.name]):
        elimQueen = queen1.name
        savedQueen = queen2.name
    else:
        elimQueen = queen2.name
        savedQueen = queen1.name

    keep_going = sanitised_input("Ladies, I've made my decision. [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    print(savedQueen, ",shantay, you stay.", sep = "")
    return [savedQueen,elimQueen]

def deleteQueen(name, contest_obj):
    for i in range(0, countRemaining(contest_obj)):
        if(name == contest_obj[i].name):
            del contest_obj[i]
            break
    return contest_obj

def musicVideoTimeNonElim(currLipsync):
    keep_going = sanitised_input("In the end, the 3 remaining Queens have to lipsync for their lives. [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    print("The Queens faced off to the lipsync of the week:", currLipsync)
    keep_going = sanitised_input("However, they were all lucky, and were told they all moved onto the Grand Finale! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))

def grandFinaleTwoRU(testQueenObj, finalChallenge):
    finalistDict = {}
    sortedFinalList = []
    for i in range(0, countRemaining(testQueenObj)):
        finalistDict[testQueenObj[i].name] = testQueenObj[i].winCt

    winner = max(finalistDict.items(), key=operator.itemgetter(1))[0]

    for i in range(0, countRemaining(testQueenObj)):
        if(testQueenObj[i].name != winner):
            sortedFinalList.append(testQueenObj[i])
    sortedFinalList.append(getQueenObjFromName(testQueenObj, winner))

    keep_going = sanitised_input("The Final 3 Queens are set to meet their fates. [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    keep_going = sanitised_input("And the winner of Rupaul's Drag Race is... [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    print(winner, "!", sep = "")
    keep_going = sanitised_input("Congradulations to our new Season Winner!!. [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    keep_going = sanitised_input("Thanks for playing my little simulator!! [y to continue]: ", \
                                            str.lower, range_ = ('y', 'Y'))
    return sortedFinalList

def runFinalStats(loserQueens):
    for i in range(0, len(loserQueens)):
        print(loserQueens[i].name, "\nNumber of Mini-Challenges wins:", loserQueens[i].minWinCt, \
              "\nNumber of Main-Challenge Wins:", loserQueens[i].winCt, "\nNumber of times lipynced:", loserQueens[i].lipsyncCt)

#call main
main()
