import telepot
import json
from chatbot import Severina
from telepot.loop import MessageLoop

with open('token.json') as jsonFile:
    token = json.load(jsonFile)
telegram = telepot.Bot(token)
bot = Severina("memoria")

def receiveMsg(msg):
    phrase = bot.listen(phrase=msg['text'])
    response = bot.think(phrase)
    bot.speak(response)
    msgType, chatType, chatID = telepot.glance(msg)
    telegram.sendMessage(chatID, response)


MessageLoop(telegram, receiveMsg).run_as_thread()
print ('Listening ...')

while True:
    pass