import telepot
from chatterbot import ChatBot
from chatterbot.utils import get_response_time
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chatbot:
    botAPI = None
    botServer = None
    registeredUser = []
    botCurrentStatus = "ready"
    def __init__(self, chatBotName, telegramTokenAPI): # done
        self.botAPI = telepot.Bot(telegramTokenAPI)
        self.botServer = ChatBot(chatBotName, storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.TimeLogicAdapter", "chatterbot.logic.BestMatch"], database='database/database.sqlite3')

    def handle(self, msg): # planning
        # some command
        return True

    def startBot(self): # planning
        # check botAPI
        # check botServer
        # check registeredUser
        # run the handle
        # run the view
        # set Ready
        return True

    def stopBot(self): # planning
        # some command
        return True

    def restartBot(self): # planning
        # some command
        return True

    def trainBot(self, mode): # planning
        if mode == "corpus":
            # train corpus
            pass
        elif mode == "all":
            # train all chat that possible
            pass
        else:
            return "Unknown mode"


    def getRegisteredUser(self): # planning
        # some command
        return True

    def isUserAllowed(self, username): # planning
        # some command
        return True

    def addRegisteredUser(self, username): # done
        self.registeredUser.append(username)
        self.appendToFile("configuration/registered_user", username)
        return True

    def fileToList(self, filename): # done
        fileUser = open(filename, mode='r').readlines()
        listTemp = []
        for item in fileUser:
            item = item.replace("\n", "")
            listTemp.append(item)
        return listTemp

    def appendToFile(self, filename, text): # done
        fileUser = open(filename, mode='a')
        fileUser.write(text)
        fileUser.write("\n")
        fileUser.close()
        return True

    def getBotStatus(self, parameter_list): # done
        return self.botCurrentStatus

    def setReadyBotStatus(self): # done
        self.botCurrentStatus = "ready"
    
    def setStopBotStatus(self): # done
        self.botCurrentStatus = "stop"