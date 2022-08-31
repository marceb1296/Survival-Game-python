#!/usr/bin/env python
# coding: utf-8

from .game import Game
import threading
import time


class Start(Game):
    
    def __init__(self, name, lang):
        self.name = name
        self.lang = lang
        super().__init__()
            
    def start_game(self):
        #call Game and starting
        #Game.__init__(self, self.name, self.lang) 
        #call in thread
        thread = threading.Thread(target=self.timing)
        thread.start()
        
    def timing(self):
        while True:
            # Update every sec
            time.sleep(10)
            if self.state:
                print("Game finished")
                break
            if self.hungry >= 90 and self.healt < 99:
                self.healt += 2
            if self.hungry <= 0 and self.healt > 0:
                self.hungry = 0
                self.healt -= 1
            if self.healt <= 0:
                print("Game Over")
                break
            if self.hungry > 0:
                self.hungry -= 1

