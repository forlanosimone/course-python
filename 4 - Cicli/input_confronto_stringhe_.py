s1=input("inserisci la 1° stringa:")
#print(len(s1))
s2=input("inserisci la 2° stringa:")
#print(len(s2))

if(len(s1) != len(s2)):
    print("le stringhe sono diverse")
else:    
    for i in range(len(s1)): #metto len(s1) e non (len(s1)-1) perché range includa già j-1
        if(s1[i] != s2[i]):
            print("le stringhe sono diverse")
            break
        else:
            i=i+1
    print("le stringhe sono uguali")

print("####################")

i=0

if(len(s1) != len(s2)):
    print("le stringhe sono diverse")
else:    
    for i in range(len(s1)): #metto len(s1) e non (len(s1)-1) perché range includa già j-1
        if(s1[i] == s2[i]):
            i=i+1
        else:
            print("le stringhe sono diverse")
    print("le stringhe sono uguali")