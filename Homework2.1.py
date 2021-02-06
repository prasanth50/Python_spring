s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
if len(s) != len(indices):
    print('Enter string and indices with same size.')
else:
    t = list(s)  
    for i in range(len(indices)):
        t[indices[i]] = s[i]
    print("".join(t)) 