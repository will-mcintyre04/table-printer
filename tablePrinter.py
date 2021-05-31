#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:39:21 2021

@author: williammcintyre
"""

# Table Printer
# Practice Project

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # create a new list of 3 "0" values: one for each list in tableData
    colWidths = [0] * len(table)
    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for y in range(0, len(table)):
        for x in table[y]:
            if colWidths[y] < len(x): # If the current largest width is less than that of the new item
                colWidths[y] = len(x)

    # "rotate" and print the list of lists
    for x in range(0, len(table[0])) :
        for y in range(0, len(table)) :
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()
        x += 1

printTable(tableData)
        
                
                