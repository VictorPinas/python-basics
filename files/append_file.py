#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:55:22 2022

@author: victor
"""

filename = 'journal.txt'
with open(filename, 'a') as file_object:
    file_object.write("\nI love making games.")