'''
Created on Dec 9, 2016
            
Output:     heroes_id_name.json heroes_name_portrait.json

@author: journeycheng
'''

import dota2api
import settings
import json



def get_heroes_info():
    api_key = settings.api_key
    api = dota2api.Initialise(api_key)

    heroes_id_name = open('heroes_id_name.json', 'w')
    heroes_name_portrait = open('heroes_name_portrait.json', 'w')

    heroes_info_details = api.get_heroes()
    if heroes_info_details['heroes']:
        for item in heroes_info_details['heroes']:

            heroes_id_name.write(json.dumps({item['id']: item['localized_name']}) + '\n')
            heroes_name_portrait.write(json.dumps({item['localized_name']: {'full': item['url_full_portrait'], 'small': item['url_small_portrait'], 
                                                   'large':item['url_large_portrait'], 'vertical': item['url_vertical_portrait']}}) + '\n')

    heroes_id_name.close()
    heroes_name_portrait.close()

    print 'Get all heroes info succeed.'

get_heroes_info()