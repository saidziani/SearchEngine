#!/usr/bin/python3

import Indexation
import os, math

class Inverse():

    def __init__(self, directory = False):
        self.directory = directory


    def dirFiles(self):
        return os.listdir(self.directory)


    def buildInv(self):
        files = self.dirFiles()
        for file in files:
            index = Indexation.Indexation(self.directory+''+file)
            dic = index.getFreqDist()
            index.writeSortedDic(dic)


    def nbDocsOcc(self, word):
        nbDocs = 0
        files = self.dirFiles()
        for file in files:
            index = Indexation.Indexation(self.directory+''+file)
            if index.nbWordOcc(word):
                nbDocs += 1
        return nbDocs


    def getSetWords(self):
        wordsSet = []
        files = self.dirFiles()
        for file in files:
            index = Indexation.Indexation(self.directory+''+file)
            words = index.getTextList()
            wordsSet.extend(words)

        return(list(set(wordsSet)))


    def getInv(self):
        files = self.dirFiles()
        setWords = self.getSetWords()
        inv = []
        for word in setWords:
            freq = [word]
            for file in files:
                index = Indexation.Indexation(self.directory+''+file)
                nbWordOcc = index.nbWordOcc(word)
                freq.append(nbWordOcc)
            freq.append(self.nbDocsOcc(word))
            inv.extend([freq])
        return inv


    def getMaxDocsOcc(self):
        files = self.dirFiles()
        maxs = []
        for file in files:
            index = Indexation.Indexation(self.directory+''+file)
            max = index.getMaxDist()
            maxs.append(max)
        return maxs


    def getPonderation(self):
        # ['conceiving', 0, 1, 1]
        N = len(self.dirFiles())
        files = self.dirFiles()
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
        return ponderations

    def getPondSpec(self, wordList):
        N = len(self.dirFiles())
        files = self.dirFiles()
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
        return ponderations
        


if __name__ == "__main__":
    inv = Inverse('docs/') 
    wordList = ['langage', 'java']
    print(inv.getPondSpec(wordList))