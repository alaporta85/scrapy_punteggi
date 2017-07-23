### Statistiche sulle classifiche delle leghe scaricate da
### fantagazzetta.com.

import pickle
import pandas as pd

f = open('classifiche.pckl', 'rb')
tutte_le_classifiche = pickle.load(f)
f.close()

def return_both_class(list_of_tuples):                                         # Questa funzione serve per formare le due
    SD = sorted(sorted(list_of_tuples,key=lambda x:x[8],reverse=True),         # classifiche: a scontri diretti e a somma
                key=lambda x:x[1],reverse=True)                                # punti. L'input è una lista di tuples che
    SP = sorted(list_of_tuples,key=lambda x:x[9],reverse=True)                 # è la classifica scrapata da fantagazzetta.
                                                                               # L'output sono due liste: la classifica a
    SD2 = [row[0] for row in SD]                                               # scontri diretti e quella a somma punti.
    SP2 = [row[0] for row in SP]
    
    return SD2,SP2

num_leghe = len(tutte_le_classifiche)
zerocambi = 0
uncambio = 0
duecambi = 0
trecambi = 0
quattrocambi = 0
cinquecambi = 0
vincitore_coincide = 0
ultimo_vince = 0
vincitoreSP_secondo = 0
vincitoreSP_terzo = 0
vincitoreSP_quarto = 0
oltre5 = 0

for lega in tutte_le_classifiche:
    
    cambi = 0                # Il numero di cambi di posizione in classifica.
    
    ''' Definisco le due classifiche.'''
    CSD, CP = return_both_class(tutte_le_classifiche[lega])
    
    '''Il vincitore della CP è anche il vincirore della CSD.'''
    if CSD[0] == CP[0]:
        vincitore_coincide += 1
        
    '''Il vincitore della CP arriva secondo nella CSD.'''
    if CSD[0] == CP[1]:
        vincitoreSP_secondo += 1
        
    '''Il vincitore della CP arriva terzo nella CSD.'''
    if CP[0] == CSD[2]:
        vincitoreSP_terzo += 1
        
    '''Il vincitore della CP arriva quarto nella CSD.'''
    if CP[0] == CSD[3]:
        vincitoreSP_quarto += 1
        
    '''L'ultimo della CP arriva primo nella CSD.'''
    if CP[0] == CSD[-1]:
        ultimo_vince += 1
        
    for name in CSD:
        
        indice = CSD.index(name)
        
        ''' Qui considero il caso in cui le posizioni in classifica di due
            squadre siano invertite tra loro. Es: Nella CSD le squadre A e
            B sono 3° e 5°, rispettivamente, mentre nella CP sono 5° e 3°.
            In questo caso ogni cambio visto dal codice vale 0.5.'''
            
        if name != CP[indice] and CP[CSD.index(CP[indice])] == name:
            cambi += 0.5
            
        elif name != CP[indice] and CP[CSD.index(CP[indice])] != name:         # Qui, contrariamente al caso precedente, considero il caso in cui
            cambi += 1                                                         # le posizioni in classifica di due squadre NON siano invertite
                                                                               # tra loro.
    
        
    if cambi == 0:
        zerocambi += 1
    elif cambi == 1:
        uncambio += 1
    elif cambi == 2:
        duecambi += 1
    elif cambi == 3:
        trecambi += 1
    elif cambi == 4:
        quattrocambi += 1
    elif cambi == 5:
        cinquecambi += 1
    else:
        oltre5 += 1
        
    
results = [zerocambi,uncambio,duecambi,trecambi,
           quattrocambi,cinquecambi,oltre5]

first_row = ['Numero di campionati', '%']

changes = [i for i in range(6)]
changes.append('>5')

data = [(i, round((i/num_leghe)*100,1)) for i in results]

table = pd.DataFrame(data,changes,first_row)

print('\n')
print('\n')
print(table)
print('\n')
print('Stessa squadra che vince entrambe le classifiche: %d (%s%%).'\
      % (vincitore_coincide, round((vincitore_coincide/num_leghe)*100,1)))
print('Primo in somma punti che arriva secondo: %d (%s%%).' % (vincitoreSP_secondo,\
      round((vincitoreSP_secondo/num_leghe)*100,1)))
print('Primo in somma punti che arriva terzo: %d (%s%%).' % (vincitoreSP_terzo,\
      round((vincitoreSP_terzo/num_leghe)*100,1)))
print('Primo in somma punti che arriva quarto: %d (%s%%).' % (vincitoreSP_quarto,\
      round((vincitoreSP_quarto/num_leghe)*100,1)))
print('Ultimo in somma punti che vince la classifica a scontri diretti: %d'\
      '(%s%%).' % (ultimo_vince, round((ultimo_vince/num_leghe)*100,1)))

    
    
    
    