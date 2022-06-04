from chatbot_tools import *

# Main
print('Hi, what is your name?')
name = catch_name(answer())
ans = answer_name(name)
print(ans)


while True:
    ans = answer()
    if ans == 'bye':
        break
    else:
        print('Write anything')
print('Bye bye')