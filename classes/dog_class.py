#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:31:21 2022

@author: victor
"""

class Dog():
    """Represent a dog."""
    
    def __init__(self, name):
        """Initialize dog object"""
        self.name = name
        
    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")
        
my_dog = Dog('Peso')
    
print(my_dog.name + " is sitting.")
my_dog.sit()