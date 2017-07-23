import scrapy
import pickle

class Teams_dataSpider(scrapy.Spider):
    name = "teams_data"
    
    def start_requests(self):
        urls = [
            'http://leghe.fantagazzetta.com/fantascandalo/calendario',
            'http://leghe.fantagazzetta.com/fantascandalo/squadre',
            'http://leghe.fantagazzetta.com/fantascandalo/tutte-le-rose'
            ]
        
        for url in urls:
            if 'calendario' in url:
                yield scrapy.Request(url=url, callback=self.parse_points)
                
            elif 'squadre' in url:
                yield scrapy.Request(url=url, callback=self.parse_teams)
                
            elif 'tutte-le-rose' in url:
                yield scrapy.Request(url=url, callback=self.parse_players)
        
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
            
        f = open('points,fantateams,players.pckl', 'wb')
        pickle.dump(fin_res, f)
        f.close()
        
    def parse_teams(self, response):
        
        num_of_teams = len(response.css('div.teambox'))        
        
        team_names = response.css('div.col-xs-12').css('h3::text')\
                     [1:num_of_teams+1].extract()
        
        f = open('points,fantateams,players.pckl', 'ab')
        pickle.dump(team_names, f)
        f.close()
        
    def parse_players(self, response):
        
        all_tables = response.css('div.item')
        fin_dict = {}
        
        for table in all_tables:
            
            list_of_players = []
            fantateam = table.css('h3::text').extract_first()
            
            for row in table.css('tbody').css('tr'):
                
                role = row.css('span.role::text').extract_first()
                player = row.css('span.steam::text').extract_first()
                realteam = row.css('td.aleft::text').extract_first()
                price = row.css('td.pt::text').extract()[1]
                
                result = (role,player,realteam,price)
                
                list_of_players.append(result)
                
            fin_dict[fantateam] = list_of_players
            
        f = open('points,fantateams,players.pckl', 'ab')
        pickle.dump(fin_dict, f)
        f.close()
                
                
                
            
            
            
