import os
os.chdir("AntiData")
Path=os.getcwd()
FList=[]
FList=os.listdir()
#DATA from https://www.emedexpert.com/lists/antibiotics.shtml

def getMedUpdate(Search):
    List=[]
    for fileName in FList:
        with open(Path+'/'+fileName,'r') as file:
            data = file.readlines()
        for i in data:
            word=str(i)
            if Search in word:
                if '\n' in word:
                    newword=word.replace('\n','')
                    word=newword
                medcata=fileName.replace('.txt','')
                List.append(word + '\t '+medcata)

    return(List)

def getMedCheck(Search):
    for fileName in FList:
        with open(Path+'/'+fileName,'r') as file:
            data = file.readlines()
        for i in data:
            word=str(i)
            if Search in word:
                return True
