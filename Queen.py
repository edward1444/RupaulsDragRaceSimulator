# George Juarez

import collections

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

    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

    name = property(getname, setname)
    '''
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

    def set_name(name):
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
    def get_lipsyncCt(lipsyncCt):
        self.__lipsyncCt = lipsyncCt
    '''
    
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

s4OrderedDict = collections.OrderedDict(s4_key_val_pairs)

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
    printRemaining()

    '''
    while(keep_going.lower() == 'y'):
        print(0)
        keep_going = input("Enter y to exit: ")
    '''
    
def printRemaining():
    
    for i in range(0, len(s4_preset_contest_obj)):
        print(s4_preset_contest_obj[i].name)


            
#call main
main()
