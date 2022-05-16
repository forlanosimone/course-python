#Le stringhe sono uguali se e sole se i caratteri sono ugali (anche lo spazio e il case sono aspetti di confonto)
#L'uguaglianza lo faccio con == mentre = è l'operazione di assegnazione

#Vediamo se due stinghe sono uguali

string1="hello"
string2="Hello"

if(string1 == string2):
    print("Ugauali")
else:
    print("diverso")

########################################################################################################
########################################################################################################

#Con lower andimao a mettere tutto minuscolo il testo
  
string1="hello"
string2="Hello"

if(string1.lower() == string2.lower()):
    print("Ugauali")
else:
    print("diverso")

########################################################################################################
########################################################################################################