# Pequeño juego survival escrito en Python

[Ingles](/README.md)

## **Metas:**

- Añadirle mas armas (espada, arco...)
- Enemigos (animales, jefes, monstruos...)
- Agregar cualquier cosa que te imagines
    

## **Como funciona:**

**Descarga**

`git clone https://github.com/marceb1296/Survival-Game-python.git`

**Inicio rapido**:

`cd Survival-Game-python`

`python main.py`

**Inicio personalizado:**

- Extraiga la carpeta Survival_Game a su directorio de trabajo

- En tu archivo .py
 
```
from Survivial_Game.init import Start

name = "My name"

# Cargar lenguajes
with open('Survival_Game/lang.json', 'r') as F:
    languaje = json.loads(F.read())

get_lang = input('\nEnglish/en | Español/es?: ').lower()

lang = languaje.get('en')

if get_lang.startswith('es'):
    lang = languaje.get('es')

lang_start = lang.get("start")

name = input("\n%s : " % lang_start[0])

#Estableciendo nombre e idioma
start = Start(name, lang)

#Iniciando juego
start.starting_game()

#Tus funciones personalizadas
...

#comandos del juego
print(start.enviroment())
start.find_cabin() #Unico comando que no necesita print()
print(start) #Mostrar status del jugador

#detener/terminar juego
start.state = True
```

### **Comandos:**

```
enviroment() > Mostrar entorno (Arboles, piedras, animales, cabaña)
tree_cut() > Talar arboles
stone_chop() > Picar piedras
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
