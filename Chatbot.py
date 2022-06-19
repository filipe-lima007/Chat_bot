import json
import sys
import os
import wikipedia
import subprocess as sub


class Chatbot():
    try:
        memory = open('Filipe.json', 'r')
    except FileNotFoundError:
        memory = open('Filipe.json', 'w')
        memory.write('[["Filipe", "Rann"], {"hi": "Hey, what is your name?", "bye": "bye"}]')
        memory.close()
        memory = open('Filipe.json', 'r')
    know_people, frases = json.load(memory)
    memory.close()
    historic = [None,]

    def __int__(self, name):
        self.name = name

    def listening(self, frase):
        if 'execute' in frase:
            return frase
        frase = frase.lower()
        return frase

    def think(self, frase):
        if "what is " in frase or "what's " in frase:
            frase = frase.title()
            term = frase.replace('What Is ', '').replace("What's ", '').strip()
            try:
                return wikipedia.summary(term, sentences=1)
            except wikipedia.exceptions.DisambiguationError as e:
                return str(e.options)
            except wikipedia.PageError as e_1:
                return str(e_1)
        if frase in self.frases:
            return self.frases[frase]
        if frase == 'learn':
            key = input('Write a frase: ')
            ans1 = input('Write a answer: ')
            self.frases[key] = ans1
            self.write_memory()
            return 'Learned!'
        if self.historic[-1] == 'Hey, what is your name?':
            name = self.catch_name(frase)
            ans = self.answer_name(name)
            return ans
        try:
            ans = str(eval(frase))
            return ans
        except:
            pass
        return 'I cannot understand'

    def answer_name(self, name):
        if name in self.know_people:
            frase = 'Welcome '
        else:
            frase = 'Nice to meet you '
            self.know_people.append(name)
            self.write_memory()
        return frase + name

    def catch_name(self, name):
        if 'my name is ' in name:
            name = name[11:]
        name = name.title()
        return name

    def write_memory(self):
        memory = open('Filipe.json', 'w')
        json.dump([self.know_people, self.frases], memory)
        memory.close()

    def speak(self, frase):
        if 'execute ' in frase:
            plform = sys.platform
            comand = frase.replace('execute ', '')
            if 'win' in plform:
                os.startfile(comand)
            if 'linux' in plform:
                try:
                    sub.Popen(comand)
                except FileNotFoundError:
                    sub.Popen(['xdg-open', comand])
        else:
            print(frase)
        self.historic.append(frase)
