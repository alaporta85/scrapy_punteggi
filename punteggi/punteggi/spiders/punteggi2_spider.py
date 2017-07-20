import scrapy
import pickle


class PunteggiSpider(scrapy.Spider):
    name = "punteggi2"
    
    def start_requests(self):
    urls = [
        'http://leghe.fantagazzetta.com/fantascandalo/calendario',
        'http://leghe.fantagazzetta.com/fantascandalo/squadre'
        ]
        
    for url in urls:
        if 'calendario' in url:
            yield scrapy.Request(url=url, callback=self.parse_points)
            
        elif 'squadre' in url:
            yield scrapy.Request(url=url, callback=self.parse_teams)
        
    def parse_points(self, response):
        
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
        f.close()
        
    def parse_teams(self, response):
        
        num_of_teams = len(response.css('div.teambox'))        
        
        team_names = response.css('div.col-xs-12').css('h3::text')[1:num_of_teams+1].extract()
            
            
            
