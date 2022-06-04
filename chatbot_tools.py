def answer():
    # Take the user's answers and processing it
    ans = input('>: ')
    ans = ans.lower()
    return ans


def catch_name(name):
    if 'my name is ' in name:
        name = name[11:]
    name = name.title()
    return name


def answer_name(name):
    know_people = ['Filipe', 'Davi', 'Rann']

    if name in know_people:
        frase = 'Welcome '
    else:
        frase = 'Nice to meet you '
    return frase + name