"""
INSERT CSV CONVERSION CODE IN HERE
"""
data1 = [["name", "var1", "var2", "var3"],["a", 1,1,"x" ],["b", 2,1,"y" ],["c", 3,1,"z" ]] # SAMPLE data set to be translated

data2 = data1 #CLONE data set to make an output datastructure

key_dict = {"name":{"a":1,"b":2,"c":3}, "var1":{1:3,2:2,3:1}, "var2":{1:-1,2:-2,3:-3}, "var3":{"x":1,"y":2,"z":3}}
# ^^KEY for converting^^
#This would be assigned by the user within the GUI 


x = 4 #number of variables /  collums in top row

for i in range(0,x):
    search_string = data1[0][i]
    print(search_string)

    data2[0][i] = search_string

    print(key_dict[search_string])
    mini_dict = key_dict[search_string]
    
    y = 1
    for key in mini_dict: # loop syntax auto iterates throught the 
        print (key, 'corresponds to', mini_dict[key])
        data2[y][i] = mini_dict[key]
        y+= 1


print(data2)        
