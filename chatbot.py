import os, time
from handle import Handle

class Chatbot:
    botHandle = None
    registeredUser = []
    botCurrentStatus = "stop"
    def __init__(self, chatBotName, telegramTokenAPI): # done
        self.botHandle = Handle(chatBotName, telegramTokenAPI)
        self.startBot()

    def startBot(self): # planning
        # check bot Status
        if (self.getBotStatus() == "ready"):
            return True
        # check botHandle
        if (self.botHandle == None):
            print("Bot is not initialized yet")
            return False
        # check registeredUser (pass)
        # run the handle
        os.system("python handle.py")
        # run the view
        # set Ready
        self.setReadyBotStatus()
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

    def getBotStatus(self): # done
        return self.botCurrentStatus

    def setReadyBotStatus(self): # done
        self.botCurrentStatus = "ready"
    
    def setStopBotStatus(self): # done
        self.botCurrentStatus = "stop"