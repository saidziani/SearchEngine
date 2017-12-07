#!/usr/bin/python3

import nltk, re, os
from nltk.corpus import stopwords
import BooleanSearch
class Indexation():

    def __init__(self, file = False):
        self.file = file


    def load(self, mode):
        return open(self.file, 'r').read().lower() if mode == 1 else open(self.file, 'w')


    def writeSortedDic(self, dic):
        inv = open(self.file+'.inv', 'w')
        for item in sorted(dic.items()):
            toWrite = '['+self.file+','+item[0]+']=>'+str(item[1])
            inv.write(toWrite+'\n')


    def dropEmptyWords(self):
        text = self.load(1) 
        splitedText = text.split()
        return [word for word in splitedText if word not in stopwords.words('english')]


    def dropPonctuation(self):
        text = self.load(1)
        ponctuation = re.compile('[^\w\s]?', re.IGNORECASE)
        return re.sub(ponctuation, '', text)

    def dropApostrophe(self, text):
        listText = text
        for word in text:
            if '\'' in word:
                newText = word.split('\'')
                listText.extend(newText)
                listText.remove(word)

        return listText

    def dropVirgule(self, text):
        listText = text
        for word in text:
            if "," in word:
                newWord = re.sub(",", "", word)
                listText.append(newWord)
                listText.remove(word)
        return listText

    def dropPoint(self, text):
        listText = text
        for word in text:
            if "." in word:
                newWord = re.sub(".", "", word)
                listText.append(newWord)
                listText.remove(word)
        return listText

    def getFreqDist(self):
        text = self.getTextList()
        return nltk.FreqDist(text)

    def getTextList(self):
        text = self.load(1)
        text = self.dropPonctuation()
        text = self.dropEmptyWords()
        text = self.dropApostrophe(text)
        text = self.dropVirgule(text)
        text = self.dropPoint(text)


        return text

    def nbWordOcc(self, word):
        freqDist = self.getFreqDist()
        return freqDist[word]


    def getMaxDist(self):
        from operator import itemgetter
        freqDist = self.getFreqDist()
        return sorted(freqDist.items(), key=itemgetter(1), reverse=True)[0][1]


    def booleanSearch(self, dirrr, query):
        files = os.listdir(dirrr)
        result = []
        for file in files:
            index = Indexation(dirrr+"/"+file)
            text = index.getTextList()
            print(text)
            if query != '':
                b = BooleanSearch.BooleanSearch(text, query)
                if eval(b.creatBoolQuery()):
                    result.append(file)

        if len(result) == 0:
            return ["Not Found!"]
        return result
