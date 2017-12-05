#!/usr/bin/python3

import Indexation, Inverse, re, nltk, math
from nltk.corpus import stopwords
from operator import itemgetter

class Vectorial():

    def __init__(self, directory = False, query = False, exped = 1):
        self.directory = directory
        self.query = query
        self.exped = exped


    def getPropQuery(self):
        query = self.query
        ponctuation = re.compile('[^\w\s]?', re.IGNORECASE)
        propQuery = re.sub(ponctuation, '', query)
        propQuery = query.split()
        propQuery = [word for word in propQuery if word not in stopwords.words('french')]
        return propQuery, nltk.FreqDist(propQuery)


    def innerProduct(self):
        propQuery, FreqDist = self.getPropQuery()
        if self.exped == 1:
            pond = Inverse.Inverse(self.directory).getPondSpec(propQuery)
        else:
            pond = Inverse.Inverse(self.directory, 2).getPondSpec(propQuery)

        rsvDocs = []
        for doc in pond:
            RSV = 0
            for docTuple in doc[1]:
                if docTuple[0] in FreqDist.keys():
                    word = docTuple[0]
                    occ, freq = FreqDist[word], docTuple[1]
                    RSV += occ * freq
            rsvDocs.append((doc[0], round(float(RSV),3)))
            rsvDocsSorted = sorted(rsvDocs, key=itemgetter(1), reverse=True)
        return rsvDocsSorted


    def diceCoef(self):
        propQuery, FreqDist = self.getPropQuery()
        if self.exped == 1:
            pond = Inverse.Inverse(self.directory).getPondSpec(propQuery)
        else:
            pond = Inverse.Inverse(self.directory, 2).getPondSpec(propQuery)

        sumFreqDist = 0
        for item in FreqDist.values():
            powFreq = item * item
            sumFreqDist += powFreq
        rsvDocs = []
        for doc in pond:
            subRSV = 0
            RSV = 0
            sumPond = 0
            for docTuple in doc[1]:
                sumPond += math.pow(float(docTuple[1]), 2)
                if docTuple[0] in FreqDist.keys():
                    word = docTuple[0]
                    occ, freq = FreqDist[word], docTuple[1]
                    subRSV +=  (occ * freq)
            RSV = (2 * subRSV) / (sumPond + sumFreqDist)
            rsvDocs.append((doc[0], round(float(RSV),3)))
            rsvDocsSorted = sorted(rsvDocs, key=itemgetter(1), reverse=True)
        return rsvDocsSorted


    def cosinusMesure(self):
        propQuery, FreqDist = self.getPropQuery()
        if self.exped == 1:
            pond = Inverse.Inverse(self.directory).getPondSpec(propQuery)
        else:
            pond = Inverse.Inverse(self.directory, 2).getPondSpec(propQuery)

        sumFreqDist = 0
        for item in FreqDist.values():
            powFreq = item * item
            sumFreqDist += powFreq

        rsvDocs = []
        for doc in pond:
            subRSV = 0
            RSV = 0
            sumPond = 0
            for docTuple in doc[1]:
                sumPond += math.pow(float(docTuple[1]), 2)
                if docTuple[0] in FreqDist.keys():
                    word = docTuple[0]
                    occ, freq = FreqDist[word], docTuple[1]
                    subRSV +=  (occ * freq)
            calc = math.sqrt(sumPond * sumFreqDist)
            RSV = 0
            if (calc != 0):
                RSV = (subRSV) / calc
            rsvDocs.append((doc[0], round(float(RSV),3)))
            rsvDocsSorted = sorted(rsvDocs, key=itemgetter(1), reverse=True)
        return rsvDocsSorted


    def jaccardMesure(self):
        propQuery, FreqDist = self.getPropQuery()
        if self.exped == 1:
            pond = Inverse.Inverse(self.directory).getPondSpec(propQuery)
        else:
            pond = Inverse.Inverse(self.directory, 2).getPondSpec(propQuery)
            
        sumFreqDist = 0
        for item in FreqDist.values():
            powFreq = item * item
            sumFreqDist += powFreq
        rsvDocs = []
        for doc in pond:
            subRSV = 0
            RSV = 0
            sumPond = 0
            for docTuple in doc[1]:
                sumPond += math.pow(float(docTuple[1]), 2)
                if docTuple[0] in FreqDist.keys():
                    word = docTuple[0]
                    occ, freq = FreqDist[word], docTuple[1]
                    subRSV +=  (occ * freq)
            RSV = (subRSV) / (sumPond + sumFreqDist - subRSV)
            rsvDocs.append((doc[0], round(float(RSV),3)))
            rsvDocsSorted = sorted(rsvDocs, key=itemgetter(1), reverse=True)
        return rsvDocsSorted






# if __name__ == "__main__":
#     a = "langage le python langage "
    
#     v = Vectorial('/media/said/DevStuff/Master2-Sii/RI/Projet_RI/docs/', a)

#     # print("Dice coef", v.diceCoef())
#     # print("Cos mesure", v.cosinusMesure())
#     # print("Jaccard mesure", v.jaccardMesure())
#     print("inner product", v.innerProduct())



    
