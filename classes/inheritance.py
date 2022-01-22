#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:36:34 2022

@author: victor
"""

class SARDog(Dog):
    """Represent a search dog."""
    
    def __init__(self, name):
        """Initilize the sar dog."""
        super().__init__(name)
        
    def search(self):
        """Simulate search."""
        print(self.name + " is searching.")
        
my_dog = SARDog("Willie")

print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()