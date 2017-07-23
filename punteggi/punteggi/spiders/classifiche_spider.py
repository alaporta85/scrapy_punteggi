import scrapy
import pickle

class ClassificheSpider(scrapy.Spider):
    
    handle_httpstatus_list = [400]
    
    name = 'classifiche'
    
    f = open('1690leghe.pckl', 'rb')
    leghe = pickle.load(f)
    f.close()

#    leghe = ['fantasunhopeless']    
        
    start_urls = ['http://leghe.fantagazzetta.com/%s/classifica'
                  % lega for lega in leghe]
        
    def parse(self, response):
        
        nome_lega = str(response).split('/')[-2]
        
        if nome_lega != 'leghe.fantagazzetta.com':

            table = []
            rows = response.css('table').css('tbody').css('tr')
            
            if len(rows) > 0 and len(rows[0].css('td')) == 11:
            
                for row in rows:
                    
                    fantateam = row.css('td')[1].css('a::text').extract_first()
                    pt = int(row.css('td')[2].css('::text').extract_first())
                    g = int(row.css('td')[3].css('::text').extract_first())
                    v = int(row.css('td')[4].css('::text').extract_first())
                    n = int(row.css('td')[5].css('::text').extract_first())
                    p = int(row.css('td')[6].css('::text').extract_first())
                    gf = int(row.css('td')[7].css('::text').extract_first())
                    gs = int(row.css('td')[8].css('::text').extract_first())
                    dr = int(row.css('td')[9].css('::text').extract_first())
                    tot = row.css('td')[10].css('::text').extract_first()
                    tot = float(tot.replace(',','.'))
                    
                    fin_tup = (fantateam,pt,g,v,n,p,gf,gs,dr,tot)
                    
                    table.append(fin_tup)
                
                try:
                    f = open('classifiche.pckl', 'rb')
                    all_tables = pickle.load(f)
                    f.close()
                    all_tables[nome_lega] = table
                    f = open('classifiche.pckl', 'wb')
                    pickle.dump(all_tables, f)
                    f.close()
                    
                except FileNotFoundError:
                    all_tables = {nome_lega: table}
                    f = open('classifiche.pckl', 'wb')
                    pickle.dump(all_tables, f)
                    f.close()
            
        
        
        
        
        
        