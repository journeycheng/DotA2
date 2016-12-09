# DotA2

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

```json
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
[0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
```
