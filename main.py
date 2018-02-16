from chatbot import Chatbot
import time

def isValidKey(key):
	# some code
	# example 
	# check key have 45 char
	if(len(key) != 45):
		return False
	# check char at 9 is ':'
	if(key[9] != ':'):
		return False
	return True

def inputKey():
	key = input("API Key : ")
	# print(len(key))
	time.sleep(3)
	if (isValidKey(key)):
		return key
	else:
		print("Not valid key", end="\n\n")
		print("- Re-input key -")
		inputKey()

print("\tWelcome to Expost Bot")
print("----------------------------------------------------")
print("Input the API Telegram Bot Key from Bot Father")
key = inputKey()
bot = Chatbot("Expost", key)
