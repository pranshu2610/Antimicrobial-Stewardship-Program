import os
import CSVdata
import csv
#os.chdir("Desktop/Antimicrobal")
#PathPharm=os.getcwd()
PathPharm='/Users/prans/Desktop/Antimicrobal'

def invoiceData():
    with open(PathPharm+'/PharmacyInvoice.csv','rt') as file:
        dataName = csv.reader(file)
        AntiBio=[]
        for row in dataName:
            if CSVdata.getMedCheck(row[0]):
                AntiBio.append(row[0])
    AntiBio=AntiBio[:-1]
    dash="-"
    print("\n"+dash*78)
    print(AntiBio)

if __name__ == "__main__":
    invoiceData()
