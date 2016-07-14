# George Juarez

import collections

class Queen:

    def __init__(name, sewStat, danceStat, singStat, actStat, humorStat, lipsyncCt = 0):
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


def main():
    for key in s4OrderedDict :
        print(key)


main()
