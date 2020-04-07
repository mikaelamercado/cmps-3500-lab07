"""
cmps 3500
lab 07
date: 4/6/20
username: mmercado
name: Ma Mikaela Mercado
description: NearestEnemy.py
"""
import numpy as np

def NearestEnemy(array): 
    array= list(array.split(','))

    strArray = []
    for a in array:
        arr = []
        for b in a:
            if b.isdigit():
                arr.append(int(b))
        strArray.append(arr)
    mini_map = np.array(strArray)
    if 2 not in mini_map:
        return 0
    x_loc = list(zip(*np.where(mini_map == 1)))
    if len(x_loc) != 1:
        raise ValueError("Too many 1's")
    x = x_loc[0]

    e_loc = list(zip(*np.where(mini_map == 2)))

    distance = [sum((abs(x[0] - e[0]),abs(x[1] - e[1]))) for e in e_loc]
    print "output: "
    return min(distance)

print NearestEnemy(raw_input("input:"))
