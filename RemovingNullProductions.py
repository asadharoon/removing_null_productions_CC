# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:02:27 2020

@author: AsadHaroon
"""
# Considered # as epsilon so please write epsilon as # in file.

def printGrammar():
    file=open("D:\\CFG.txt")
    for line in file.readlines():
        print(line)
def isEpsilon(s):
    if s=='#':
        return True
    return False
def isTerminal(s):
    if s>='a' and s<='z':
        return True
    return False
def readCFG():
    file=open("D:\\CFG.txt")
    nonterminals=[]
    for line in file:
        s=line.split('->')
        rules=s[1].split('|')
        for i in rules:
            if i.endswith('\n'):
                i=i.split('\n')[0]
            nonterminals.append([s[0],i])
    return nonterminals

def main():
    li=readCFG()
    dictlist=dict()
    for i in li:
        if not i in dictlist.items():
            dictlist.setdefault(i[0], [])
    for j in li:
        dictlist[j[0]].append(j[1])
    for i in range(len(li)-1,-1,-1):
        if isEpsilon(li[i][1]):
            x=li[i][0]
            for j in li:
                if x in j[1]:
                    e=j[1]
                    e=e.replace(x,"")
                    dictlist[j[0]].append(e)
                    a=dictlist[j[0]]
                    if '#' in a:
                        a.remove('#')
                        dictlist.update({j[0]:a})
    
    return dictlist
if __name__=='__main__':
    printGrammar()
    a=main()
    print("\nAfter Null Productions Removal:\n",a)
    
