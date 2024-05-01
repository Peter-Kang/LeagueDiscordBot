class DnDMonster:
    Name:str = ""                           #index 1
    Size:str = ""                           #2
    Type:str = ""                           #3                   
    Alignment:str = ""                      #4
    #defense
    AC:int = 0                              #5
    HP:int = 0                              #6
    #Movement
    SpeedNormal:str = ""                    #7
    SpeedFlying:str = ""                    #8
    SpeedSwimming:str = ""                  #9
    SpeedBurrowing:str = ""                 #10
    SpeedClimb:str = ""                     #11
    #stats
    Strength:int = 0                        #12
    Dexterity:int = 0                       #13
    Constitution:int = 0                    #14
    Intelligence:int = 0                    #15
    Wisdom:int = 0                          #16
    Charisma:int = 0                        #17
    #details
    SavingThrows:str = ""                   #18
    Skills:str = ""                         #19
    WeaknessResistanceImmunities:str = ""   #20
    Senses:str=""                           #21
    Languages:str=""                        #22
    #Challenge
    ChallengeRating:float=0.0               #23
    Experience:int = 0                      #24
    #Environments
    Unknown:bool = False                    #25
    AllEnvironments:bool = False            #26
    Arctic:bool = False                     #27
    Costal:bool = False                     #28
    Desert:bool = False                     #29
    Forest:bool = False                     #30
    Grassland:bool = False                  #31
    Hills:bool = False                      #32
    Jungle:bool = False                     #33
    Mountain:bool = False                   #34
    Swamp:bool = False                      #35
    Underdark:bool = False                  #36
    Underwater:bool = False                 #37
    Urban:bool = False                      #38
    #Extra info
    Additional:str = ""                     #39
    Source:str= ""                          #40

    def __init__(self, row:list[str]=[]):
        self.Name:str = row[1]                         
        self.Size:str = row[2]                    
        self.Type:str = row[3]                                         
        self.Alignment:str = row[4]                   
        #defense
        self.AC:int = int(row[5])                           
        self.HP:int = int(row[6])                     
        #Movement
        self.SpeedNormal:str = row[7]                        #7
        self.SpeedFlying:str = row[8]                        #8
        self.SpeedSwimming:str = row[9]                      #9
        self.SpeedBurrowing:str = row[10]                    #10
        self.SpeedClimb:str = row[11]                        #11
        #stats
        self.Strength:int = int(row[12])                     #12
        self.Dexterity:int =  int(row[13])                   #13
        self.Constitution:int =  int(row[14])                #14
        self.Intelligence:int =  int(row[15])                #15
        self.Wisdom:int =  int(row[16])                      #16
        self.Charisma:int =  int(row[17])                    #17
        #details
        self.SavingThrows:str = row[18]                      #18
        self.Skills:str = row[19]                            #19
        self.WeaknessResistanceImmunities:str = row[20]      #20
        self.Senses:str=row[21]                              #21
        self.Languages:str=row[22]                           #22
        #Challenge
        self.ChallengeRating:float= float(row[23])           #23
        self.Experience:int =  int(row[24])                  #24
        #Environments
        self.Unknown:bool = bool(row[25])                    #25
        self.AllEnvironments:bool = bool(row[26])            #26
        self.Arctic:bool = bool(row[27])                     #27
        self.Costal:bool = bool(row[28])                     #28
        self.Desert:bool = bool(row[29])                     #29
        self.Forest:bool = bool(row[30])                     #30
        self.Grassland:bool = bool(row[31])                  #31
        self.Hills:bool = bool(row[32])                      #32
        self.Jungle:bool = bool(row[33])                     #33
        self.Mountain:bool = bool(row[34])                   #34
        self.Swamp:bool = bool(row[35])                      #35
        self.Underdark:bool = bool(row[36])                  #36
        self.Underwater:bool = bool(row[37])                 #37
        self.Urban:bool = bool(row[38])                      #38
        #Extra info
        self.Additional:str = row[39]                        #39
        self.Source:str = row[40]                            #40