#IMPORT statements
import csv
import pandas as pd
import math
import numpy as np

#PREVIOS neccessary class and method declarations
class Variable:
        def __init__(self, VarName, VarDescription, Category, SubCategory, SubCategory2, Instrumentation, VarDataType, VarData):
            self.Varname = VarName
            self.VarDescription = VarDescription
            self.Category = Category
            self.SubCategory = SubCategory
            self.SubCategory2 = SubCategory2
            self.Instrumentation = Instrumentation
            self.VarDataType = VarDataType
            self.VarData = VarData
        def returnVals(self):
            data = [  self.Varname,self.VarDescription,self.Category,self.SubCategory ,self.SubCategory2 ,self.Instrumentation,self.VarDataType, self.VarData ]
            return data

data = []
varContainer = []
x = 1
varFormat = ["VarName", "VarDescription", "Category", "SubCategory", "SubCategory2", "Instrumentation", "VarDataType", "VarData"]

#FILL and mapping methods
filename = "GAGE-DD_Automation_051921.xlsx - Sheet1.csv"
filename2 = 'test_driver.csv'

def fill_dictionary(FILENAME, collumnNum):
    col_list = ["Domain","Category B","Category C","filler","Instruments"] #ENSURE THESE VALUSE ARE CONSISTENT WITH CSV FILE
    df = pd.read_csv(FILENAME, usecols=col_list)
    return df[col_list[collumnNum-1]]

def filterCells(df):
    dict1 = {}
    j = 0
    for i in df:
        j+=1
        if str(i) != "nan":
            dict1[i] = j
    return dict1

def findSubCategories(dictionary, nxtDict, category):
    arr1 = []
    arr2 = []
    val1 = dictionary[category]
    for i in dictionary: 
        if dictionary[i] > val1: 
            arr1.append(i)
    val2 = dictionary[min(arr1)]

    for j in nxtDict:
        if nxtDict[j] > val1 and nxtDict[j] < val2: 
            arr2.append(j)
    return arr2

def printHotkeys(arrayList): # add hotley arrays to each
    n = 0
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    print(hotkeyDict)

def returnHotkeys(num, arrayList): #ADJUST FRO OTHER OPTION ATTHE END >> INCLUDE CUSTOM OPTION @ END AS REMINDER
    n = 1
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    if type(arrayList) is dict:
        v = arrayList.keys()
        v = list(v)
        return v[num]
    else: return arrayList[num]

def saveTo():
        file = open('test.csv', 'a+', newline ='')

        # writing the data into the file
        with file:    
            write = csv.writer(file)
            write.writerows(data)
#Execute methods on csv
df_categories = filterCells(fill_dictionary(filename,1 ))
df_subCategories = filterCells(fill_dictionary(filename,2 ))
df_subSubCategories = filterCells(fill_dictionary(filename,3 ))
df_instruments = filterCells(fill_dictionary(filename,5 ))

#print(findSubCategories(df_categories,df_subCategories, 'Lifetime Pharmacological Treatment'))




#LOOP logic
with open(filename2, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    for row in datareader:
        # NAME
        name = row[0]
        description = row[1]
        print("\n now dealing with variable :", name)

        # DESCRIPTION
        if  len(row[1]) == 1: 
            print("No description, would you like to add one [y/n] ?")
            i = input()
            if i == 'y':
                print("enter description")
                description = input()
        else: 
            print("The description is:", row[1])
            print("would you like to change it [y/n] ?")
            i = input()
            if i == 'y':
                print("enter description:")
                description = (input()) 

        # CATEGORY
        print("The available categories are as follows:\n")
        printHotkeys(df_categories)
        print("Select a default category or enter a custom category")
        category = input()
        category = str(returnHotkeys(int(category), df_categories))
        #ADD OPTION FOR MISC!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


        
        subCat1 = findSubCategories(df_categories, df_subCategories, category)

        print("Select a subcategory, or enter a new one:")  
        printHotkeys(subCat1)
        sub1 = input()
        sub1 =str(returnHotkeys(int(sub1), subCat1))
        print(sub1)
        
        # SUBCATEGORY_2  >> NO SECOND SUB CATEGORY

        print("would you like to add a second subcategory  [y/n] ?")
        i = input()
        if(i == "y") :
            subCat2 = findSubCategories(df_subCategories, df_subSubCategories, sub1)
            print("select a second subcategory")
            printHotkeys(subCat2)
            sub2 = input()
            sub2 = str(returnHotkeys(int(sub2), subCat2))
        else:
            sub2 = 0
                        
        # INSTRUMENTATION >> MAKE SURE ONLY RELEVANT INSTRUMENTATION SHOWN >> CATCH @ SUB FETCH METHOD
        #EACH cell is an arr datatype, not corresponding to branchign >> write seperate method
        print("was instrumentaion used [y/n]")
        i = input()
        if i == 'y':
            instrumentList = findSubCategories(df_categories, df_instruments, category)
            print("Select from the following list or enter your own:")
            printHotkeys(instrumentList)
            instrument = input()
            instrument = str(instrument)
            if instrument == "Other":
                print(" would you like to enter any information regarding the methodology of the data collection [y/n] ?")
                i = input()
                if i =='y': 
                    print("enter:")
                    instrument = input()
            else: instrument = str(returnHotkeys(int(instrument), instrumentList))

        else: instrument = 0

        # VARIABLE TYPE
        print("what kind of data is stored in this varibale ?") #CATEGORICAL / CONSTINTUOUS HOTKEYS >> 2 CHAIN IF/ELIF
        #IF CATEGORICAL: HOW MANY CATEGORIS && LOOP THRU VALUE // DESCRIPTION FOReach loop
        varType = input()

        #VARIABLE DATA
        print("is this an item or summary score ?[ 0: item / 1: summary]")
        varData = input()
        if int(varData) == 0:
            print("enter item numner")
            g = input()
            varData = "item: " + str(g)
        elif int(varData) == 1:
            varData = "summary"
            #select && return summary



        #IS THIS VARIABLE DEPendent


        #ENTER DATA
        varObject =  Variable(name, description, category, sub1, sub2, instrument, varType, varData)
        varContainer = varObject.returnVals()
        print(" do you want to enter these values ?  [y/n] \n", varContainer) #BACK OPTION >> variable behind it
        i = input()
        if i == "y":
            data.append(varContainer)

        #ADD SECOND SAVE OPTION (WITHOUT EXITING)
        saveTo()
        #BREAK
        print("press (y) to save and exit, or (n) to continue:")
        breakVar = input()
        if breakVar == "y": break

  
# opening the csv file in 'a+' mode
file = open('test.csv', 'a+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(data)
