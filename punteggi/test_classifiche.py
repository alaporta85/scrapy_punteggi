import pickle
import pandas as pd

f = open('classifiche.pckl', 'rb')
tutte_le_classifiche = pickle.load(f)
f.close()

def return_both_class(list_of_tuples):
    SD = sorted(sorted(list_of_tuples,key=lambda x:x[8],reverse=True),key=lambda x:x[1],reverse=True)
    SP = sorted(list_of_tuples,key=lambda x:x[9],reverse=True)
    
    SD2 = [row[0] for row in SD]
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
#==============================================================================
# seicambi = 0
# settecambi = 0
# ottocambi = 0
#==============================================================================
oltre5 = 0

for lega in tutte_le_classifiche:
    
    cambi = 0
    
    class_SD, class_SP = return_both_class(tutte_le_classifiche[lega])
    
    if class_SD[0] == class_SP[0]:
        vincitore_coincide += 1
    if class_SD[0] == class_SP[-1]:
        ultimo_vince += 1
    
    for name in class_SD:
        
        indice = class_SD.index(name)
        
        if name != class_SP[indice] and class_SP[class_SD.index(class_SP[indice])] == name:
            cambi += 0.5
        elif name != class_SP[indice] and class_SP[class_SD.index(class_SP[indice])] != name:
            cambi += 1
    
        
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
#==============================================================================
#     elif cambi == 6:
#         seicambi += 1
#     elif cambi == 7:
#         settecambi += 1
#     elif cambi == 8:
#         ottocambi += 1
#==============================================================================
    else:
        oltre5 += 1
        
    
results = [zerocambi,uncambio,duecambi,trecambi,quattrocambi,
           cinquecambi,oltre5]
first_row = ['Numero di campionati', '%']
changes = [i for i in range(6)]
changes.append('>5')
data = [(i, round((i/num_leghe)*100,1)) for i in results]

table = pd.DataFrame(data,changes,first_row)

print('\n')
print('\n')
print(table)
print('\n')
print('Stessa squadra che vince entrambe le classifiche: %d (%d%%).'\
      % (vincitore_coincide, round((vincitore_coincide/num_leghe)*100,1)))
#print('\n')
print('Ultimo in somma punti che vince la classifica a scontri diretti: %d'\
      '(%d%%).' % (ultimo_vince, round((ultimo_vince/num_leghe)*100,1)))
    
    
    
    