from .API.Champions import Champions as ChampionsAPI 
from .API.Summoners import Summoners as SummonersAPI
from .API.Matches import Matches as MatchesAPI, Match
import random
from DataAccess.LeagueDatabase import LeagueDatabase
from .DataUtil.SummonerStatSummary import SummonerStatSummary, SummonerStatSummaryResults
import json

class league:

    def __init__(self, riotAPIKey:str,db:LeagueDatabase):
        self.RIOT_API_KEY:str = riotAPIKey
        #API call objects
        self.ChampionData:ChampionsAPI = ChampionsAPI(riotAPIKey)
        self.UserSummonerAPI:SummonersAPI = SummonersAPI(riotAPIKey)
        self.MatchesAPI:MatchesAPI = MatchesAPI(riotAPIKey)
        #Features/DataModels
        self.SummonerStat = SummonerStatSummary()
        #Database
        self.db:LeagueDatabase = db
        #commonly used data
        self.userToSummonerPUUID:dict[str:str] = {} #discordUser:string to summonerPUUID:string
        self.matchCache:dict[str:Match] = {}#matchName:string to json
        #inits
        self.__initUserToSummonerPUUID()
        self.__initMatchCache()

    def __initUserToSummonerPUUID(self) -> None:
        userIDIndex:int = 0
        summonerPUUIDIndex:int = 1
        result:list[tuple[str]] = self.db.SummonerDB.getAllUsers()
        #populate
        for row in result:
            self.userToSummonerPUUID[row[userIDIndex]] = row[summonerPUUIDIndex]

    def __initMatchCache(self) -> None:
        matchIDIndex:int = 0
        jsonIndex:int = 2
        result:list[tuple[str]] = self.db.MatchesDB.getMatches()
        for row in result:
            self.matchCache[row[matchIDIndex]] = Match(self.RIOT_API_KEY,row[matchIDIndex],json.loads(row[jsonIndex]))
        
    def randomChampion(self) -> str:
        champ_count:int = len(self.ChampionData.ChampionList)-1
        result:str = "No Data"
        if champ_count >= 0:
            index:int = random.randrange(0, champ_count, 1)
            result:str = self.ChampionData.ChampionList[index][0]
        return result

    def register(self, user:str , summoner:str) -> str:
        puuid:str = self.UserSummonerAPI.getSummonerPUUID( summoner )
        if(puuid != ""):
            self.userToSummonerPUUID[str(user)] = puuid
            self.db.SummonerDB.addOrUpdateUserToSummonerMapping(user, summoner, puuid)
        return puuid

#summoner stats
    def updateMissingMatchesData(self, matchList:list[Match]) -> None:
        for match in matchList:
            self.matchCache[match.matchID] = match
            self.db.MatchesDB.addMatches(match.matchID,match.EndEpoch,json.dumps(match.results))

    def getListOfMatches(self, matchListString:list[str]) -> list[Match]:
        result:list[Match] = []
        for matchID in matchListString:
            result.append(self.matchCache[matchID])
        return result
    
    async def populateMissingMatches(self, matchListString:list[str])-> None:
        matchListStringMissing:list[str] = []
        #filter out the list of ids we already have
        for matchStr in matchListString :
            if not matchStr in self.matchCache:
                matchListStringMissing.append(matchStr)
        # get the matches missing
        matchMissingListMatch:list[Match] = await self.MatchesAPI.getMatchesFromList(matchListStringMissing) # turn list of match ids to list of completed matches
         # save the matches to db and add to match cache
        self.updateMissingMatchesData(matchMissingListMatch)

    async def getUserStatus(self, userID:str) -> str:
        if( not (userID in self.userToSummonerPUUID)):
            return "Not Registered"
        puuid:str = self.userToSummonerPUUID[userID]
        matchStringList:list[str] = await self.UserSummonerAPI.getMatchesFromSummoner(puuid) # list of match ids
        await self.populateMissingMatches(matchStringList)
        matchList = self.getListOfMatches(matchStringList)
        #report stats
        res:SummonerStatSummaryResults = self.SummonerStat.ListOfMatchesToSummonerStat(matchList,puuid)
        return format(res)