import json
from Survival_Game import Start

# Load languajes
with open('Survival_Game/lang.json', 'r') as F:
    languaje = json.loads(F.read())

get_lang = input('\nEnglish/en | Español/es?: ').lower()

lang = languaje.get('en')

if get_lang.startswith('es'):
    lang = languaje.get('es')

lang_start = lang.get("start")

name = input("\n%s : " % lang_start[0])

game = Start(name, lang)
game.start_game()

while True:
    command = input("%s | %s: " % (lang_start[1], lang_start[2])).lower()
    
    if command == lang_start[2]:
        print(lang.get("commands"))
    elif command == lang_start[3]:
        print(lang_start[4])
        game.state = True
        break
    elif command == lang_start[5]:
        print(game.enviroment())
    elif command == lang_start[6]:
        print(game)
    elif command == lang_start[7]:
        print(game.tree_cut())
    elif command == lang_start[8]:
        print(game.stone_chop())
    elif command == lang_start[9]:
        print(game.b_axe_wood())
    elif command == lang_start[10]:
        print(game.b_axe_stone())
    elif command == lang_start[11]:
        print(game.b_pickaxe_stone())
    elif command == lang_start[12]:
        print(game.b_knife_wood())
    elif command == lang_start[13]:
        print(game.b_knife())
    elif command == lang_start[14]:
        print(game.b_shield_upper())
    elif command == lang_start[15]:
        print(game.b_shield_lower())
    elif command == lang_start[16]:
        print(game.bonfire())
    elif command == lang_start[17]:
        print(game.cook())
    elif command == lang_start[18]:
        print(game.eat())
    elif command == lang_start[19]:
        print(game.kill_anm())
    elif command == lang_start[20]:
        print(game.run())
    elif command == lang_start[21]:
        game.find_cabin()
    