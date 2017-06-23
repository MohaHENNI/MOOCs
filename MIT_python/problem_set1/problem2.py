l = len (s)
i = s.find ("b") 
count = 0

while i != -1:
    if i < l - 2:
        print (s [i+1:i+3])
        if s[i+1:i+3] == 'ob':
            count += 1
        i = s.find ("b", i+1) 
    else :
        i = -1
print ("Number of times bob occurs is: "+ str(count))
