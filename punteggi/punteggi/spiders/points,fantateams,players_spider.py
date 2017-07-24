import scrapy
import pickle

'''Scraping dal sito di fantagazzetta dei dati relativi ad ogni squadra:
   punti fatti per giornata, nomi delle squadre e rispettive rose di
   calciatori.'''

class Teams_dataSpider(scrapy.Spider):
    name = "teams_data"
    
    def start_requests(self):
        urls = [
            'http://leghe.fantagazzetta.com/fantascandalo/squadre',
            'http://leghe.fantagazzetta.com/fantascandalo/calendario',
            'http://leghe.fantagazzetta.com/fantascandalo/tutte-le-rose'
            ]
        
        for url in urls:
            if 'squadre' in url:
                yield scrapy.Request(url=url, callback=self.parse_teams)
                
            elif 'calendario' in url:
                yield scrapy.Request(url=url, callback=self.parse_points)
                
            elif 'tutte-le-rose' in url:
                yield scrapy.Request(url=url, callback=self.parse_players)
        
    def parse_teams(self, response):
        
        num_of_teams = len(response.css('div.teambox'))        
        
        team_names = response.css('div.col-xs-12').css('h3::text')\
                     [1:num_of_teams+1].extract()
        
        f = open('points,fantateams,players.pckl', 'wb')
        pickle.dump(team_names, f)
        f.close()
    
    
    def parse_points(self, response):
        
        f = open('points,fantateams,players.pckl', 'rb')
        team_names = pickle.load(f)
        f.close()
        
        fin_res = {i: [] for i in team_names}
        
        for day in response.css('div.item'):
            
            for match in day.css('td.match'):
                
                match_data = match.css('::text').extract()
                
                team1 = match_data[0]
                team2 = match_data[6]
                points1 = match_data[2]
                points2 = match_data[4]
                
                fin_res[team1].append(points1)
                fin_res[team2].append(points2)

            
        f = open('points,fantateams,players.pckl', 'ab')
        pickle.dump(fin_res, f)
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
                
                
                
            
            
            
