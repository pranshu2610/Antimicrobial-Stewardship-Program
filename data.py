import os
os.chdir("AntiData")
Path=os.getcwd()
FList=[]
FList=os.listdir()
#DATA from https://www.emedexpert.com/lists/antibiotics.shtml
import eel

eel.init('web')


@eel.expose
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
            #word=str(i)
            #word=word[4:]
            #if '\n' in word:
            #    newword=word.replace('\n','')
            #    word=newword
            #List.append(word)
    return(List)

def getMedCheck(Search):
    for fileName in FList:
        with open(Path+'/'+fileName,'r') as file:
            data = file.readlines()
        for i in data:
            word=str(i)
            if Search in word:
                return True

eel.start('index.html',size=(900, 600))