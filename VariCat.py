#IMPORT statements
import csv
import pandas as pd
import math
import numpy as np
import os

#PREVIOS neccessary class and method declarations
class Variable:
        def __init__(self, studyName, VarName, VarDescription, Category, SubCategory, SubCategory2, Instrumentation, VarDataType, VarData, relatedVar, interval):
            self.studyName =  studyName
            self.Varname = VarName
            self.VarDescription = VarDescription
            self.Category = Category
            self.SubCategory = SubCategory
            self.SubCategory2 = SubCategory2
            self.Instrumentation = Instrumentation
            self.VarDataType = VarDataType
            self.VarData = VarData
            self.relatedVar = relatedVar
            self.interval = interval
        def returnVals(self):
            data = [ self.studyName, self.Varname,self.VarDescription,self.Category,self.SubCategory ,self.SubCategory2 ,self.Instrumentation,self.VarDataType, self.VarData, self.relatedVar, self.interval ]
            return data

data = []
varContainer = []
x = 1
varFormat = ["StudyName","VarName", "VarDescription", "Category", "SubCategory", "SubCategory2", "Instrumentation", "VarDataType", "VarData","relatedVar","intervals"]

#FILL and mapping methods
filename1 = "GAGE-DD_Automation_051921.xlsx - Sheet1.csv"
filename2 = 'test_driver.csv'

def pStars():
    print("************************************")


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
#    print(val1, " ", category)
    for i in dictionary: 
        if dictionary[i] > val1: 
            s = str(i)
            break

    val2 = dictionary[s]

    for j in nxtDict:
        if nxtDict[j] > val1:
            if nxtDict[j] < val2: 
                arr2.append(j)
    return arr2

def getInstruments(dictionary, category):
    index1 = dictionary[category]
    print(index1)
    print(type(df_instruments))
    j = 0
    final = 0
    for i in df_instruments:
            if j == index1:
                final = i
                final = final.split(',')
                print(i)
                break
            j+=1
    if final == 0:
        final == ["no instruments available"]
    return final

def printInstruments(array):
    dc = 0
    for element in array:
        print(dc, element)
        dc+=1

def selectInstrument(index, array):
    print(index)
    index = int(index)
    return array[index]
    
out_csv = " "


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

def printCSV():
    arr = []
    for entry in os.scandir('.'):
        if entry.is_file():
            s = str(entry)
            s2 = s[-5:-2]
            if s2 == 'csv':
                arr.append(s)
    return arr

def saveTo():
        file = open(out_csv, 'a+', newline ='')

        # writing the data into the file
        with file:    
            write = csv.writer(file)
            write.writerows(data)


#get vsv
csvlst = printCSV()
i=0
print("select a csv file to run the program on")
k = os.path.dirname(os.path.abspath(__file__))

for x in csvlst:
    print(i, ":", x)
    i+=1
pStars()
i = input()
csvUse = csvlst[int(i)]
l = csvUse.replace("<DirEntry '", '')
l = l.replace("'>", '')
print(str(k))

k = k + "/" + l
print(k)
filename = k
#Execute methods on csv
df_categories = filterCells(fill_dictionary(filename,1 ))
df_subCategories = filterCells(fill_dictionary(filename,2 ))
df_subSubCategories = filterCells(fill_dictionary(filename,3 ))
df_instruments = filterCells(fill_dictionary(filename,5 ))

df_r = pd.read_csv(filename2)
df_r_l = list(df_r["variable"])
#print(df_r_l)

#print(findSubCategories(df_categories,df_subCategories, 'Lifetime Pharmacological Treatment'))

print("enter name of this study:")
pStars()
studyName = input()
name1 = ""
out_csv = studyName + ".csv"
pStars()

data.append(varFormat)
saveTo()
data.clear()

