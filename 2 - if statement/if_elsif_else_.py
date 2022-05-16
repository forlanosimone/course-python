#Di solito si sabglia il case quando uno deve fare una scelta ES."vuoi continuare?"
#Codice pessimo c'è tanta ripetizione

scelta=input("vuoi continuare?")
if(scelta=="Y"): #L'utente può digitare la Y o y 
    print("ho scelto si...")
elif(scelta=="y"):
    print("ho scelto si...")
elif(scelta=="n"):
    print("ho scelto no...")
elif(scelta=="N"):
    print("ho scelto no...")
else:
    print("scegli tra Y or N")

########################################################################################################
########################################################################################################

#Codice migliorato ma leggermente ripetuto

scelta=(input("vuoi continuare?"))
if(scelta.lower()=="y"):
    print("ho scelto si...")
elif(scelta.lower()=="n"):
    print("ho scelto no...")
else:
    print("scegli tra Y or N")

########################################################################################################
########################################################################################################

#Codice ottimizzato

scelta=(input("vuoi continuare?")).lower()
#scelta=scelta.lower() #posso farlo tutto nella prima riga altrimenti lo faccio alla seconda linea
if(scelta=="y"):
    print("ho scelto si")
elif(scelta=="n"):
    print("ho scelto no...")
else:
    print("scegli tra Y or N")

########################################################################################################
########################################################################################################