# Little survival game in python

[Spanish](/README_es.md)

### **Goals:**

- Add more weapons (sword, arch...)
- Enemies (animals, bosses, monsters...)
- Add whatever you can imagine
    

### **How it works:**

- Create your own file

```
from Survival_Game.init import Start

name = "My name"

#game init > name 
start = Start(name) #Start(name, "es") for spanish

#start game
start.starting_game()

#game commands
print(start.enviroment())
start.find_cabin() #only command without print()
print(start) #show player status

#stop/finish game
start.state = True
```

### **Commands:**

```
enviroment() > Show enviroment (trees, stones, animals, cabin)
tree_cut() > Cut trees
stone_cut() > Chop stone
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
