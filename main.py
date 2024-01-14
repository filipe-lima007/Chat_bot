from Chatbot import Chatbot

bot = Chatbot()

while True:
    question = input('>: ')
    frase = bot.listening(question)
    ans = bot.think(frase=frase)
    ans_to_speak = bot.speak(frase=ans)
    if ans_to_speak:
        print(ans_to_speak)
    if ans == 'bye':
        break