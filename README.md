# DotA2

安装dota2api
```linux
$ pip install dota2api
```

如果这种方式没有成功的话，可以用build source的方式

```linux
$ git clone https://github.com/joshuaduffy/dota2api/ && cd dota2api/
$ python setup.py install
```

去Valve申请 API Key
[链接在这里](https://steamcommunity.com/dev/apikey)


之后就可以写脚本，利用api获得很多很多的数据了。
[具体的api使用教程](http://dota2api.readthedocs.io/en/latest/index.html)

## 英雄id和对应的名字
```json
{"1": "Anti-Mage"}
{"2": "Axe"}
{"3": "Bane"}
{"4": "Bloodseeker"}
{"5": "Crystal Maiden"}
{"6": "Drow Ranger"}
{"7": "Earthshaker"}
{"8": "Juggernaut"}
{"9": "Mirana"}
{"11": "Shadow Fiend"}
{"10": "Morphling"}
...
...
```
## 2016 Boston Major
### Boston Major战队比赛信息
```json
{
    "bans": [
        33,
        70,
        73,
        75,
        45
    ],
    "picks": [
        88,
        84,
        63,
        111,
        98
    ],
    "players": [
        {
            "84": {
                "hero_damage": 3163,
                "account_id": 131237305,
                "kills": 0,
                "deaths": 6,
                "assists": 3,
                "xp_per_min": 145,
                "gold_per_min": 163
            }
        },
        {
            "88": {
                "hero_damage": 4960,
                "account_id": 221651179,
                "kills": 1,
                "deaths": 9,
                "assists": 4,
                "xp_per_min": 183,
                "gold_per_min": 187
            }
        },
        {
            "98": {
                "hero_damage": 20197,
                "account_id": 106863163,
                "kills": 4,
                "deaths": 5,
                "assists": 2,
                "xp_per_min": 426,
                "gold_per_min": 462
            }
        },
        {
            "63": {
                "hero_damage": 11266,
                "account_id": 177416702,
                "kills": 1,
                "deaths": 3,
                "assists": 4,
                "xp_per_min": 451,
                "gold_per_min": 473
            }
        },
        {
            "111": {
                "hero_damage": 2978,
                "account_id": 107081378,
                "kills": 1,
                "deaths": 6,
                "assists": 3,
                "xp_per_min": 164,
                "gold_per_min": 155
            }
        }
    ],
    "state": "lose",
    "team": "LGD-GAMING",
    "id": 2832112211,
    "side": "radiant"
}
```

将各战队使用的英雄数据提取出来，用于分析。比如像这样的
```json
{
    "pick_heroes": [
        "Nyx_Assassin",
        "Ogre_Magi",
        "Weaver",
        "Oracle",
        "Timbersaw"
    ],
    "game_result": "lose",
    "team_name": "LGD-GAMING",
    "match_id": 2832112211,
    "game_side": "radiant"
}
```
为了方便分析，把英雄名字和战队名字中的空格被替换成了下划线。


16只战队
```
[u'Team_AD_FINEM', u'Newbee', u'Evil_Geniuses', u'Team_NP', 
 u'Faceless', u'Virtus.pro', u'MVP_Phoenix', u'EHOME', 
 u'OG_Dota2', u'Digital_Chaos', u'compLexity_Gaming', u'WarriorsGaming.Unity', 
 u'LGD-GAMING', u'the_wings_gaming', u'LGD.Forever_Young', u'iG.Vitality']
```

目前已经使用了88个英雄
```python
[u'Razor', u'Legion_Commander', u'Ogre_Magi', u'Juggernaut', u'Ursa', u'Ancient_Apparition', u'Jakiro', u'Pugna', u'Tinker',
u'Omniknight', u'Undying', u'Elder_Titan', u'Abaddon', u'Dark_Seer', u'Mirana', u'Bristleback', u'Sand_King', u'Slardar',
u'Anti-Mage', u'Storm_Spirit', u'Medusa', u'Ember_Spirit', u'Queen_of_Pain', u'Enchantress', u'Riki', u'Invoker',
u'Earth_Spirit', u"Nature's_Prophet", u'Sniper', u'Witch_Doctor', u'Leshrac', u'Silencer', u'Enigma', u'Doom',
u'Spirit_Breaker', u'Alchemist', u'Batrider', u'Brewmaster', u'Dragon_Knight', u'Axe', u'Drow_Ranger', u'Shadow_Demon',
u'Clinkz', u'Venomancer', u'Naga_Siren', u'Treant_Protector', u'Morphling', u'Lion', u'Dazzle', u'Magnus', u'Pudge',
u'Centaur_Warrunner', u'Warlock', u'Sven', u'Shadow_Shaman', u'Outworld_Devourer', u'Lifestealer', u'Keeper_of_the_Light',
u'Clockwerk', u'Night_Stalker', u'Oracle', u'Phantom_Assassin', u'Earthshaker', u'Puck', u'Luna', u'Faceless_Void',
u'Shadow_Fiend', u'Disruptor', u'Timbersaw', u'Vengeful_Spirit', u'Templar_Assassin', u'Winter_Wyvern', u'Lycan',
u'Beastmaster', u'Bloodseeker', u'Bane', u'Windranger', u'Terrorblade', u'Nyx_Assassin', u'Kunkka', u'Slark', u'Weaver',
u'Bounty_Hunter', u'Visage', u'Tidehunter', u'Io', u'Chen', u'Rubick']
```
已经获取到了所有英雄的图片url地址。


将战队名称、近卫夜魇和使用的英雄作为特征，基于朴素贝叶斯分类算法
```python
>>> infoList[:10]
[u'radiant', u'LGD-GAMING', u'Nyx_Assassin', u'Ogre_Magi', u'Weaver', u'Oracle', u'Timbersaw'], 
[u'dire', u'LGD.Forever_Young', u'Batrider', u'Lifestealer', u'Disruptor', u'Dragon_Knight', u'Slardar'], 
[u'radiant', u'LGD-GAMING', u'Nyx_Assassin', u'Ogre_Magi', u'Lifestealer', u'Io', u'Shadow_Fiend'], 
[u'dire', u'LGD.Forever_Young', u'Batrider', u'Silencer', u'Juggernaut', u'Sand_King', u'Dragon_Knight'], 
[u'radiant', u'Team_AD_FINEM', u'Shadow_Demon', u'Nyx_Assassin', u'Alchemist', u'Mirana', u'Weaver'], 
[u'dire', u'Newbee', u'Batrider', u'Luna', u'Warlock', u'Timbersaw', u'Sand_King'], 
[u'radiant', u'Team_AD_FINEM', u'Batrider', u'Rubick', u'Bounty_Hunter', u'Puck', u'Morphling'], 
[u'dire', u'Newbee', u'Ogre_Magi', u'Sand_King', u'Oracle', u'Slark', u'Dragon_Knight'], 
[u'radiant', u'Team_AD_FINEM', u'Bounty_Hunter', u'Dark_Seer', u'Bane', u'Luna', u'Templar_Assassin'], 
[u'dire', u'Newbee', u'Rubick', u'Juggernaut', u'Sand_King', u'Outworld_Devourer', u'Omniknight']]

>>> resultVec
[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 
1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 
1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 
1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
```
将上面的数据分成训练集和测试集，由于数据量很小，所以只选了其中4组作为测试集。


中间的分析预测过程，下次再
```python
[u'radiant', u'MVP_Phoenix', u'Ogre_Magi', u"Nature's_Prophet", u'Drow_Ranger', u'Disruptor', u'Visage'] classified as:  0
```
![](BostonMajor/pic/mvp.png?raw=true)

预测为失败，和实际情况相同

```python
[u'dire', u'Newbee', u'Slardar', u'Rubick', u'Juggernaut', u'Treant_Protector', u'Templar_Assassin'] classified as:  1
```
![](BostonMajor/pic/newbee.png?raw=true)
预测为获胜，和实际情况相同

```python
[u'radiant', u'Virtus.pro', u'Ogre_Magi', u'Lifestealer', u'Sand_King', u'Io', u'Shadow_Fiend'] classified as:  1
```
![](BostonMajor/pic/vp.png?raw=true)
预测为成功，和实际情况相同

```python
[u'dire', u'Team_NP', u'Drow_Ranger', u'Omniknight', u'Rubick', u'Outworld_Devourer', u'Undying'] classified as:  1
```
![](BostonMajor/pic/np.png?raw=true)
预测为失败，和实际情况相反