#LOOP logic
def main_driver():
    with open(filename2, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row[0] == "variable":
                x = 0
            else:
                # NAME
                name = name1+ ":" +row[0]
                description = row[1]
                print("\n now dealing with variable :", name)

                # DESCRIPTION
                if  len(row[1]) == 1: 
                    print("No description, would you like to add one [y/n] ?")
                    i = input()
                    if i == 'y':
                        print("enter description")
                        pStars()
                        description = input()
                        pStars()
                else: 
                    print("The description is:", row[1])
                    print("would you like to change it [y/n] ?")
                    pStars()
                    i = input()
                    pStars()
                    if i == 'y':
                        print("enter description:")
                        pStars()
                        description = (input()) 
                        pStars()

                # CATEGORY
                print("The available categories are as follows:\n")
                printHotkeys(df_categories)
                print("Select a default category or enter a custom category")
                pStars()
                category = input()
                pStars()
                category = str(returnHotkeys(int(category), df_categories))
                #ADD OPTION FOR MISC!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


                
                subCat1 = findSubCategories(df_categories, df_subCategories, category)

                print("Select a subcategory:")
                print("[O]ther for other category")  
                printHotkeys(subCat1)
                pStars()
                sub1 = input()
                pStars()
                if sub1 == "o" or sub1 == "O":
                    sub1 = "other"
                else: sub1 =str(returnHotkeys(int(sub1), subCat1))
                print(sub1)
                
                # SUBCATEGORY_2  >> NO SECOND SUB CATEGORY

                if sub1 == "other" or sub1 == "Other":
                    sub2 = "other"
                else: 
                    subCat2 = findSubCategories(df_subCategories, df_subSubCategories, sub1)
                    if subCat2 == []:
                        print("no second subcategory available")
                        sub2 = 0

                    else:
                        print("select a second subcategory")
                        print("[O]ther for other category")
                        printHotkeys(subCat2)
                        pStars()
                        sub2 = input()
                        pStars()
                        if sub2 == "o" or sub2 == "O":
                            sub2 = "other"
                        else :sub2 = str(returnHotkeys(int(sub2), subCat2))

                                
                # INSTRUMENTATION >> MAKE SURE ONLY RELEVANT INSTRUMENTATION SHOWN >> CATCH @ SUB FETCH METHOD
                #EACH cell is an arr datatype, not corresponding to branchign >> write seperate method
                print("was instrumentaion used [y/n]")
                pStars()
                i = input()
                pStars()
                if i == 'y':
                    if type(sub2) is int and sub2>0:
                        instrumentList = getInstruments( df_subSubCategories, sub2)
                        g = 1
                    elif type(sub1) is int and sub1>0:
                        instrumentList = getInstruments( df_subCategories, sub1)
                        print("Select from the following list or enter your own:")
                        printInstruments(instrumentList)
                        g = 1
                    else:
                        print("enter the instrument:")
                        g = 0
                    pStars()
                    instrument = input()
                    pStars()
                    if g == 1: instrument = selectInstrument(instrument, instrumentList)
                    print(" would you like to enter any information regarding the methodology of the data collection [y/n] ?")
                    pStars()
                    i = input()
                    pStars()
                    if i =='y': 
                        print("enter:")
                        pStars()
                        instrument = input()
                        pStars()
        #           else: instrument = str(selectInstrument(int(instrument), instrumentList))

                else: instrument = 0

                # VARIABLE TYPE
                print("Is the variable data [0]continous or [1]categorical?") #CATEGORICAL / CONSTINTUOUS HOTKEYS >> 2 CHAIN IF/ELIF
                #IF CATEGORICAL: HOW MANY CATEGORIS && LOOP THRU VALUE // DESCRIPTION FOReach loop
                pStars()
                varType = input()
                pStars()
                if varType == "1":
                    print("how many levels?")
                    pStars()
                    levels = input()
                    pStars()
                    levelLst = []
                    for l in range(0,int(levels)):
                        print("enter level ", l+1)
                        pStars()
                        lev = input()
                        pStars()
                        levelLst.append(lev)
                    varType = levelLst
                else:
                    varType = "discrete"

                #VARIABLE DATA
                if instrument == 0:
                    varData = 0
                else:
                    print("is this an item or summary score ?[ 0: item / 1: summary]")
                    pStars()
                    varData = input()
                    pStars()
                    if int(varData) == 0:
                        print("enter item numner")
                        pStars()
                        g = input()
                        pStars()
                        varData = "item: " + str(g)
                    elif int(varData) == 1:
                        varData = "summary"
                        #select && return summary



                #IS THIS VARIABLE DEPendent
                print("is this variable dependent on others?")
                df_r_index = df_r_l.index(row[0])
                print(df_r_l.index(row[0]))

                j = df_r_index - 2
                j2 = df_r_index + 2

                """                if df_r_index < 5:
                    j = 0
                    while df_r_index >= 0:
                        df_r_index-=1
                        j+=1
                j = df_r_index - j
                print("n: no")
                #kk = (len(df_r_l)-df_r_index)
                j2 = df_r_index + 5"""
                """                if kk < 5:
                    j2 = kk-1"""
                for i in range(j,j2):
                    print( i, ": ", df_r_l[i])
                rVar = input()
                if rVar =="n":
                    rVar = "no dependecy"
                else: rVar = df_r_l[int(rVar)]


                intervals = input("Was this variable entered at multiple intervals? [y/n] \n")
                #ENTER DATA
                varObject =  Variable(studyName, name, description, category, sub1, sub2, instrument, varType, varData, rVar, intervals)
                varContainer = varObject.returnVals()
                print(" do you want to enter these values ?  [y/n] \n", varContainer, "under the name:", name) #BACK OPTION >> variable behind it
                i = input()
                if i == "y":
                    data.append(varContainer)
                    saveTo()
                    data.clear()
                else:
                    if row[0] == "variable":
                        x = 0
                    else:
                        main_driver()

main_driver()
"""# opening the csv file in 'a+' mode
file = open('test.csv', 'a+', newline ='')
  
# writing the data into the file
with file:    
    write = csv.writer(file)
    write.writerows(data)"""
