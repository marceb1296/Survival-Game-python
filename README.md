# Little survival game in python

[Spanish](/README_es.md)

## **Goals:**

- Add more weapons (sword, arch...)
- Enemies (animals, bosses, monsters...)
- Add whatever you can imagine
    

## **How it works:**

**Clone the repository**

`git clone https://github.com/marceb1296/Survival-Game-python.git`

### **Quick start:**

`cd Survival-Game-python`

`python main.py`

### **Custom start:**

- Extract the dir Survival_Game to your work directory

- In your file .py

```
from Survival_Game import Start

name = "My name"

# Load languajes
with open('Survival_Game/lang.json', 'r') as F:
    languaje = json.loads(F.read())

get_lang = input('\nEnglish/en | Español/es?: ').lower()

# Set languaje
lang = languaje.get('en')

if get_lang.startswith('es'):
    lang = languaje.get('es')

lang_start = lang.get("start")

name = input("\n%s : " % lang_start[0])

#game init > name & lang
game = Start(name, lang)

#start game
start.starting_game()

# do your custom stuffs 
...

#game commands
print(start.enviroment())
start.find_cabin() #only command without print()
print(start) #show player status

#stop/finish game
start.state = True
```

## **Commands:**

```
enviroment() > Show enviroment (trees, stones, animals, cabin)
tree_cut() > Cut trees
stone_chop() > Chop stone
b_axe_wood() > Build wooden axe
b_axe_stone() > Build stone axe
b_pickaxe_stone() > Build pickaxe
b_knife() > Build knife
b_knife_wood() > Build wooden knife
b_shield_upper() > Build upper armor
b_shield_lower() > Build lower armor
kill_anm() > Kill animal
run() > Run from animal
bonfire() > Build bonfire
cook() > Cook
eat() > Eat
find_cabin() > Go to cabin
```
