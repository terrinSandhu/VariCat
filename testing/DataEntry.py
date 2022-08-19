"""import csv

filename = 'test_driver.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if  len(row[1]) == 1:
            print(row[0])
"""

varContainer = []
#loop condition
x = 1
# multidimensional dict to contain value, categories & subcategories
# hardcode vs. csv O(n) -- run data sim // time efficency

dataKey = {"cat1":["sub1", "sub2", "sub3"] , 
        "cat2" : ["sub4", "sub5", "sub6"] , 
        "cat3": ["sub7", 
            {"sub8": ["a", "b","c"]}]
}

#class to store data for csv input
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

#driver loop for comand line interface (later tio be connected to GUI)
while(x ==1):

    print("enter var name")   # take variable name from csv file from column && include description
    a1 = input()
    print(dataKey.keys()) # add option for other 

    # if other : enter new cat && sub cat && sub2
    # add misc category for extreem DNE

    a = input()
    print(dataKey[a])

    b = input()

    #print(type(dataKey[b]))  #delete l8er
    if(isinstance(b,dict)):
        print(dataKey[b])

        c = input()
    else:
        c = 0


#ssee documentation for  lists of instrumentation
    print("Was instrumentation used, if so specify which kind was utilized, else enter 0") # connnect list based on categories (python psuedo switch statement)
    d = input()

# item level vs toatal score || both || item level(if: whichc) // summary level variable(spec ?)
# ^^ add defaults to whichever entry was last^^
# see MEQ 4 example on default cases -- iteration over same form
# y/n? --- reverse scored scales --- include scoring scales ?


    print("What kind of data does this variable contain? (Continous / Categorical)")
    e = input()

    print("Enter the data contained by this variable:") # modify to make clearer only appliccable tp categorical && connect
    f = input() 
                    # loop thru num of categories && includes defaults that have common occurences

    
    newVar = Variable(a1,a,b,c,d,e,f)
    varContainer.append(newVar)

    print("press 1 to continue, and 2 to enter")
    x = input()

# enter elenments int csv file
# add reminder for usercase 4 accidental close out
# autosace feature
#continue feature for csv files

#select local files -- new// continiue 

# search alg for insertion into csv for organized file  
# last entered vatriable on csv -- on loop mechanics

"""
PRINT BY VARIABLE -- formatting will be handles by query 
no need for filter // search ?? 

if category DNE: add option ot enter new variables
"""


print(varContainer)
