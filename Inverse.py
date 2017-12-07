#!/usr/bin/python3

import Indexation
import os, math

class Inverse():

    def __init__(self, directory = False, exped = 1):
        self.directory = directory
        self.exped = exped


    def dirFiles(self):
        return os.listdir(self.directory)


    def buildInv(self):
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory

        for file in files:
            if self.exped == 1:
                index = Indexation.Indexation(self.directory+''+file)
            else:
                index = Indexation.Indexation(file)
            dic = index.getFreqDist()
            index.writeSortedDic(dic)


    def nbDocsOcc(self, word):
        nbDocs = 0
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory

        for file in files:
            if self.exped == 1:
                index = Indexation.Indexation(self.directory+''+file)
            else:
                index = Indexation.Indexation(file)

            if index.nbWordOcc(word):
                nbDocs += 1
        return nbDocs


    def getSetWords(self):
        wordsSet = []
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory
        for file in files:
            if self.exped == 1:
                index = Indexation.Indexation(self.directory+''+file)
            else:
                index = Indexation.Indexation(file)
            words = index.getTextList()
            wordsSet.extend(words)

        return(list(set(wordsSet)))


    def getInv(self):
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory
        setWords = self.getSetWords()
        inv = []
        for word in setWords:
            freq = [word]
            for file in files:
                # print(file)
                if self.exped == 1:
                    index = Indexation.Indexation(self.directory+''+file)
                else:
                    index = Indexation.Indexation(file)
                nbWordOcc = index.nbWordOcc(word)
                freq.append(nbWordOcc)
            freq.append(self.nbDocsOcc(word))
            inv.extend([freq])
        # print(files)
        # print(inv)
        return inv


    def getMaxDocsOcc(self):
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory
        
        maxs = []
        for file in files:
            if self.exped == 1:
                index = Indexation.Indexation(self.directory+''+file)
            else:
                index = Indexation.Indexation(file)
            max = index.getMaxDist()
            maxs.append(max)
        return maxs


    def getPonderation(self):
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory
        
        N = len(files)
        inv = self.getInv()
        maxs = self.getMaxDocsOcc()
        ponderations = []
        for i in range(N):
            pds = []
            for item in inv:
                freq, word, nbDocsOcc, max = item[i+1], item[0], item[-1], maxs[i]

                pd = (freq/max) * math.log10((N/nbDocsOcc)+1)
                pds.append((word,pd))

            ponderations.append((files[i], pds))
        print(ponderations)
        return ponderations

    def getPondSpec(self, wordList):
        if self.exped == 1:
            files = self.dirFiles()
        else:
            files = self.directory
        
        N = len(files)

        inv = self.getInv()
        maxs = self.getMaxDocsOcc()
        ponderations = []
        for i in range(N):
            pds = []
            for item in inv:
                if item[0] in wordList:
                    freq, word, nbDocsOcc, max = item[i+1], item[0], item[-1], maxs[i]

                    pd = (freq/max) * math.log10((N/nbDocsOcc)+1)
                    pds.append((word,pd))

            ponderations.append((files[i], pds))
        print(ponderations)
        return ponderations
        


if __name__ == "__main__":
    inv = Inverse('docs/') 
    wordList = ['langage', 'java']
    print(inv.getPondSpec(wordList))