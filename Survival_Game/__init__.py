#!/usr/bin/env python
# coding: utf-8

from .game import Game
import threading
import time


class Start(Game):
    
    def __init__(self, name, lang):
        self.name = name
        super().__init__(lang)
            
    def start_game(self):
        
        thread = threading.Thread(target=self.timing)
        thread.start()
        
    def timing(self):
        while True:
            # Update every 5 sec
            time.sleep(5)
            if self.state:
                print(f"\n{self.lang_game[35]}\n")
                break
            if self.hungry >= 90 and self.healt < 99:
                self.healt += 2
            if self.hungry <= 0 and self.healt > 0:
                self.hungry = 0
                self.healt -= 1
            if self.healt <= 0:
                print("\nGame Over\n")
                break
            if self.hungry > 0:
                self.hungry -= 1

