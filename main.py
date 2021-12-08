import telepot
import json
from chatbot import Severina

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

telegram.message_loop(receiveMsg)
print ("em execução!")

while True:
    pass