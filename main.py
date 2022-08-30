import json
from Survival_Game import Start

with open('Survival_Game/lang.json', 'r') as F:
    languaje = json.loads(F.read())

get_lang = input('\nEnglish/en | Español/es?: ').lower()

lang = languaje.get('en')

if get_lang.startswith('es'):
    lang = languaje.get('es')

name = input("\n%s : " % lang[93])

game = Start(name, lang)
game.start_game()

while True:
    command = input("%s: " % lang[94])
    
    if command == 'exit':
        print()
        game.state = True
        break
    elif command == 'status':
        print(game)
    