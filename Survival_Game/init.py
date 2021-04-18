#!/usr/bin/env python
# coding: utf-8

# In[7]:


from lang import Lang
from game import Game
import threading
import time


class Start(Lang, Game):
    
    def __init__(self, name, lang="en"):
        self.name = name
        self.lang = self.en()
        #set spanish in case
        if lang == "es":
            self.lang = self.es()
            
    def starting_game(self):
        #call Game and starting
        Game.__init__(self, self.name, self.lang) 
        #call in thread
        thread = threading.Thread(target=self.timing)
        thread.start()
        
    def timing(self):
        while True:
            #every 10 sec update, you can chage it and play with it
            time.sleep(10)
            if self.state:
                print("Game finished")
                break
            if self.hungry >= 90 and self.healt < 99:
                self.healt += 2
            if self.hungry <= 0 and self.healt > 0:
                self.hungry = 0
                self.healt = self.healt - 1
            if self.healt <= 0:
                print("Game Over")
                break
            if self.hungry > 0:
                self.hungry = self.hungry - 1

