#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, name):
        curr = self.root
        
        for char in name:
            if char not in curr.children:
                curr.children [char] = TrieNode()
            curr = curr.children[char]
            curr.cnt += 1
        
    def find(self, name):
        curr = self.root
        for char in name: 
            if char not in curr.children:
                return 0 #Word was not found
            curr = curr.children[char]
        return curr.cnt #Return True if the word exists
        
def contacts(queries):
    obj = Trie()
    res = [] #List to store results
    
    for op, val in queries:
        if op == "add":
            obj.add(val)
        elif op == "find":
            res.append(obj.find(val))
    return res
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
