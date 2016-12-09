'''
Created on Dec 9, 2016

Input:      inX: match_id file
            
Output:     the most popular class label

@author: journeycheng
'''


import dota2api
import settings
import json


def get_match_details(matchId):
    api_key = settings.api_key
    api = dota2api.Initialise(api_key)
    match = api.get_match_details(match_id = matchId)
    if match:
        info_radiant = {}
        info_dire = {}

        info_radiant['id'] = matchId
        info_radiant['side'] = 'radiant'
        info_radiant['team'] = match['radiant_name']

        info_dire['id'] = matchId
        info_dire['side'] = 'dire'
        info_dire['team'] = match['dire_name']

        if match['radiant_win']:
            info_radiant['state'] = 'win'
            info_dire['state'] = 'lose'
        else:
            info_radiant['state'] = 'lose'
            info_dire['state'] = 'win'


        info_radiant['bans'] =[]
        info_radiant['picks'] = []   # 'id': id, 'damage': damage, 'kill_num': kill, 'die_num: die
        info_dire['bans'] = []
        info_dire['picks'] =[]


        picks_bans_info = match['picks_bans']    # bp info
        for item in picks_bans_info:
            if item['team'] == 1 and item['is_pick'] == False:
                info_dire['bans'].append(item['hero_id'])
            elif item['team'] == 1 and item['is_pick'] == True:
                info_dire['picks'].append(item['hero_id'])
            elif item['team'] == 0 and item['is_pick'] == False:
                info_radiant['bans'].append(item['hero_id'])
            elif item['team'] == 0 and item['is_pick'] == True:
                info_radiant['picks'].append(item['hero_id'])

        info_radiant['players'] = []
        info_dire['players'] = []

        players_info = match['players']
        for item in players_info:
            if item['hero_id'] in info_radiant['picks']:
                info_radiant['players'].append({item['hero_id']: {'account_id': item['account_id'], 'kills': item['kills'], 'deaths': item['deaths'], 
                                                                  'assists': item['assists'], 'hero_damage': item['hero_damage'], 'gold_per_min': item['gold_per_min'], 'xp_per_min': item['xp_per_min']}})
            elif item['hero_id'] in info_dire['picks']:
                info_dire['players'].append({item['hero_id']: {'account_id': item['account_id'], 'kills': item['kills'], 'deaths': item['deaths'], 
                                                               'assists': item['assists'], 'hero_damage': item['hero_damage'], 'gold_per_min': item['gold_per_min'], 'xp_per_min': item['xp_per_min']}})

        return info_radiant, info_dire




match_id_file = open(settings.match_id_file, 'r')
match_info_file = open(settings.match_info_file, 'w')
for line in match_id_file:
    info_radiant, info_dire = get_match_details(int(line.strip()))
    # print info_radiant
    match_info_file.write(json.dumps(info_radiant) + '\n')
    match_info_file.write(json.dumps(info_dire) + '\n')

match_info_file.close()
match_id_file.close()
print 'Get Boston Major match info succeed.'

