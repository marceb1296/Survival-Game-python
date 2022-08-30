#!/usr/bin/env python
# coding: utf-8

from random import choices
from random import randint



class Game():
    
    #IMPORTANT
    #If you'll add new stuff, dont forget to add output string to lang.py
    #Example lang.py
    #Data = [
    #    "Damage", #92
    #    "You create a sword"]
    #game.py
    #The last index of lang.py is [92], so you'll set print()/return self.lang[93]    

    def __init__(self):
        
        #Game init
        #self.name = name
        self.healt = 100
        self.hungry = 100
        self.shield = 0
        #self.lang = lang
        #Materials
        self.material_wood = 0
        self.material_stone = 0
        #axe
        self.hacha_wood = 0
        self.hacha_wood_life = 100
        self.build_hacha_wood = 30 # wood
        #axe stone
        self.hacha_stone = 0
        self.hacha_stone_life = 100
        self.build_hacha_stone = [30, 15] # wood/stone
        #pickaxe only stone
        self.pickaxe_stone = 0
        self.pickaxe_stone_life = 100
        self.build_pickaxe_stone = [30, 20] # wood/stone
        #Knife
        self.knife = 0
        self.knife_life = 100
        self.knife_damage = 30
        self.build_knife = [10, 30] # wood/stone
        #Knife wood
        self.knife_wood = 0
        self.knife_wood_life = 100
        self.knife_wood_damage = 10
        self.build_knife_wood = 30 #wood
        #Build materials 
        self.leather = 0
        self.meat = 0
        self.meat_cooked = 0
        self.rope = 0
        self.ganzua = 0
        #upper armor
        self.shirtfront = 75
        self.shield_shirtfront = 0
        self.build_shirtfront_cost = [50, 20] # leather/rope 
        #Lower armor
        self.kneepads = 25
        self.shield_kneepads = 0
        self.build_kneepads_cost = [25, 10] #leather/rope
        #Environment
        self.times_ent = 0
        #Animals
        self.animals = {
            "anm": ["buey", "jabali", "lobo"], 
            "life": [120, 80, 90], 
            "damage": [3, 5, 10], 
            "leather": [10, 8, 5], 
            "meat": [5, 3, 1], 
            "rope": [5, 3, 2]
        } 
        #Animals rewards
        self.kill_anm_life = 0
        self.kill_anm_damage = 0
        self.kill_anm_leather = 0
        self.kill_anm_meat = 0
        self.kill_anm_rope = 0
        
        self.animal_choice = [0, 1, 2]
        #Not implemented
        self.archer = 0
        self.build_archer = [50, 10, 30] #wood/stone/rope
                
        self.special_arrows = 0
        self.special_arrows_damage = 80
        #Fist damage
        self.puño_damage = 5
        #three/wood
        self.three = 0
        self.wood = 5
        #rock/stone
        self.rock = 0
        self.stone = 3
        #game state
        self.state = False
        #bonfire
        self.fogata_state = False
        #cabins
        self.state_cabaña = False
        # Probabilitys
        self.probability_get_from_anm = [0, 1]
        self.probability_eat_damage = [0, 1, 0]
        self.probability_anm = [0, 1, 0, 0, 0]
        self.probability_cabaña = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.probability_three = [0, 0, 1, 0, 0, 2, 0, 0, 1, 0]
        self.probability_stone = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    
    
    def enviroment(self):
        
        if not self.state:
            
            self.times_ent += 1
            #Make false, avoid reuse
            self.fogata_state = False
            
            return_data = ""
            
            self.three = choices(self.probability_three)[0]
            self.rock = choices(self.probability_stone)[0]
            self.anm_show = choices(self.probability_anm)[0]
            self.cabaña_show = choices(self.probability_cabaña)[0]
            
            return_data += f"{self.lang[9]}: {self.three}\n{self.lang[10]}s: {self.rock}\n"
            
            if self.anm_show == 1:
                self.set_animal = choices(self.animal_choice)[0]
                self.get_from_anm = choices(self.probability_get_from_anm)[0]
                                            
                self.kill_anm_life = self.animals['life'][self.set_animal]
                self.kill_anm_damage = self.animals['damage'][self.set_animal]
                self.kill_anm_leather = self.animals['leather'][self.set_animal]
                self.kill_anm_meat = self.animals['meat'][self.set_animal]
                self.kill_anm_rope = self.animals['rope'][self.set_animal]
                
                return_data += f"{self.lang[11]}: {self.anm_show} -> {self.animals['anm'][self.set_animal]}\n"
           
            if self.cabaña_show == 1:
                return_data += f"{self.lang[12]}"
                
            return return_data
        
    
    def tree_cut(self):
        
        data = ""
        
        if self.three > 0:
            
            if self.hacha_wood > 0:
                self.material_wood += 3 + (self.wood * self.three)
                data += f"{self.lang[13]} + {(self.wood * self.three)} -> + 3\n"
                self.hacha_wood_life -= 20
                data += f"{self.lang[14]} -> {self.hacha_wood_life}\n"
                if self.hacha_wood_life <= 0:
                    self.hacha_wood -= 1
                    data += "{self.lang[15]}\n"
                    self.hacha_wood_life = 100
                self.three = 0
            elif self.hacha_stone > 0 and self.hacha_wood == 0:
                self.material_wood += 5 + (self.wood * self.three)
                data += f"{self.lang[13]} + {(self.wood * self.three)} -> + 5\n"
                self.hacha_stone_life -= 10
                data += f"{self.hacha[16]} -> {self.hacha_stone_life}\n"
                if self.hacha_stone_life <= 0:
                    self.hacha_stone -= 1
                    data += f"{self.lang[17]}\n"
                    self.hacha_stone_life = 100
                self.three = 0
            else:
                self.material_wood += (self.wood * self.three)
                data += f"{self.lang[13]} + {(self.wood * self.three)}\n"
                self.three = 0                
          
        else:
            data += f"{self.lang[18]}"
        
        return data
    
    
    def stone_cut(self):
        
        data = ""
        
        if self.rock > 0:
            if self.pickaxe_stone > 0:
                self.material_stone += 3 + (self.stone * self.rock)
                data += f"{self.lang[10]} + 3 -> + 3\n"
                self.pickaxe_stone_life -= 10
                data += f"{self.lang[19]} -> {self.pickaxe_stone_life}\n"
                if self.pickaxe_stone_life <= 0:
                    self.pickaxe_stone -= 1
                    data += f"{self.lang[20]}\n"
                    self.pickaxe_stone_life = 100
                self.rock = 0
            else:
                self.material_stone += (self.stone * self.rock)
                data += f"{self.lang[10]} + 3\n"
                self.rock = 0
        else:
            data += f"{self.lang[21]}"
        return data
    
    # b_ instead of build_ cuz already used 
    def b_axe_wood(self):
        
        data = ""
        
        if self.material_wood >= self.build_hacha_wood:
            self.hacha_wood += 1
            self.material_wood -= 30
            data += f"{self.lang[22]} -> + 3 {self.lang[77]}!\n"
        else:
            data_wood = self.build_hacha_wood - self.material_wood
            
            data += f"{self.lang[23]}\n{self.lang[25]} -> {data_wood} {self.lang[77]}\n"
        return data
    
    
    def b_axe_stone(self):
        
        data = ""
        
        if self.material_wood >= self.build_hacha_stone[0] and self.material_stone >= self.build_hacha_stone[1]:
            self.hacha_stone += 1
            self.material_wood -= 30
            self.material_stone -= 15
            data += f"{self.lang[24]} -> + 5 {self.lang[77]}!\n"
        else:
            send_data += f"{self.lang[23]}\n"
            
            
            if not self.material_wood >= self.build_hacha_stone[0]:
                data_wood = self.build_hacha_stone[0] - self.material_wood
                send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[77]}"
            if not self.material_stone >= self.build_hacha_stone[1]:
                data_stone = self.build_hacha_stone[1] - self.material_stone
                send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[76]}"
            
            data += send_data
        return data
    
    
    def b_pickaxe_stone(self):
        
        data = ""
        
        if self.material_wood >= self.build_pickaxe_stone[0] and self.material_stone >= self.build_pickaxe_stone[1]:
            self.pickaxe_stone += 1
            self.material_wood -= 30
            self.material_stone -= 20
            data += f"{self.lang[26]} -> + 3 {self.lang[76]}!"
        else:
            send_data += f"{self.lang[23]}\n"
            
            
            if not self.material_wood >= self.build_pickaxe_stone[0]:
                data_wood = self.build_pickaxe_stone[0] - self.material_wood
                send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[77]}"
            if not self.material_stone >= self.build_pickaxe_stone[1]:
                data_stone = self.build_pickaxe_stone[1] - self.material_stone
                send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[76]}"
            
            data += send_data
        return data
    
    
    def b_knife(self):
        
        data = ""
        
        if self.material_wood >= self.build_knife[0] and self.material_stone >= self.build_knife[1]:
            self.knife += 1
            self.material_wood -= 10
            self.material_stone -= 30
            data += f"{self.lang[27]} -> = 30 {self.lang[75]}!"
        else:
            send_data = f"{self.lang[23]}\n"
            
            if not self.material_wood >= self.build_knife[0]:
                data_wood = self.build_knife[0] - self.material_wood
                send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[77]}"
            if not self.material_stone >= self.build_knife[1]:
                data_stone = self.build_knife[1] - self.material_stone
                send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[76]}"
            
            data += send_data
        return data
    
    
    def b_knife_wood(self):
        
        data = ""
        
        if self.material_wood >= self.build_knife_wood:
            self.knife_wood += 1
            self.material_wood -= 30
            data += f"{self.lang[28]}-> = 15 {self.lang[75]}!"
        else:
            data_wood = self.build_knife_wood - self.material_wood
            data += f"{self.lang[23]}\n{self.lang[25]} -> {data_wood} {self.lang[77]}"
        return data
    
    
    def b_shield_upper(self):
        
        data = ""
        
        if self.leather >= self.build_shirtfront_cost[0] and self.rope >= self.build_shirtfront_cost[1]: 
            
            if self.shirtfront > 0 and self.shirtfront < 74 and self.shield_shirtfront == 1:
                data_shield = 75 - self.shirtfront
                self.shield += data_shield
                self.leather -= self.build_shirtfront_cost[0]
                self.rope -= self.build_shirtfront_cost[1]
                data += f"{self.lang[29]}"
                
            elif self.shield_shirtfront == 0:
                self.shield = self.shield + 75
                self.leather -= self.build_shirtfront_cost[0]
                self.rope -= self.build_shirtfront_cost[1]
                self.shield_shirtfront += 1
                data += f"{self.lang[31]} -> + 75 {self.lang[79]}!"
            else:
                data += f"{self.lang[33]}"
                
        else:
            send_data = f"{self.lang[23]}\n"
            
            if not self.leather >= self.build_shirtfront_cost[0]:
                data_wood = self.build_shirtfront_cost[0] - self.leather
                send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[80]}"
            if not self.rope >= self.build_shirtfront_cost[1]:
                data_stone = self.build_shirtfront_cost[1] - self.rope
                send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[83]}"
            
            data += send_data
        return data

    
    def b_shield_lower(self):
        
        data = ""
        
        if self.leather >= self.build_kneepads_cost[0] and self.rope >= self.build_kneepads_cost[1]: 
            if self.kneepads > 0 and self.kneepads < 24 and self.shield_kneepads == 1:
                data_shield = 25 - self.kneepads
                self.shield += data_shield
                self.leather -= self.build_kneepads_cost[0]
                self.rope -= self.build_kneepads_cost[1]
                data += f"{slef.lang[30]}"
                
            elif self.shield_kneepads == 0:
                self.shield += 25
                self.leather = - self.build_kneepads_cost[0]
                self.rope -= self.build_kneepads_cost[1]
                self.shield_kneepads += 1
                data += f"{self.lang[32]} -> + 25 {self.lang[79]}!"
            else:
                data += f"{self.lang[33]}"
            
        else:
            send_data = f"{self.lang[23]}\n"
            
            if not self.leather >= self.build_kneepads_cost[0]:
                data_wood = self.build_kneepads_cost[0] - self.leather
                send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[80]}"
            if not self.rope >= self.build_kneepads_cost[1]:
                data_stone = self.build_kneepads_cost[1] - self.rope
                send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[83]}"
            
            data += send_data
        return data
    
    
    def kill_anm(self):
        
        data = ""
        
        if self.anm_show > 0:
            #if has wooden knife and knife, wooden knife will be used first
            if self.knife_wood > 0:              
                self.kill_anm_life -= self.knife_wood_damage
                #if lower armor and upper armor, only lower armor get damage
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang[35]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
                else:
                    self.healt -= self.kill_anm_damage
                
                self.knife_wood_life -= 20
                
                data += f"{self.lang[36]} -> {self.knife_wood_damage} {self.lang[75]}!\n"
                data += f"{self.lang[37]} -> {self.kill_anm_damage} {self.lang[75]}\n"
                data += f"{self.lang[38]} -> {self.kill_anm_life}\n"
                data += f"{self.lang[39]} -> {self.knife_wood_life}\n"
                
                if self.knife_wood_life == 0:
                    self.knife_wood -= 1
                    data += f"{self.lang[41]}\n"
                    self.knife_wood_life = 100
        
            elif self.knife > 0 and self.knife_wood == 0:
                self.kill_anm_life -= self.knife_damage
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang[35]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
                else:
                    self.healt -= self.kill_anm_damage
                
                self.knife_life -= 10
                
                data += f"{self.lang[36]} -> {self.knife_damage} {self.lang[75]}!\n"
                data += f"{self.lang[37]} -> {self.kill_anm_damage} {self.lang[75]}\n"
                data += f"{self.lang[38]} -> {self.kill_anm_life}\n"
                data += f"{self.lang[39]} -> {self.knife_life}\n"
                
                if self.knife_life == 0:
                    self.knife -= 1
                    data += f"{self.lang[40]}\n"
                    self.knife_life = 100
                
            else:
                
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang[35]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang[34]}\n"
                        self.kneepads = 25
    
                else:
                    
                    self.healt -= self.kill_anm_damage
                
                self.kill_anm_life -= self.puño_damage
                data += f"{self.lang[36]} -> {self.puño_damage} {self.lang[75]}\n"
                data += f"{self.lang[37]} -> {self.kill_anm_damage} {self.lang[75]}\n"
                data += f"{self.lang[38]} -> {self.kill_anm_life}\n"                         
            
            if self.kill_anm_life <= 0:
                #restore animal and get rewards 
                self.anm_show = 0
                self.meat += self.kill_anm_meat
                data += f"\n{self.lang[42]} -> + {self.kill_anm_meat} {self.lang[81]}"
                if self.get_from_anm == 1:
                    self.leather += self.kill_anm_leather
                    self.rope += self.kill_anm_rope
                    data += f"\n{self.lang[42]} -> + {self.kill_anm_leather} {self.lang[80]}\n{self.lang[42]} -> + {self.kill_anm_rope} {self.lang[83]}\n"
                data += f"\n{self.lang[43]}"
                      
        else:
            data += f"{self.lang[44]}"
        if self.healt < 21:
            data += f"\n{self.lang[45]}"
        return data
    
    
    def run(self):
                
        data = ""                
        if self.anm_show > 0:
            self.anm_show = 0
            data += f"{self.lang[46]}"
        else:
            data += f"{self.lang[47]}"
        return data
    
    
    def bonfire(self):
        
        data = ""
        
        if not self.fogata_state:
            if self.material_wood >= 10 and self.material_stone >= 10:
                self.fogata_state = True
                self.material_wood -= 10
                self.material_stone -= 10
                data += f"{self.lang[48]}"
            else:
                send_data = f"{self.lang[23]}"
                if not self.material_wood >= 10:
                    data_wood = 10 - self.material_wood
                    send_data += f"\n{self.lang[25]} -> {data_wood} {self.lang[77]}"
                if not self.material_stone >= 10:
                    data_stone = self.build_pickaxe_stone[1] - self.material_stone
                    send_data += f"\n{self.lang[25]} -> {data_stone} {self.lang[76]}"
                data += send_data                           
        else:
            data += f"{self.lang[49]}"
        return data
            
            
    def cook(self):
        
        data = ""
        
        if self.fogata_state and self.meat > 0:
            self.meat_cooked += self.meat
            self.meat = 0
            data += f"{self.lang[50]}"
        elif self.fogata_state and self.meat == 0:
            data += f"{self.lang[51]}"
        else:
            data += f"{self.lang[52]}"
        return data
    
    
    def eat(self):
        
        data = ""
        
        if self.hungry >= 99 and self.healt > 90:
            data += f"{self.lang[53]}"        	
        else:
            if not self.meat_cooked > 0:
                self.damage_eating = choices(self.probability_eat_damage)[0]
                if self.damage_eating == 1 and self.meat > 0:
                    self.meat -= 1
                    self.healt -= 10
                    data += f"{self.lang[54]}"
                elif not self.damage_eating == 1 and self.meat > 0:
                    #avoid eat more than 100
                    if self.hungry >= 96:
                        self.meat -= 1
                        status_hungry = 100 - self.hungry
                        self.hungry += status_hungry
                        data += f"{self.lang[55]}"
                    else:
                        self.meat -= 1
                        self.hungry += 5
                        data += f"{self.lang[55]}"
                else:
                    data += f"{self.lang[56]}"
            
            else:
                if self.hungry > 80 and self.healt > 90:
                    self.meat_cooked -= 1
                    status_hungry = 100 - self.hungry
                    self.hungry += status_hungry
                    data += f"{self.lang[57]}"
                elif self.hungry >= 96 and self.healt < 91:
                    self.meat_cooked -= 1
                    self.healt += 10
                    data += f"{self.lang[0]} -> + 10\n"
                    data += f"{self.lang[57]}"
                elif self.hungry < 81 and self.healt > 90:
                    self.meat_cooked -= 1
                    self.hungry += 20
                    data += f"{self.lang[57]}"
                else:
                    self.meat_cooked -= 1
                    self.hungry += 20
                    data += f"{self.lang[57]}"
        return data
                                
    
    def find_cabin(self):
                        
        if self.cabaña_show == 1:
            #probability animal appear
            self.probability_anm_cabaña_show = choices([0, 1])[0]
            if self.probability_anm_cabaña_show == 1:
                self.choice_cabaña_in = randint(1, 2)
            else:
                self.choice_cabaña_in = 0
                
            self.anm_cabaña_show = 0
            
            madera_random = randint(1, 15)
            piedra_random = randint(1, 15)
            meat_random = randint(1, 3)
            leather_random = randint(1, 5)
            
            ganzua = choices([0, 1, 0])[0]
            rope = choices([0, 1, 0])[0]
            flechas = choices([0, 0, 1, 0, 0])[0]
            
            if ganzua == 0 and rope == 0 and flechas == 0:
                artefacto = 0
                self.go_cabaña(madera_random, piedra_random, meat_random, leather_random, artefacto, 0)
                #thread = threading.Thread(target=self.go_cabaña, args=(madera_random, piedra_random, meat_random, leather_random, artefacto, 0))
                #thread.start()
            elif ganzua == 1 and rope == 0 and flechas == 0:
                self.go_cabaña(madera_random, piedra_random, meat_random, leather_random, ganzua, 1)
                
                #thread = threading.Thread(target=self.go_cabaña, args=(madera_random, piedra_random, meat_random, leather_random, ganzua, 1))
                #thread.start()
            elif ganzua == 0 and rope == 1 and flechas == 0:
                self.go_cabaña(madera_random, piedra_random, meat_random, leather_random, rope, 2)
                
               #thread = threading.Thread(target=self.go_cabaña, args=(madera_random, piedra_random, meat_random, leather_random, rope, 2))
                #thread.start()
            elif ganzua == 0 and rope == 0 and flechas == 1:
                self.go_cabaña(madera_random, piedra_random, meat_random, leather_random, flechas, 3)
                
                #thread = threading.Thread(target=self.go_cabaña, args=(madera_random, piedra_random, meat_random, leather_random, flechas, 3))
                #thread.start()
            
        else:
            print(f"{self.lang[78]}")
            
         
    def go_cabaña(self, madera, piedra, meat, leather, pieza, nombre):
        
        if nombre == 0:
            nombre_pieza = f"{self.lang[58]}"
        elif nombre == 1:
            nombre_pieza = f"{self.lang[7]}"
        elif nombre == 2:
            nombre_pieza = f"{self.lang[8]}"
        elif nombre == 3:
            nombre_pieza = "Flechas"
            pieza = 20
        
        print(f"\n{self.lang[59]}\n")
    
        test = [] 
        
        while True:
            if self.state_cabaña:
                break
                
            if not 0 in test:
                choice = input("\n1 -> Yes\n2 -> No\n")
                if choice == "1":
                    print(f"\n{self.lang[60]}\n")
                    test.append(0)
                elif choice == "2":
                    print(f"{self.lang[61]}\n")
                    self.cabaña_show = 0
                    break      
                else:
                    print(f"\n{self.lang[62]}\n")
            
            elif 0 in test and 1 not in test:
                if self.ganzua > 0:
                    print(f"\n{self.lang[63]}")
                    self.ganzua -= 1
                    test.append(1)
                else:
                    choice_in = input(f"\n1 -> {self.lang[5]}\n2 -> {self.lang[4]}\n3 -> {self.lang[3]}\n")
                    if choice_in == "1":
                        print(f"\n{self.lang[64]}")
                        if self.choice_cabaña_in == 1:
                            self.anm_cabaña_show = 1
                        test.append(1)
                    elif choice_in == "2":
                        print(f"\n{self.lang[64]}")
                        if self.choice_cabaña_in == 2:
                            self.anm_cabaña_show = 1
                        test.append(1)
                    elif choice_in == "3":
                        print(f"\n{self.lang[65]}")
                        self.cabaña_show = 0
                        break
                    else:
                        print(f"{self.lang[66]}")
                    
            elif 0 in test and 1 in test and 2 not in test:
                print(f"{self.lang[67]}:\n{self.lang[13]} + {madera}\n{self.lang[10]} + {piedra}\n{self.lang[84]} + {meat}\n{self.lang[85]} + {leather}")
                self.material_wood += madera
                self.material_stone += piedra
                self.meat += meat
                self.leather += leather
                
                print()
                print(f"\n{self.lang[68]}\n")
                test.append(2)
            elif 0 in test and 1 in test and 2 in test:
                
                choice_out = input(f"\n1 -> {self.lang[89]}\n2 -> {self.lang[90]}\n3 -> {self.lang[91]}\n4 -> {self.lang[3]}\n")
                
                if choice_out == "1":
                    print(f"{self.lang[69]}\n")
                elif choice_out == "2":
                    print(f"{self.lang[70]}\n")
                elif choice_out == "3":
                    print(f"{self.lang[71]}")
                    print()
                    
                    print(f"{self.lang[67]}: -> {nombre_pieza} + {pieza}\n")
                    if nombre == 1:
                        self.ganzua = self.ganzua + 1
                    elif nombre == 2:
                        self.rope = self.rope + 1
                    elif nombre == 3:
                        self.special_arrows = special_arrows + 20
                    self.cabaña_show = 0
                    break
                elif choice_out == "4":
                    print(f"{self.lang[72]}")
                    self.cabaña_show = 0
                    break
        #call animal stuff if probability
        if self.anm_cabaña_show == 1:
            self.anm_show = 1
            self.set_animal = 2
            self.get_from_anm = choices(self.probability_get_from_anm)[0]
                                            
            self.kill_anm_life = self.animals['life'][self.set_animal]
            self.kill_anm_damage = self.animals['damage'][self.set_animal]
            self.kill_anm_leather = self.animals['leather'][self.set_animal]
            self.kill_anm_meat = self.animals['meat'][self.set_animal]
            self.kill_anm_rope = self.animals['rope'][self.set_animal]
            
            self.healt -= self.kill_anm_damage 
            print(f"{self.lang[73]}\n{self.lang[11]}: 1 -> {self.animals['anm'][self.set_animal]} {self.lang[74]} -{self.kill_anm_damage} {self.lang[75]}!\n")
            
            
    def __str__(self):
        self.output = f"{self.name}\n\n{self.lang[0]}: {self.healt}\n{self.lang[1]}: {self.hungry}\n"
        if self.shield > 0:
            self.output += f"{self.lang[2]}: {self.shield}\n"
        if self.material_wood > 0:
            self.output += f"{self.lang[13]}: {self.material_wood}\n"
        if self.material_stone > 0:
            self.output += f"{self.lang[10]}: {self.material_stone}\n"
        if self.hacha_wood > 0:
            self.output += f"{self.lang[6]}: {self.hacha_wood} {self.lang[86]}/s {self.lang[77]}\n"
        if self.hacha_stone > 0:
            self.output += f"{self.lang[6]}: {self.hacha_stone} {self.lang[86]}/s {self.lang[76]}\n"
        if self.pickaxe_stone > 0:
            self.output += f"{self.lang[6]}: {self.pickaxe_stone} {self.lang[88]}/s {self.lang[76]}\n"
        if self.knife > 0:
            self.output += f"{self.lang[6]}: {self.knife} {self.lang[87]}/s -> {self.lang[92]}: 30\n"
        if self.knife_wood > 0:
            self.output += f"{self.lang[6]}: {self.knife} {self.lang[87]}/s {self.lang[77]} -> {self.lang[92]}: 15\n"
        if self.leather > 0:
            self.output += f"{self.lang[6]}: {self.leather} {self.lang[80]}\n"
        if self.meat > 0:
            self.output += f"{self.lang[6]}: {self.meat} {self.lang[81]}\n"
        if self.meat_cooked > 0:
            self.output += f"{self.lang[6]}: {self.meat_cooked} {self.lang[82]}\n"
        if self.rope > 0:
            self.output += f"{self.lang[6]}: {self.rope} {self.lang[83]}\n"
        if self.ganzua > 0:
            self.output += f"{self.lang[6]}: {self.ganzua} {self.lang[7]}/s\n"
    
        return self.output
