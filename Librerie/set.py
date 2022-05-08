##
# Verificare ai quali bandiere appartengono i colori delle bandiere con gli insiemi

canadian = {"R","W"}
british = {"R","B","W"}
italian = {"R","W","G"}

if canadian.issubset(british):
    print("Tutti i colori della bandiera del Canada sono nella bandiera dell Regno Unito")

if not italian.issubset(british):
    print("Almeno un colore della bandiera dell'Italia non appartiene ai colori della bandiera del Regno Unito")

