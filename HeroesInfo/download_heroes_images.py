'''
Created on Dec 16, 2016
            
Output:     directory containing each heroes images

@author: journeycheng
'''


import json
import os
import urllib


def download_images(filename):
    url_file = open(filename, 'r')
    for line in url_file:
        line = json.loads(line.strip())
        hero_name = line.keys()[0].replace(' ', '_')

        if not os.path.exists('heroes_image/' + hero_name):
            os.makedirs('heroes_image/' + hero_name)

        for url in line.values()[0].values():
            image_name = url[url.rfind('/')+1:]
            urllib.urlretrieve(url, 'heroes_image/'+hero_name+'/'+image_name)

    url_file.close()

    print 'get all images.'



download_images('heroes_name_portrait.json')