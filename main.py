import json
from Survival_Game import Start

# Load languajes
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
    command = input("%s | %s: " % (lang[94], lang[95]))
    
    if command == lang[96]:
        print()
        game.state = True
        break
    elif command == lang[97]:
        print(game)
    