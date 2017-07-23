import scrapy
import pickle

class LegheSpider(scrapy.Spider):
    
    name = 'leghe_virgilio'
    
    start_urls = ['https://www.google.be/search?biw=1366&bih=659&gbv=2&q=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+presidente&oq=site%3Ahttp%3A%2F%2Fleghe.fantagazzetta.com%2F+presidente&gs_l=psy-ab.3...33282.34670.0.34882.10.10.0.0.0.0.149.598.7j1.8.0....0...1.1.64.psy-ab..2.0.0.K5mG29qZzFk']
    
    def parse(self, response):
        
        all_leghe = []
        
        links = response.css('cite')
        
        for link in links:
            
            text = link.css('::text').extract_first()
            
            nome_lega = text.split('/')[-2]
            
#            all_leghe.append(nome_lega)

            print(nome_lega)
            
        
        
#==============================================================================
#         next_page = response.css('td.b a.fl::attr(href)').extract_first()
#     
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#==============================================================================

            
#==============================================================================
#         f = open('leghe.pckl', 'wb')
#         pickle.dump(all_leghe, f)
#         f.close()
#==============================================================================
        

        