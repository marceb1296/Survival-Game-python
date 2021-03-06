#!/usr/bin/env python
# coding: utf-8


class Lang():
    
    def es(self):
        data = [
            "Salud",
            "Hambre",
            "Escudo",
            "Irse",
            "Ventana",
            "Puerta",
            "Tienes",
            "Ganzúa", 
            "Cuerda",
            "Arboles",
            "Piedra",
            "Animales", 
            "¡Haz encontrado una cabaña!",
            "Madera",
            "Vida restante hacha de madera",
            "¡Se ha roto un hacha de madera!",
            "Vida restante hacha de piedra",
            "¡Se ha roto un hacha de piedra!",
            "No hay árboles que talar!",
            "Vida restante pico",
            "¡Se ha roto un Pico!",
            "No hay piedras que picar!",
            "¡Haz creado un Hacha de madera!",
            "¡No tienes materiales suficientes!",
            "¡Haz creado un Hacha de piedra!",
            "Te hace falta",
            "¡Haz creado un Pico!",
            "¡Haz creado un cuchillo!",
            "¡Haz creado un cuchillo de madera!",
            "¡Haz reconstruido tu armadura superior!",
            "¡Haz reconstruido tu armadura inferior!",
            "¡Haz construido una armadura superior!",
            "¡Haz construido una armadura inferior!",
            "¡Solo puedes crear una armadura!",
            "¡Oh no... se ha roto la armadura inferior!",
            "¡Oh no... se ha roto la armadura superior!",
            "Haz causado",
            "Haz sufrido",
            "Vida restante del animal",
            "Vida restante del cuchillo",
            "¡Oh no... se ha roto el cuchillo!",
            "¡Oh no... se ha roto el cuchillo de madera!",
            "Haz obtenido",
            "¡Haz matado al animal!",
            "¡No hay animales cerca!",
            "¡CUIDADO! Tu vida esta alcanzando un numero critico",
            "Uff, has huido a tiempo...",
            "¡No hay animales cerca para huir!",
            "Fogata echa",
            "¡Ya tienes una fogata echa!",
            "¡Carne cocinada!",
            "¡No tienes carne que cocinar!",
            "¡No tienes una fogata puesta!",
            "¡No puedes comer más!",
            "Debi cocinarla mejor...",
            "Cocida hubiese estado perfecta",
            "¡No tienes carne que comer!",
            "¡Esa chuleta estuvo deliciosa!",
            "Parece que no hay nada",
            "Parece que aquello podria ser una cabaña...\nNo se si ir a investigar o mejor seguir:",
            "La puerta tiene seguro, y no puedo ver nada por las ventanas, la unica forma de entrar seria si tirase la puerta o rompiera una ventana:",
            "Mejor seguire, quien sabe que o a quien habria encontrado ahi...",
            "Tengo que tomar una decisión rápido antes de que algo o alguien llegue...",
            "Me alegro de haber encontrado esta ganzua antes",
            "Aqui vamos, espero no haga mucho ruido...",
            "Esto es una terrible idea, mejor me voy",
            "Tengo que elejir una opcion",
            "Haz encontrado", 
            "Parece que no hay nada mas, pero aquella pintura, chimenea y cajonera dan un toque extraño al ambiente",
            "Parece que la ultima vez que se utilizo fue no mas de 5 horas",
            "No entiendo porque colgaria esto...",
            "Un poco malgastada...",
            "Es hora de irse",
            "El ruido trajo a un lobo",
            "Te ha echo",
            "de daño",
            "de piedra",
            "de madera", 
            "¡No hay cabañas cerca!",
            "de protección",
            "de cuero",
            "de carne cruda",
            "de carne cocida",
            "de cuerda",
            "carne",
            "Cuero",
            "Hacha",
            "Cuchillo",
            "Pico",
            "Chimenea",
            "Pintura",
            "Cajonera",
            "Daño" #92
        ]
        
        return data
    
    def en(self):
        data = [
            "Health",
            "Hungry",
            "Shield",
            "Go away",
            "Window",
            "Door",
            "You have",
            "Picklock",
            "Rope",
            "Trees",
            "Stone",
            "Animals",
            "You've found a cabin!",
            "Wood",
            "Wooden ax life remaining",
            "Wooden ax broked!",
            "Stone ax life remaining",
            "Stone ax broked!",
            "There are no trees to cut down!",
            "Pickaxe life remaining",
            "Pickaxe broked",
            "There is no stone to chop",
            "You've build a wooden axe!",
            "You don't have enough resource!",
            "You've build a stone axe!",
            "You need",
            "You've build a Pickaxe!",
            "You've build a knife!",
            "You've build a wooden knife!",
            "You've rebuild your upper armor!",
            "You've rebuild your lower armor!",
            "You've build an upper armor!",
            "You've build a lower armor!",
            "You only can create one armor",
            "Oh no... lower armor has broken",
            "Oh no... upper armor has broken",
            "You've done",
            "You've suffered",
            "Animal life remaining",
            "Knife life remaining",
            "Oh no... knife has broken",
            "Oh no... wooden knife has broken",
            "You got",
            "You killed the animal!",
            "No animals nearby!",
            "BECAREFUL! Your life is reaching a critical number",
            "Uff, you run on time...",
            "No animals nearby to run",
            "Bonfire created",
            "You already have a bonfire made!",
            "Cooked meat!",
            "You don't have meat to cook!",
            "You don't have a bonfire made",
            "You can't eat more!",
            "Should i cooked...",
            "Cooked would be perfect",
            "You don't have meat to eat!",
            "That cutlet was delicious",
            "It seems there's nothing",
            "It seems that that would be a cabin...\nI don't know whether to go investigate or better continue:",
            "The door has a lock and I can't see anything through the windows, the only way to get in would be if I broke the door or broke a window:",
            "I better go on, who knows what or who would have found there...",
            "I have to make a quick decision before something or someone come...",
            "Im glad to have find this picklock before",
            "Here we go, I hope it doesn't make too much noise...",
            "This is a terrible idea, i better go",
            "I need take a desicion",
            "You've found",
            "It seems that there's nothing else, but the painting, fireplace and chest of drawers give a strange touch to the environment",
            "It seems that the last time it was used was not more than 5 hours ago",
            "I don't understand why someone would hang this...",
            "A little dirty",
            "Time to go",
            "The noise brought a wolf",
            "Has made you",
            "of damage",
            "of stone",
            "of wood",
            "No cabins nearby!",
            "of protection",
            "of leather",
            "of raw meat",
            "of cooked meat",
            "of rope",
            "meat",
            "leather",
            "Axe",
            "Knife",
            "Pickaxe",
            "Fireplace",
            "Painting",
            "Chest of drawers",
            "Damage" #92
        ]
        
        return data
