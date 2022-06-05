from Chatbot import Chatbot

Bot = Chatbot()
while True:
    frase = Bot.listening()
    ans = Bot.think(frase)
    Bot.speak(ans)
    if ans == 'bye':
        break
