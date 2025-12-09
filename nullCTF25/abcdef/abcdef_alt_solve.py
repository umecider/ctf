#iterate through all int versions of alphabet, convert into oct, turn into literal string
all_letters = []
for x in range(97, 123):
    all_letters.append("\'\\"+str(oct(x))[2:]+"\'")
print("abcdef = [", end = ' ')
for i in range(len(all_letters)):
    if i == len(all_letters)-1:
        print(all_letters[i]+ "]")
    else:
        print(all_letters[i] + ", ", end='')
