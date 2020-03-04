import data

def displayList(List):
    print('Generic \tBrand Name \tAntibiotic Category')
    for i in List:
        print(i)

if __name__ == "__main__":
#    MedList=[]
#    DeadMeds=[]
#    ResultMeds=[]
#    MedList=data.getMedUpdate('meds')
#    DeadMeds=data.getMedUpdate('DeletedMeds')
    Search=str(input('Enter your prescription: '))
    ResultMeds=data.getMedUpdate(Search)
    displayList(ResultMeds)
    
    