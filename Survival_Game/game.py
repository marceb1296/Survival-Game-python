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

    def __init__(self, lang):
        
        # Game init
        # self.name = name
        self.healt = 100
        self.hungry = 100
        self.shield = 0
        # lang
        self.lang_game = lang.get("game")
        self.lang_materials = lang.get("materials")
        self.lang_animals = lang.get("animals")
        self.lang_cottage = lang.get("cottage")
        self.lang_tools = lang.get("tools")
        self.lang_not_enough = lang.get("not_enough")
        self.lang_tools_state = lang.get("tools_state")
        # Materials
        self.material_wood = 0
        self.material_stone = 0
        # axe
        self.hacha_wood = 0
        self.hacha_wood_life = 100
        self.build_hacha_wood = 30 # wood
        # axe stone
        self.hacha_stone = 0
        self.hacha_stone_life = 100
        self.build_hacha_stone = [30, 15] # wood/stone
        # pickaxe only stone
        self.pickaxe_stone = 0
        self.pickaxe_stone_life = 100
        self.build_pickaxe_stone = [30, 20] # wood/stone
        # knife
        self.knife = 0
        self.knife_life = 100
        self.knife_damage = 30
        self.build_knife = [10, 30] # wood/stone
        # knife wood
        self.knife_wood = 0
        self.knife_wood_life = 100
        self.knife_wood_damage = 10
        self.build_knife_wood = 30 #wood
        # build materials 
        self.leather = 0
        self.meat = 0
        self.meat_cooked = 0
        self.rope = 0
        self.picklock = 0
        # upper armor
        self.shirtfront = 75
        self.shield_shirtfront = 0
        self.build_shirtfront_cost = [50, 20] # leather/rope 
        # lower armor
        self.kneepads = 25
        self.shield_kneepads = 0
        self.build_kneepads_cost = [25, 10] #leather/rope
        # environment
        self.times_ent = 0
        # animals
        self.anm_show = 0
        self.animals = {
            "life": [120, 80, 90], 
            "damage": [3, 5, 10], 
            "leather": [10, 8, 5], 
            "meat": [5, 3, 1], 
            "rope": [5, 3, 2]
        } 
        # animals rewards
        self.kill_anm_life = 0
        self.kill_anm_damage = 0
        self.kill_anm_leather = 0
        self.kill_anm_meat = 0
        self.kill_anm_rope = 0
        
        self.animal_choice = [0, 1, 2]
        # Not implemented
        self.archer = 0
        self.build_archer = [50, 10, 30] #wood/stone/rope
                
        self.special_arrows = 0
        self.special_arrows_damage = 80
        # fist damage
        self.fist_damage = 5
        # tree/wood
        self.tree = 0
        self.wood = 5
        # rock/stone
        self.rock = 0
        self.stone = 3
        # game state
        self.state = False
        # bonfire
        self.fogata_state = False
        # cottage
        self.cottage_show = 0
        self.state_cottage = False
        # Probabilitys
        self.probability_get_from_anm = [0, 1]
        self.probability_eat_damage = [0, 1, 0]
        self.probability_anm = [0, 1, 0, 0, 0]
        self.probability_cabaña = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.probability_tree = [0, 0, 1, 0, 0, 2, 0, 0, 1, 0]
        self.probability_stone = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    
    
    def enviroment(self):
        
        if not self.state:
            
            self.times_ent += 1

            # Make false, avoid reuse
            self.fogata_state = False
            
            return_data = "\n"
            
            self.tree = choices(self.probability_tree)[0]
            self.rock = choices(self.probability_stone)[0]
            self.anm_show = choices(self.probability_anm)[0]
            self.cottage_show = choices(self.probability_cabaña)[0]
            
            return_data += f"{self.lang_materials[0]}: {self.tree}\n{self.lang_materials[1]}: {self.rock}\n"
            
            if self.anm_show == 1:
                self.set_animal = choices(self.animal_choice)[0]
                self.get_from_anm = choices(self.probability_get_from_anm)[0]
                                            
                self.kill_anm_life = self.animals['life'][self.set_animal]
                self.kill_anm_damage = self.animals['damage'][self.set_animal]
                self.kill_anm_leather = self.animals['leather'][self.set_animal]
                self.kill_anm_meat = self.animals['meat'][self.set_animal]
                self.kill_anm_rope = self.animals['rope'][self.set_animal]
                
                return_data += f"{self.lang_animals[0]}: {self.anm_show} -> {self.lang_animals[1][self.set_animal]}\n"
           
            if self.cottage_show == 1:
                return_data += f"{self.lang_cottage[0]}\n"
                
            return return_data
        
    
    def tree_cut(self):
        
        data = "\n"
        
        if self.tree > 0:
            
            if self.hacha_wood > 0:
                self.material_wood += 3 + (self.wood * self.tree)
                data += f"{self.lang_materials[2]} + {(self.wood * self.tree)} -> + 3\n"
                self.hacha_wood_life -= 20
                data += f"{self.lang_tools_state[0]} -> {self.hacha_wood_life}\n"
                if self.hacha_wood_life <= 0:
                    self.hacha_wood -= 1
                    data += f"{self.lang_tools_state[1]}\n"
                    self.hacha_wood_life = 100
                self.tree = 0
            elif self.hacha_stone > 0 and self.hacha_wood == 0:
                self.material_wood += 5 + (self.wood * self.tree)
                data += f"{self.lang_materials[2]} + {(self.wood * self.tree)} -> + 5\n"
                self.hacha_stone_life -= 10
                data += f"{self.lang_tools_state[2]} -> {self.hacha_stone_life}\n"
                if self.hacha_stone_life <= 0:
                    self.hacha_stone -= 1
                    data += f"{self.lang_tools_state[3]}\n"
                    self.hacha_stone_life = 100
                self.tree = 0
            else:
                self.material_wood += (self.wood * self.tree)
                data += f"{self.lang_materials[2]} + {(self.wood * self.tree)}\n"
                self.tree = 0                
          
        else:
            data += f"{self.lang_not_enough[0]}\n"
        
        return data
    
    
    def stone_chop(self):
        
        data = "\n"
        
        if self.rock > 0:
            if self.pickaxe_stone > 0:
                self.material_stone += 3 + (self.stone * self.rock)
                data += f"{self.lang_materials[3]} + 3 -> + 3\n"
                self.pickaxe_stone_life -= 10
                data += f"{self.lang_tools_state[4]} -> {self.pickaxe_stone_life}\n"
                if self.pickaxe_stone_life <= 0:
                    self.pickaxe_stone -= 1
                    data += f"{self.lang_tools_state[5]}\n"
                    self.pickaxe_stone_life = 100
                self.rock = 0
            else:
                self.material_stone += (self.stone * self.rock)
                data += f"{self.lang_materials[3]} + 3\n"
                self.rock = 0
        else:
            data += f"{self.lang_not_enough[1]}\n"
        return data
    
    # b_ instead of build_ cuz already used 
    def b_axe_wood(self):
        
        data = "\n"
        
        if self.material_wood >= self.build_hacha_wood:
            self.hacha_wood += 1
            self.material_wood -= 30
            data += f"{self.lang_tools_state[6]} -> + 3!\n"
        else:
            data_wood = self.build_hacha_wood - self.material_wood
            
            data += f"{self.lang_not_enough[2]}\n{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}\n"
        return data
    
    
    def b_axe_stone(self):
        
        data = "\n"
        
        if self.material_wood >= self.build_hacha_stone[0] and self.material_stone >= self.build_hacha_stone[1]:
            self.hacha_stone += 1
            self.material_wood -= 30
            self.material_stone -= 15
            data += f"{self.lang_tools_state[7]} -> + 5!\n"
        else:
            send_data = ""
            send_data += f"{self.lang_not_enough[2]}\n"
            
            
            if not self.material_wood >= self.build_hacha_stone[0]:
                data_wood = self.build_hacha_stone[0] - self.material_wood
                send_data += f"\n{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}"
            if not self.material_stone >= self.build_hacha_stone[1]:
                data_stone = self.build_hacha_stone[1] - self.material_stone
                send_data += f"\n{self.lang_game[12]} -> {data_stone} {self.lang_not_enough[4]}\n"
            
            data += send_data
        return data
    
    
    def b_pickaxe_stone(self):
        
        data = "\n"
        
        if self.material_wood >= self.build_pickaxe_stone[0] and self.material_stone >= self.build_pickaxe_stone[1]:
            self.pickaxe_stone += 1
            self.material_wood -= 30
            self.material_stone -= 20
            data += f"{self.lang_tools_state[8]} -> + 3!"
        else:
            send_data = ""
            send_data += f"{self.lang_not_enough[2]}\n"
            
            
            if not self.material_wood >= self.build_pickaxe_stone[0]:
                data_wood = self.build_pickaxe_stone[0] - self.material_wood
                send_data += f"\n{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}"
            if not self.material_stone >= self.build_pickaxe_stone[1]:
                data_stone = self.build_pickaxe_stone[1] - self.material_stone
                send_data += f"\n{self.lang_game[12]} -> {data_stone} {self.lang_not_enough[4]}\n"
            
            data += send_data
        return data
    
    
    def b_knife(self):
        
        data = "\n"
        
        if self.material_wood >= self.build_knife[0] and self.material_stone >= self.build_knife[1]:
            self.knife += 1
            self.material_wood -= 10
            self.material_stone -= 30
            data += f"{self.lang_tools_state[9]} -> = 30 {self.lang_game[13]}!\n"
        else:
            send_data = ""
            send_data = f"{self.lang_not_enough[2]}\n"
            
            if not self.material_wood >= self.build_knife[0]:
                data_wood = self.build_knife[0] - self.material_wood
                send_data += f"\n{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}"
            if not self.material_stone >= self.build_knife[1]:
                data_stone = self.build_knife[1] - self.material_stone
                send_data += f"\n{self.lang_game[12]} -> {data_stone} {self.lang_not_enough[4]}\n"
            
            data += send_data
        return data
    
    
    def b_knife_wood(self):
        
        data = "\n"
        
        if self.material_wood >= self.build_knife_wood:
            self.knife_wood += 1
            self.material_wood -= 30
            data += f"{self.lang_tools_state[10]} -> = 15 {self.lang_game[13]}!\n"
        else:
            data_wood = self.build_knife_wood - self.material_wood
            data += f"{self.lang_not_enough[2]}\n{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}\n"
        return data
    
    
    def b_shield_upper(self):
        
        data = "\n"
        
        if self.leather >= self.build_shirtfront_cost[0] and self.rope >= self.build_shirtfront_cost[1]: 
            
            if self.shirtfront > 0 and self.shirtfront < 74 and self.shield_shirtfront == 1:
                data_shield = 75 - self.shirtfront
                self.shield += data_shield
                self.leather -= self.build_shirtfront_cost[0]
                self.rope -= self.build_shirtfront_cost[1]
                data += f"{self.lang_tools_state[11]}"
                
            elif self.shield_shirtfront == 0:
                self.shield = self.shield + 75
                self.leather -= self.build_shirtfront_cost[0]
                self.rope -= self.build_shirtfront_cost[1]
                self.shield_shirtfront += 1
                data += f"{self.lang_tools_state[13]} -> + 75 {self.lang_game[14]}!"
            else:
                data += f"{self.lang_tools_state[15]}"
                
        else:
            send_data = ""
            send_data = f"{self.lang_not_enough[2]}\n"
            
            if not self.leather >= self.build_shirtfront_cost[0]:
                data_wood = self.build_shirtfront_cost[0] - self.leather
                send_data += f"\n{self.lang_game[12]} -> {data_wood} {self.lang_game[8]}"
            if not self.rope >= self.build_shirtfront_cost[1]:
                data_rope = self.build_shirtfront_cost[1] - self.rope
                send_data += f"\n{self.lang_game[12]} -> {data_rope} {self.lang_game[11]}\n"
            
            data += send_data
        return data

    
    def b_shield_lower(self):
        
        data = "\n"
        
        if self.leather >= self.build_kneepads_cost[0] and self.rope >= self.build_kneepads_cost[1]: 
            if self.kneepads > 0 and self.kneepads < 24 and self.shield_kneepads == 1:
                data_shield = 25 - self.kneepads
                self.shield += data_shield
                self.leather -= self.build_kneepads_cost[0]
                self.rope -= self.build_kneepads_cost[1]
                data += f"{self.lang_tools_state[12]}"
                
            elif self.shield_kneepads == 0:
                self.shield += 25
                self.leather = - self.build_kneepads_cost[0]
                self.rope -= self.build_kneepads_cost[1]
                self.shield_kneepads += 1
                data += f"{self.lang_tools_state[14]} -> + 25 {self.lang_game[14]}!"
            else:
                data += f"{self.lang_tools_state[15]}"
            
        else:
            send_data = ""
            send_data = f"{self.lang_not_enough[2]}\n"
            
            if not self.leather >= self.build_kneepads_cost[0]:
                data_wood = self.build_kneepads_cost[0] - self.leather
                send_data += f"\n{self.lang_game[12]} -> {data_wood} {self.lang_game[8]}"
            if not self.rope >= self.build_kneepads_cost[1]:
                data_stone = self.build_kneepads_cost[1] - self.rope
                send_data += f"\n{self.lang_game[12]} -> {data_stone} {self.lang_game[11]}\n"
            
            data += send_data
        return data
    
    
    def kill_anm(self):
        
        data = "\n"
        
        if self.anm_show > 0:
            # if has wooden knife and knife, wooden knife will be used first
            if self.knife_wood > 0:              
                self.kill_anm_life -= self.knife_wood_damage
                # if lower armor and upper armor, only lower armor get damage
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang_tools_state[17]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
                else:
                    self.healt -= self.kill_anm_damage
                
                self.knife_wood_life -= 20
                
                data += f"{self.lang_game[15]} -> {self.knife_wood_damage} {self.lang_game[13]}!\n"
                data += f"{self.lang_game[16]} -> {self.kill_anm_damage} {self.lang_game[13]}\n"
                data += f"{self.lang_game[17]} -> {self.kill_anm_life}\n"
                data += f"{self.lang_tools_state[18]} -> {self.knife_wood_life}\n"
                
                if self.knife_wood_life == 0:
                    self.knife_wood -= 1
                    data += f"{self.lang_tools_state[20]}\n"
                    self.knife_wood_life = 100
        
            elif self.knife > 0 and self.knife_wood == 0:
                self.kill_anm_life -= self.knife_damage
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang_tools_state[17]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
                else:
                    self.healt -= self.kill_anm_damage
                
                self.knife_life -= 10
                
                data += f"{self.lang_game[15]} -> {self.knife_damage} {self.lang_game[13]}!\n"
                data += f"{self.lang_game[16]} -> {self.kill_anm_damage} {self.lang_game[13]}\n"
                data += f"{self.lang_game[17]} -> {self.kill_anm_life}\n"
                data += f"{self.lang_tools_state[18]} -> {self.knife_life}\n"
                
                if self.knife_life == 0:
                    self.knife -= 1
                    data += f"{self.lang_tools_state[19]}\n"
                    self.knife_life = 100
                
            else:
                
                if self.shield_shirtfront == 1 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
                elif self.shield_shirtfront == 1 and self.shield_kneepads == 0:
                    self.shirtfront -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.shirtfront <= 0:
                        self.shield_shirtfront -= 1
                        data += f"{self.lang_tools_state[17]}\n"
                        self.shirtfront = 75
                elif self.shield_shirtfront == 0 and self.shield_kneepads == 1:
                    self.kneepads -= self.kill_anm_damage
                    self.shield -= self.kill_anm_damage
                    if self.kneepads <= 0:
                        self.shield_kneepads -= 1
                        data += f"{self.lang_tools_state[16]}\n"
                        self.kneepads = 25
    
                else:
                    
                    self.healt -= self.kill_anm_damage
                
                self.kill_anm_life -= self.fist_damage
                data += f"{self.lang_game[15]} -> {self.fist_damage} {self.lang_game[13]}\n"
                data += f"{self.lang_game[16]} -> {self.kill_anm_damage} {self.lang_game[13]}\n"
                data += f"{self.lang_game[17]} -> {self.kill_anm_life}\n"                         
            
            if self.kill_anm_life <= 0:
                #restore animal and get rewards 
                self.anm_show = 0
                self.meat += self.kill_anm_meat
                data += f"\n{self.lang_game[18]} -> + {self.kill_anm_meat} {self.lang_game[9]}"
                if self.get_from_anm == 1:
                    self.leather += self.kill_anm_leather
                    self.rope += self.kill_anm_rope
                    data += f"\n{self.lang_game[18]} -> + {self.kill_anm_leather} {self.lang_game[8]}\n{self.lang_game[18]} -> + {self.kill_anm_rope} {self.lang_game[11]}\n"
                data += f"\n{self.lang_animals[2]}\n"
                      
        else:
            data += f"{self.lang_animals[3]}\n"
        if self.healt < 21:
            data += f"{self.lang_animals[4]}\n"
        return data
    
    
    def run(self):
                
        data = "\n"                
        if self.anm_show > 0:
            self.anm_show = 0
            data += f"{self.lang_animals[5]}\n"
        else:
            data += f"{self.lang_animals[6]}\n"
        return data
    
    
    def bonfire(self):
        
        data = "\n"
        
        if not self.fogata_state:
            if self.material_wood >= 10 and self.material_stone >= 10:
                self.fogata_state = True
                self.material_wood -= 10
                self.material_stone -= 10
                data += f"{self.lang_game[19]}\n"
            else:
                send_data = ""
                send_data = f"{self.lang_not_enough[2]}\n"
                if not self.material_wood >= 10:
                    data_wood = 10 - self.material_wood
                    send_data += f"{self.lang_game[12]} -> {data_wood} {self.lang_not_enough[3]}\n"
                if not self.material_stone >= 10:
                    data_stone = self.build_pickaxe_stone[1] - self.material_stone
                    send_data += f"{self.lang_game[12]} -> {data_stone} {self.lang_not_enough[4]}\n"
                data += send_data                           
        else:
            data += f"{self.lang_game[20]}\n"
        return data
            
            
    def cook(self):
        
        data = "\n"
        
        if self.fogata_state and self.meat > 0:
            self.meat_cooked += self.meat
            self.meat = 0
            data += f"{self.lang_game[21]}\n"
        elif self.fogata_state and self.meat == 0:
            data += f"{self.lang_game[22]}\n"
        else:
            data += f"{self.lang_game[23]}\n"
        return data
    
    
    def eat(self):
        
        data = "\n"
        
        if self.hungry >= 99 and self.healt > 90:
            data += f"{self.lang_game[24]}\n"        	
        else:
            if not self.meat_cooked > 0:
                self.damage_eating = choices(self.probability_eat_damage)[0]
                if self.damage_eating == 1 and self.meat > 0:
                    self.meat -= 1
                    self.healt -= 10
                    data += f"{self.lang_game[25]}"
                elif not self.damage_eating == 1 and self.meat > 0:
                    #avoid eat more than 100
                    if self.hungry >= 96:
                        self.meat -= 1
                        status_hungry = 100 - self.hungry
                        self.hungry += status_hungry
                        data += f"{self.lang_game[26]}\n"
                    else:
                        self.meat -= 1
                        self.hungry += 5
                        data += f"{self.lang_game[26]}\n"
                else:
                    data += f"{self.lang_game[27]}\n"
            
            else:
                if self.hungry > 80 and self.healt > 90:
                    self.meat_cooked -= 1
                    status_hungry = 100 - self.hungry
                    self.hungry += status_hungry
                    data += f"{self.lang_game[28]}\n"
                elif self.hungry >= 96 and self.healt < 91:
                    self.meat_cooked -= 1
                    self.healt += 10
                    data += f"{self.lang_game[0]} -> + 10\n"
                    data += f"{self.lang_game[28]}\n"
                elif self.hungry < 81 and self.healt > 90:
                    self.meat_cooked -= 1
                    self.hungry += 20
                    data += f"{self.lang_game[28]}\n"
                else:
                    self.meat_cooked -= 1
                    self.hungry += 20
                    data += f"{self.lang_game[28]}\n"
        return data
                                
    
    def find_cabin(self):
                        
        if self.cottage_show == 1:
            # animal appear probability 
            self.probability_anm_cabaña_show = choices([0, 1])[0]
            if self.probability_anm_cabaña_show == 1:
                self.choice_cabaña_in = randint(1, 2)
            else:
                self.choice_cabaña_in = 0
                
            self.anm_cabaña_show = 0
            
            random_wood = randint(1, 15)
            random_stone = randint(1, 15)
            random_meat = randint(1, 3)
            random_leather = randint(1, 5)
            
            picklock = choices([0, 1, 0])[0]
            rope = choices([0, 1, 0])[0]
            arrows = choices([0, 0, 1, 0, 0])[0]

            part = {}

            if picklock > 0:
                part[self.lang_materials[8]] = picklock
            if rope > 0:
                part[self.lang_materials[4]] = rope
            if arrows > 0:
                part[self.lang_materials[9]] = arrows

            self.go_cabaña(random_wood, random_stone, random_meat, random_leather, part)
            """
            if picklock == 0 and rope == 0 and arrows == 0:
                artefacto = 0
            elif picklock == 1 and rope == 0 and arrows == 0:
                self.go_cabaña(random_wood, random_stone, random_meat, random_leather, picklock, 1)
            elif picklock == 0 and rope == 1 and arrows == 0:
                self.go_cabaña(random_wood, random_stone, random_meat, random_leather, rope, 2)
            elif picklock == 0 and rope == 0 and arrows == 1:
                self.go_cabaña(random_wood, random_stone, random_meat, random_leather, arrows, 3)
            """
            
        else:
            print(f"\n{self.lang_game[29]}\n")
            
         
    def go_cabaña(self, wood, stone, meat, leather, part):
        
        if not part:
            part_name = f"{self.lang_game[30]}"
        else:
            part_name = "\n".join([" -> ".join([str(el) for el in i]) for i in part.items()])
        
        print(f"\n{self.lang_game[31]}\n")
    
        test = [] 
        
        while True:
            if self.state_cottage:
                break
                
            if not 0 in test:
                choice = input(f"\n1 -> {self.lang_cottage[15]}\n2 -> {self.lang_cottage[16]}\n: ")
                if choice == "1":
                    print(f"\n{self.lang_cottage[1]}\n")
                    test.append(0)
                elif choice == "2":
                    print(f"\n{self.lang_cottage[2]}\n")
                    self.cottage_show = 0
                    break      
                else:
                    print(f"\n{self.lang_cottage[3]}\n")
            
            elif 0 in test and 1 not in test:
                if self.picklock > 0:
                    print(f"\n{self.lang_cottage[4]}\n")
                    self.picklock -= 1
                    test.append(1)
                else:
                    choice_in = input(f"\n1 -> {self.lang_game[5]}\n2 -> {self.lang_game[4]}\n3 -> {self.lang_game[3]}\n: ")
                    if choice_in == "1":
                        print(f"\n{self.lang_cottage[5]}")
                        if self.choice_cabaña_in == 1:
                            self.anm_cabaña_show = 1
                        test.append(1)
                    elif choice_in == "2":
                        print(f"\n{self.lang_cottage[5]}")
                        if self.choice_cabaña_in == 2:
                            self.anm_cabaña_show = 1
                        test.append(1)
                    elif choice_in == "3":
                        print(f"\n{self.lang_cottage[6]}")
                        self.cottage_show = 0
                        break
                    else:
                        print(f"\n{self.lang_cottage[7]}")
                    
            elif 0 in test and 1 in test and 2 not in test:
                print(f"\n{self.lang_cottage[8]}:\n{self.lang_materials[2]} + {wood}\n{self.lang_materials[3]} + {stone}\n{self.lang_materials[5]} + {meat}\n{self.lang_materials[7]} + {leather}\n")
                self.material_wood += wood
                self.material_stone += stone
                self.meat += meat
                self.leather += leather
                
                print()
                print(f"\n{self.lang_cottage[9]}\n")
                test.append(2)
            elif 0 in test and 1 in test and 2 in test:
                
                choice_out = input(f"\n1 -> {self.lang_game[32]}\n2 -> {self.lang_game[33]}\n3 -> {self.lang_game[34]}\n4 -> {self.lang_game[3]}\n: ")
                
                if choice_out == "1":
                    print(f"\n{self.lang_cottage[10]}\n")
                elif choice_out == "2":
                    print(f"\n{self.lang_cottage[11]}\n")
                elif choice_out == "3":
                    print(f"\n{self.lang_cottage[12]}\n")
                    print()
                    
                    print(f"{self.lang_cottage[8]}: \n{part_name}\n")

                    for i in part.items():
                        item, amount = i

                        if item == self.lang_materials[8]:
                            self.picklock += amount
                        elif item == self.lang_materials[4]:
                            self.rope += amount
                        elif item == self.lang_materials[9]:
                            self.special_arrows += 20

                    self.cottage_show = 0
                    break
                elif choice_out == "4":
                    print(f"\n{self.lang_cottage[13]}\n")
                    self.cottage_show = 0
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
            print(f"\n{self.lang_cottage[14]}\n{self.lang_animals[0]}: 1 -> {self.lang_animals[1][self.set_animal]}, {self.lang_animals[7]} {self.kill_anm_damage} {self.lang_game[13]}!\n")
            
            
    def __str__(self):
        self.output = f"{self.name}\n\n{self.lang_game[0]}: {self.healt}\n{self.lang_game[1]}: {self.hungry}\n"
        if self.shield > 0:
            self.output += f"{self.lang_game[3]}: {self.shield}\n"
        if self.material_wood > 0:
            self.output += f"{self.lang_materials[2]}: {self.material_wood}\n"
        if self.material_stone > 0:
            self.output += f"{self.lang_materials[3]}: {self.material_stone}\n"
        if self.hacha_wood > 0:
            self.output += f"{self.lang_game[6]}: {self.hacha_wood} {self.lang_tools[0]}/s\n"
        if self.hacha_stone > 0:
            self.output += f"{self.lang_game[6]}: {self.hacha_stone} {self.lang_tools[1]}/s\n"
        if self.pickaxe_stone > 0:
            self.output += f"{self.lang_game[6]}: {self.pickaxe_stone} {self.lang_tools[2]}/s\n"
        if self.knife > 0:
            self.output += f"{self.lang_game[6]}: {self.knife} {self.lang_tools[3]}/s -> {self.lang_game[7]}: {self.knife_damage}\n"
        if self.knife_wood > 0:
            self.output += f"{self.lang_game[6]}: {self.knife_wood} {self.lang_tools[4]}/s -> {self.lang_game[7]}: {self.knife_wood_damage}\n"
        if self.leather > 0:
            self.output += f"{self.lang_game[6]}: {self.leather} {self.lang_game[8]}\n"
        if self.meat > 0:
            self.output += f"{self.lang_game[6]}: {self.meat} {self.lang_game[9]}\n"
        if self.meat_cooked > 0:
            self.output += f"{self.lang_game[6]}: {self.meat_cooked} {self.lang_game[10]}\n"
        if self.rope > 0:
            self.output += f"{self.lang_game[6]}: {self.rope} {self.lang_game[11]}\n"
        if self.picklock > 0:
            self.output += f"{self.lang_game[6]}: {self.picklock} {self.lang_materials[8]}/s\n"
    
        return self.output
