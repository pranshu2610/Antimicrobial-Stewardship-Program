import eel
eel.init('web')

import os
os.chdir("AntiData")
Path=os.getcwd()
FList=[]
FList=os.listdir()
    

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
                List.append(word + '\t : '+medcata+", ")
    return List


eel.start('index.html', size=(900,600))
#if __name__ == "__main__":
#    print(getMedUpdate("Ertapenem"))
