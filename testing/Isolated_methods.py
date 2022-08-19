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

def getInstruments(dictionary, category):
    instrumentRow = df_instruments
    index1 = dictionary[category]
    final = instrumentRow[index1]
    final = final.split(',')
    return final

def printInstruments(array):
    dc = 0
    for element in array:
        print(dc, " element")
        dc+=1

def selectInstrument(index, array):
    return array[index -1]
    
    


def printHotkeys(arrayList): # add hotley arrays to each
    n = 0
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    print(hotkeyDict)

def returnHotkeys(num, arrayList):
    n = 1
    hotkeyDict = {}
    for i in arrayList:
        hotkeyDict[n] = i
        n+=1
    if type(arrayList) is dict:
        v = arrayList.keys()
        v = list(v)
        return v[num]
    else:
        return hotkeyDict

#Execute methods on csv
df_categories = filterCells(fill_dictionary(filename,1 ))
df_subCategories = filterCells(fill_dictionary(filename,2 ))
df_subSubCategories = filterCells(fill_dictionary(filename,3 ))
df_instruments = filterCells(fill_dictionary(filename,5 ))

#print(findSubCategories(df_categories,df_subCategories, 'Lifetime Pharmacological Treatment'))




#LOOP logic
with open(filename2, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    category = input()
    category = str(returnHotkeys(int(category), df_categories))

    subCat1 = findSubCategories(df_categories, df_subCategories, category)

    sub1 = input()
    sub1 =str(returnHotkeys(int(sub1), subCat1))

    # SUBCATEGORY_2
    subCat2 = findSubCategories(df_subCategories, df_subSubCategories, sub1)
    
    #test loop
    printHotkeys(df_categories)

    for item in df_categories:
        print("CAT 1")
        print(str(returnHotkeys(int(item), df_categories)))
        print("SUB SUB")
        for items in df_subCategories:
            print("SUB ")
            print(str(returnHotkeys(int(items), subCat1)))

            for itemss in df_subSubCategories:
                print("SUB SUB")
                print(findSubCategories(df_subCategories, df_subSubCategories, items))
