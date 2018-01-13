import telepot
from chatterbot import ChatBot
from chatterbot.utils import get_response_time
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Chatbot:
    botAPI = None
    botServer = None
    registeredUser = []
    def __init__(self, chatBotName, telegramTokenAPI):
        self.botAPI = telepot.Bot(telegramTokenAPI)
        self.botServer = ChatBot(chatBotName, storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.TimeLogicAdapter", "chatterbot.logic.BestMatch"], database='database/database.sqlite3')

    def handle(self, msg):
        # some command
        return True

    def startBot(self):
        # some command
        return True

    def stopBot(self):
        # some command
        return True

    def restartBot(self):
        # some command
        return True

    def getRegisteredUser(self):
        # some command
        return True

    def isUserAllowed(self, username):
        # some command
        return True

    def addRegisteredUser(self, username):
        # some command
        return True

    def fileToList(self, filename):
        # some command
        return True

    def appendToFile(self, filename, text):
        # some command
        return True

