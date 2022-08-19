import csv
from csv import reader
"""ffile = open("data_key.csv", "r")
dict_reader = csv.DictReader(ffile)

ordered_dict_from_csv = list(dict_reader)[0]
dict_from_csv = dict(ordered_dict_from_csv)

"""
with open('students.csv', 'r') as read_obj: # puts rows into list
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
#   print(list_of_rows)

numSub, lastNum = 0
category = list_of_rows[1] #Fill CATEGORIES
subCat = []
subSubCat =[]
data_key_dict = {}
for elements in category: #FILL SUBCATEGORIES
    if elements == None:
        numSub += 1
        lastCheck = 0
    if lastCheck ==0 and elements != None:
        for j in range(lastNum, numSub):
            subCat.append(list_of_rows[2][j])
        data_key_dict[elements] = subCat
        subCat.clear()
        lastNum  = numSub

#FILL SUB-SUB CATEGORIES
subCat = list_of_rows[2]
numSub, lastNum = 0
for elements in subCat: #FILL SUBCATEGORIES
    if elements == None:
        numSub += 1
        lastCheck = 0
    if lastCheck ==0 and elements != None:
        for j in range(lastNum, numSub):
            subSubCat.append(list_of_rows[3][j])
        data_key_dict[elements] = subSubCat
        subSubCat.clear()
        lastNum  = numSub

filename = open('data_key.csv', 'r')
file = csv.DictReader(filename)

data_lst =[]
i =0

for col in file:
    dataList = list(data_key_dict)
    string = dataList[i]
    data_lst.append(col[string])
    i+=1

