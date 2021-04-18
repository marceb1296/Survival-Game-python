# Pequeño juego survival escrito en Python

[English](/README.md)

### **Metas:**

- Añadirle mas armas (espada, arco...)
- Enemigos (animales, jefes, monstruos...)
- Agregar cualquier cosa que te imagines
    

### **Como funciona:**

- Crea tu propio archivo
 
```
from Survivial_Game.init import Start

name = "My name"

#Estableciendo nombre e idioma
start = Start(name) #Start(name, "es") para español

#Iniciando juego
start.starting_game()

#comandos del juego
print(start.enviroment())
start.find_cabin #Unico comando que no necesita print()
print(start) #Mostrar status del jugador

#detener/terminar juego
start.state = True
```

### **Comandos:**

```
enviroment() > Mostrar entorno (Arboles, piedras, animales, cabaña)
tree_cut() > Talar arboles
stone_cut() > Picar piedras
b_axe_wood() > Crear Hacha de madera
b_axe_stone() > Crear Hacha de piedra
b_pickaxe_stone() > Crear pico
b_knife() > Crear cuchillo
b_knife_wood() > Crear cuchillo de madera
b_shield_upper() > Crear armadura superior
b_shield_lower() > Crear armadura inferior
kill_anm() > Matar animal
run() > Correr de algun animal
bonfire() > Crear fogata
cook() > Cocinar
eat() > Comer
find_cabin() > Ir a cabaña
```
