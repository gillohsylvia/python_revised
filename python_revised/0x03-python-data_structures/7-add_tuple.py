#!/usr/bin/python3
"""
* given two tuples
* 
"""
def add_tuple(tuple_a=(), tuple_b=()):
    tup_0 = (0,0)
    tup_1 = (tuple_a + tup_0)
    tup_2 = (tuple_b + tup_0)
    sum = (tup_1[0]+tup_2[0], tup_1[1]+tup_2[1])
    return(sum)
