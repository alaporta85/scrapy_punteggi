import scrapy
import pickle


class PunteggiSpider(scrapy.Spider):
    name = "punteggi"
    start_urls = [
        'http://leghe.fantagazzetta.com/fantascandalo/calendario'
        ]
        
    def parse(self, response):
        
        res_punti = []
        res_teams = []
        count = 0
        
        for day in response.css('div.item'):
            
            punti = day.css('table.tbblu').css('tbody').css('td.match')\
                    .css('span.point::text').extract()
                   
            teams = day.css('table.tbblu').css('tbody').css('td.match')\
                    .css('span').css('a::text').extract()
                   
            res_punti += punti
            res_teams += teams
            
        team_names = set(res_teams)
        fin_res = {i: [] for i in team_names}
        
        for team in res_teams:
            fin_res[team].append(res_punti[count])
            count += 1
            
        f = open('points__names.pckl', 'wb')
        pickle.dump(fin_res, f)
        pickle.dump(list(team_names), f)
        f.close()
            
            
            
#==============================================================================
#             yield {
#                 'text': quote.css('span.text::text').extract_first(),
#                 'author': quote.css('small.author::text').extract_first(),
#                 'tags': quote.css('div.tags a.tag::text').extract(),
#             }
#==============================================================================
