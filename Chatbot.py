class Chatbot:
    historic = []
    know_people = ['Filipe', 'Davi', 'Rann']

    def __int__(self, name):
        self.name = name

    def listening(self):
        # Take the user's answers and processing it
        frase = input('>: ')
        frase = frase.lower()
        return frase

    def think(self, frase):
        if frase == 'hi':
            return 'Hey, what is your name?'
        if self.historic[-1] == 'Hey, what is your name?':
            name = self.catch_name(frase)
            ans = self.answer_name(name)
            return ans
        if frase == 'bye':
            return 'bye'
        return 'I cannot understand'

    def answer_name(self, name):
        if name in self.know_people:
            frase = 'Welcome '
        else:
            frase = 'Nice to meet you '
        return frase + name

    def catch_name(self, name):
        if 'my name is ' in name:
            name = name[11:]
        name = name.title()
        return name

    def speak(self, frase):
        print(frase)
        self.historic.append(frase)
