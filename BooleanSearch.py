#!/usr/bin/python3

import re, os

class BooleanSearch():

    def __init__(self, wordList = False, query = False):
        self.wordList = wordList
        self.query = query


    def disjonctiveQuery(self):
        return re.split(r'\bou\b', self.query)


    def conjonctiveQuery(self):
        disjonctiveQ = self.disjonctiveQuery()
        return [re.split(r'\bet\b', disQuery) for disQuery in disjonctiveQ]


    def creatBoolQuery(self):
        newList = []
        conjonctiveQuery = self.conjonctiveQuery()
        # print(conjonctiveQuery)

        for listWord in conjonctiveQuery:
            subNewList = []
            for word in listWord:
                if(word.strip() not in self.wordList or (word.strip().startswith('non') and word.strip()[3:] not in self.wordList)):
                    decision = 0
                elif word.strip() in self.wordList:
                    decision = 1
                subNewList.append(decision)
            newList.append(subNewList)
        # print(newList)
        return newList

    
    def search(self):
        finalList = []
        newList = self.creatBoolQuery()

        for subList in newList:
            finalList.append(0) if 0 in subList else finalList.append(1)
        # print(finalList)
        if 1 in finalList:
            return True
        return False 
