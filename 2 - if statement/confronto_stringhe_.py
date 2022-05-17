##
# Le stringhe sono uguali se e sole se i caratteri sono uguali (anche lo spazio e il case sono aspetti di confonto)
# L'uguaglianza lo faccio con == mentre = è l'operazione di assegnazione

#Vediamo se due stinghe sono uguali

string_1 = "hello"
string_2 = "Hello"

if(string_1 == string_2):
    print("Ugauali")
else:
    print("diverso")

# Con lower andimao a mettere tutto minuscolo il testo
  
string_1 = "hello"
string_2 = "Hello"

if(string_1.lower() == string_2.lower()):
    print("Ugauali")
else:
    print("diverso")
