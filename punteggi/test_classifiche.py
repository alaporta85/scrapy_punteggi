import pickle
import pandas as pd

f = open('prova_classifiche.pckl', 'rb')
tutte_le_leghe = pickle.load(f)
f.close()

num_leghe = len(tutte_le_leghe)
zerocambi = 0
uncambio = 0
duecambi = 0
trecambi = 0
quattrocambi = 0
cinquecambi = 0
#==============================================================================
# seicambi = 0
# settecambi = 0
# ottocambi = 0
#==============================================================================
oltre5 = 0

for lega in tutte_le_leghe:
    
    cambi = 0
    
    class_SD = [row[0] for row in tutte_le_leghe[lega][0]]
    class_SP = [row[0] for row in tutte_le_leghe[lega][1]]
    
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
data = [(i, (i/num_leghe)*100) for i in results]

table = pd.DataFrame(data,changes,first_row)
print(table)
    
    
    
    