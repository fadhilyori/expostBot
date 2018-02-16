import telepot
from chatterbot import ChatBot
from chatterbot.utils import get_response_time
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class Handle:
	botAPI = None
	botServer = None

	def __init__(self, chatBotName, telegramTokenAPI):
		self.botAPI = telepot.Bot(telegramTokenAPI)
		self.botServer = ChatBot(chatBotName, storage_adapter='chatterbot.storage.SQLStorageAdapter', logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.TimeLogicAdapter", "chatterbot.logic.BestMatch"], database='database/database.sqlite3')

	if __name__ == '__main__':
		print("Bot Started")
