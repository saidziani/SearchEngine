#!/usr/bin/python3

import re, os

class BooleanSearch():

    def __init__(self, wordList = False, query = False):
        self.wordList = wordList
        self.query = query

    def createQueryToEval(self):
        query = re.sub(r'\(', ' ( ', self.query)
        query = re.sub(r'\)', ' ) ', query)
        return query.split()


    def creatBoolQuery(self):
        querySplited = self.createQueryToEval()
        newQuery = ""
        exist = []

        for item in querySplited:
            if item not in ['et', 'ou'] and (item in self.wordList or item[3:] in self.wordList):
                exist.append(item[3:]) if item.startswith('non') else exist.append(item)

        for item in querySplited:
            if item in set(exist) or item[3:] in set(exist):
                if item.startswith('non'):
                    decision = " 0 "
                else:
                    decision = " 1 "
                newQuery += decision
            elif item == '(':
                newQuery += ' ( '
            elif item == ')':
                newQuery += ' ) '
            elif item == 'et':
                newQuery += ' and '
            elif item == 'ou':
                newQuery += ' or '
            else:
                newQuery += " 0 "
        return newQuery


if __name__ == "__main__":

    bs = BooleanSearch(['bi', 'mi', 'hi'], 'nonmi')
    cb = bs.creatBoolQuery()
    print(eval(str(cb)))


            # if (item in set(exist) or item[3:] in set(exist)):
                # print(item)
            # if item.startswith('non'):
            #         # print(item)
            #         t = re.sub(item, '0 ', item)
            #         decision = t
            #     else:
            #         t = re.sub(item, ' 1  ', item)
            #         decision = t
            #     newQuery += decision



        # print(exist)
        #         if item.startswith('non'):
        #             # print(item)
        #             t = re.sub(item, '0 ', item)
        #             decision = t
        #         else:
        #             t = re.sub(item, ' 1  ', item)
        #             decision = t
        #         newQuery += decision
        #     else:
        #         newQuery += item
        # print(newQuery)




        #     if item not in ['et', 'ou']:
        #         print(item)
        #         word = item
        #         decision = 1
        #         if item.startswith('non'):
        #             word = item[3:]
        #             decision = 0
        #             # print(word)
        #     newQuery += str(decision)
        # print(newQuery)




            # if(word.strip() in self.wordList or (word.strip().startswith('non') and word.strip()[3:] in self.wordList)):
                # print('Hiiii', word)

            









        # for listWord in conjonctiveQuery:
        #     subNewList = []
        #     for word in listWord:
        #         if(word.strip() not in self.wordList or (word.strip().startswith('non') and word.strip()[3:] not in self.wordList)):
        #             decision = 0
        #         elif word.strip() in self.wordList:
        #             decision = 1
        #         subNewList.append(decision)
        #     newList.append(subNewList)
        # # print(newList)
        # return newList

    
    # def search(self):
    #     finalList = []
    #     newList = self.creatBoolQuery()

    #     for subList in newList:
    #         finalList.append(0) if 0 in subList else finalList.append(1)
    #     # print(finalList)
    #     if 1 in finalList:
    #         return True
    #     return False 



