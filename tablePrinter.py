#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:39:21 2021

@author: williammcintyre
"""

# Table Printer
# Practice Project

tableData = [['apples', 'oranges', 'cherries', 'bananas'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findWidth():
    colWidth = [0] * len(tableData)
    for column in tableData:
        longestString = ''
        for value in column:
            if len(value) > len(longestString):
                longestString = value
        colWidth.append(longestString, len(longestString))
    return colWidth

findWidth()