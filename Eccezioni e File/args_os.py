##
# avviando python sul terminale e avviando il file argo_os.py andremo a printare a posizione del file (path)
import sys
print(sys.argv) # argv è una lista che contiene i parametri che staimo passando al nostro programma

for item in sys.argv:
    print(item)