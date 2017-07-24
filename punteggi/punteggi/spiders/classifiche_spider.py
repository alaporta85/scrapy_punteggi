import scrapy
import pickle

class ClassificheSpider(scrapy.Spider):
    
    handle_httpstatus_list = [400]                                             # Senza questo settaggio lo scraping non
                                                                               # funziona bene: molte leghe non vengono
                                                                               # scaricate.
    name = 'classifiche'
    
    f = open('1690leghe.pckl', 'rb')                                           # Questo è il file con i nomi delle leghe di
    leghe = pickle.load(f)                                                     # fantagazzetta ottenuti con lo scraping.
    f.close()                                                                  # Sono 1690 ma non tutte sono valide.

        
    start_urls = ['http://leghe.fantagazzetta.com/%s/classifica'               # Per ogni nome di lega mi collego alla
                  % lega for lega in leghe]                                    # pagina di fantagazzetta contenente la
                                                                               # classifica di quella stessa lega.
                                                                               
    def parse(self, response):
        
        nome_lega = str(response).split('/')[-2]
        
        if nome_lega != 'leghe.fantagazzetta.com':                             # Per eliminare alcuni risultati non
                                                                               # validi dello scraping.

            table = []
            rows = response.css('table').css('tbody').css('tr')                # L'insieme delle righe, cioè le posizioni di
                                                                               # ogni squadra, che compongono la classifica.
            
            if len(rows) > 0 and len(rows[0].css('td')) == 11:                 # Queste due condizioni escludono le leghe
                                                                               # senza dati e quelle che utilizzano solo
                                                                               # la somma punti, senza scontri diretti.
                
                for row in rows:                                               # Per ogni posizione creo un tuple con:
                    
                    fantateam = row.css('td')[1].css('a::text').extract_first()# Nome squadra
                    pt = int(row.css('td')[2].css('::text').extract_first())   # Punti
                    g = int(row.css('td')[3].css('::text').extract_first())    # Partite giocate
                    v = int(row.css('td')[4].css('::text').extract_first())    # Vittorie
                    n = int(row.css('td')[5].css('::text').extract_first())    # Pareggi
                    p = int(row.css('td')[6].css('::text').extract_first())    # Sconfitte
                    gf = int(row.css('td')[7].css('::text').extract_first())   # Gol fatti
                    gs = int(row.css('td')[8].css('::text').extract_first())   # Gol subiti
                    dr = int(row.css('td')[9].css('::text').extract_first())   # Differenza reti
                    tot = row.css('td')[10].css('::text').extract_first()      # Somma punti
                    tot = float(tot.replace(',','.'))
                    
                    fin_tup = (fantateam,pt,g,v,n,p,gf,gs,dr,tot)
                    
                    table.append(fin_tup)
                
                try:
                    f = open('classifiche.pckl', 'rb')                         # Se il file è già stato creato, allora lo apro.
                    all_tables = pickle.load(f)                                # Carico il dictionary: le keys sono i nomi
                    f.close()                                                  # delle leghe mentre i values le classifiche.
                    all_tables[nome_lega] = table                              # Aggiungo i nuovi dati e salvo sul file.
                    f = open('classifiche.pckl', 'wb')
                    pickle.dump(all_tables, f)
                    f.close()
                    
                except FileNotFoundError:                                      # Se il file non è ancora stato creato (cioè
                    all_tables = {nome_lega: table}                            # solo nel caso della prima lega), allora
                    f = open('classifiche.pckl', 'wb')                         # creo la variabile e la salvo sul file.
                    pickle.dump(all_tables, f)
                    f.close()
            
        
        
        
        
        
        