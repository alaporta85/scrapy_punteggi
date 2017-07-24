import scrapy
import pickle

'''Scraping dei nomi delle leghe di fantagazzetta utilizzando Bing.'''

class LegheSpider(scrapy.Spider):
    
    name = 'leghe_bing'
    
    start_urls = ['https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+home&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+ho&sc=0-39&sk=&cvid=08A9D2B716624917AFA18D49287EDBAC',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+squadre&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+squadre&sc=1-44&sk=&cvid=7C53779101854B8FBBD500FE54EE25A1',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+calendario&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-38&sk=&cvid=5D5B7819E66F48D38AB2C81238EAD52F',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+classifiche&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+cla&sc=0-40&sk=&cvid=5194802861094842818376E8DCD9D19A',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+formazioni&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+fo&sc=0-39&sk=&cvid=2D6610490897459FA592BC2F5A774F8D',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+statistiche&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=EA0397415F894204AFB13D90463D76D1',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+bacheca&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+bacheca&sc=1-44&sk=&cvid=1C25520B2B4C464BABCA5380641D0678',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+live&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-38&sk=&cvid=7FF228A98A314FC3A038D9F8545778FF',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+albo&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=D5B078D6874A4F9A9CBE1E2FE5B64C05',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+info+lega&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-38&sk=&cvid=604BEBAA585A48BE9DAD10BB746614B1',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+presidente&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+p&sc=0-38&sk=&cvid=AE1A67D52F554D9CA70E2B13EF172D2A',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+anno+di+fondazione&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+anno&sc=0-41&sk=&cvid=ED4A2F0DF44C4173B6CA2F81AD76E5B5',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+seleziona+una+competizione&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=0DF033F3931A4C3A9657DCD245193CFC',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+da+non+perdere&qs=n&form=QBRE&sp=-1&pq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+da+&sc=0-40&sk=&cvid=96B03F8476AB4CACB34732167D27DFFB',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+avvisi&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=F983E0EFFAD34938B300D78F455BC1E1',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+strumenti&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=87FE5B3941B34A2DA7D1FF16387F4C9E',
                  'https://www.bing.com/search?q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+le+pagine+facebook&qs=n&form=QBRE&sp=-1&pq=undefined&sc=0-39&sk=&cvid=EFCC1D6EB9304894A42B9E8389F04B0D']
    
    def parse(self, response):
        
        try:
            f = open('leghe.pckl', 'rb')                                       # Se il file con i nomi delle leghe è già stato
            all_leghe = pickle.load(f)                                         # creato allora lo apro e carico la variabile
            f.close()                                                          # all_leghe.
        except FileNotFoundError:
            all_leghe = []                                                     # Se il file non esiste creo la variabile. 
        
        
        links = response.css('cite')                                           # Insieme dei risultati della ricerca.
        
        for link in links:
            
            try:
                text = link.css('::text').extract_first()                      # Scarico il testo contenente il nome
                text = text.split('/')                                         # lo divido in più parti
                
                nome_lega = text[1]                                            # Il nome è in genere l'elemento con indice 1.
                
                if nome_lega not in all_leghe:                                 # Se il nome non è già presente nella lista
                    all_leghe.append(nome_lega)                                # lo aggiungo.
            
            except IndexError:                                                 # Gestisce alcuni errori durante lo scraping.
                pass
            
        f = open('leghe.pckl', 'wb')
        pickle.dump(all_leghe, f)
        f.close()            
        
        next_page = response.css('a.sb_pagN::attr(href)').extract_first()      # Definisce le pagine successive da scrapare.
    
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

            
        
        

        