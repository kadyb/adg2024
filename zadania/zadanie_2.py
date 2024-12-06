#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:39:13 2024

@author: michalbaczkiewicz
"""


# Napisz funkcję, która zamienia kilogramy (kg) na funty (lb) oraz na odwrót.

def kilogramatorofuntator(x, y):
    if y == 'kg_lb':
        return x * 2.20462  
    elif y == 'lb_kg':
        return x / 2.20462  
    else: print('cos nie tak')

kilogramatorofuntator(100, 'kg_lb')
kilogramatorofuntator(100, 'lb_kg')
