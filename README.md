# DotA2

## 一、准备工作
### 1.1 安装dota2api
```linux
$ pip install dota2api
```

如果这种方式没有成功的话，可以用build source的方式

```linux
$ git clone https://github.com/joshuaduffy/dota2api/ && cd dota2api/
$ python setup.py install
```
### 1.2 申请API key
去 [Valve](https://steamcommunity.com/dev/apikey) 申请。

### 1.3 阅读dota2api 开发文档
[具体的api使用教程](http://dota2api.readthedocs.io/en/latest/index.html)

## 二、英雄信息
### 2.1 英雄id和对应的名字


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
- 信息都存储在[heroes_id_name.json](HeroesInfo/heroes_id_name.json)文件
- 获取上述信息的脚本: [heroes_info.py](HeroesInfo/heroes_info.py)

### 2.2 英雄图片

每个英雄的图片都分为small、large、full、vertical四种形式，都存放在了相应的文件夹下面。

下面显示的就是small形式: 

- ![](HeroesInfo/heroes_image/Monkey_King/monkey_king_sb.png?raw=true) [美猴王](HeroesInfo/heroes_image/Monkey_King)
- ![](HeroesInfo/heroes_image/Underlord/abyssal_underlord_sb.png?raw=true) [深渊领主](HeroesInfo/heroes_image/Underlord)
- ![](HeroesInfo/heroes_image/Arc_Warden/arc_warden_sb.png?raw=true) [天穹守望者](HeroesInfo/heroes_image/Arc_Warden)
- ![](HeroesInfo/heroes_image/Winter_Wyvern/winter_wyvern_sb.png?raw=true) [寒冬飞龙](HeroesInfo/heroes_image/Winter_Wyvern)
- ![](HeroesInfo/heroes_image/Techies/techies_sb.png?raw=true) [炸弹人](HeroesInfo/heroes_image/Techies)
- ![](HeroesInfo/heroes_image/Oracle/oracle_sb.png?raw=true) [神谕者](HeroesInfo/heroes_image/Oracle)
- ![](HeroesInfo/heroes_image/Phoenix/phoenix_sb.png?raw=true) [凤凰](HeroesInfo/heroes_image/Phoenix)
- ![](HeroesInfo/heroes_image/Terrorblade/terrorblade_sb.png?raw=true) [恐怖利刃](HeroesInfo/heroes_image/Terrorblade)
- ![](HeroesInfo/heroes_image/Earth_Spirit/earth_spirit_sb.png?raw=true) [大地之灵](HeroesInfo/heroes_image/Earth_Spirit)
- ![](HeroesInfo/heroes_image/Ember_Spirit/ember_spirit_sb.png?raw=true) [灰烬之灵](HeroesInfo/heroes_image/Ember_Spirit)
- ![](HeroesInfo/heroes_image/Legion_Commander/legion_commander_sb.png?raw=true) [军团指挥官](HeroesInfo/heroes_image/Legion_Commander)
- ![](HeroesInfo/heroes_image/Elder_Titan/elder_titan_sb.png?raw=true) [上古巨神](HeroesInfo/heroes_image/Elder_Titan)
- ![](HeroesInfo/heroes_image/Abaddon/abaddon_sb.png?raw=true) [亚巴顿](HeroesInfo/heroes_image/Abaddon)
- ![](HeroesInfo/heroes_image/Skywrath_Mage/skywrath_mage_sb.png?raw=true) [天怒法师](HeroesInfo/heroes_image/Skywrath_Mage)
- ![](HeroesInfo/heroes_image/Tusk/tusk_sb.png?raw=true) [巨牙海民](HeroesInfo/heroes_image/Tusk)
- ![](HeroesInfo/heroes_image/Bristleback/bristleback_sb.png?raw=true) [钢背兽](HeroesInfo/heroes_image/Bristleback)
- ![](HeroesInfo/heroes_image/Timbersaw/shredder_sb.png?raw=true) [伐木机](HeroesInfo/heroes_image/Timbersaw)
- ![](HeroesInfo/heroes_image/Magnus/magnataur_sb.png?raw=true) [马格纳斯](HeroesInfo/heroes_image/Magnus)
- ![](HeroesInfo/heroes_image/Centaur_Warrunner/centaur_sb.png?raw=true) [半人马战行者](HeroesInfo/heroes_image/Centaur_Warrunner)
- ![](HeroesInfo/heroes_image/Troll_Warlord/troll_warlord_sb.png?raw=true) [巨魔战将](HeroesInfo/heroes_image/Troll_Warlord)
- ![](HeroesInfo/heroes_image/Medusa/medusa_sb.png?raw=true) [美杜莎](HeroesInfo/heroes_image/Medusa)
- ![](HeroesInfo/heroes_image/Slark/slark_sb.png?raw=true) [斯拉克](HeroesInfo/heroes_image/Slark)
- ![](HeroesInfo/heroes_image/Visage/visage_sb.png?raw=true) [维萨吉](HeroesInfo/heroes_image/Visage)
- ![](HeroesInfo/heroes_image/Io/wisp_sb.png?raw=true) [小精灵](HeroesInfo/heroes_image/Io)
- ![](HeroesInfo/heroes_image/Keeper_of_the_Light/keeper_of_the_light_sb.png?raw=true) [光之守卫](HeroesInfo/heroes_image/Keeper_of_the_Light)
- ![](HeroesInfo/heroes_image/Naga_Siren/naga_siren_sb.png?raw=true) [娜迦海妖](HeroesInfo/heroes_image/Naga_Siren)
- ![](HeroesInfo/heroes_image/Nyx_Assassin/nyx_assassin_sb.png?raw=true) [司夜刺客](HeroesInfo/heroes_image/Nyx_Assassin)
- ![](HeroesInfo/heroes_image/Disruptor/disruptor_sb.png?raw=true) [干扰者](HeroesInfo/heroes_image/Disruptor)
- ![](HeroesInfo/heroes_image/Rubick/rubick_sb.png?raw=true) [拉比克](HeroesInfo/heroes_image/Rubick)
- ![](HeroesInfo/heroes_image/Undying/undying_sb.png?raw=true) [不朽尸王](HeroesInfo/heroes_image/Undying)
- ![](HeroesInfo/heroes_image/Ogre_Magi/ogre_magi_sb.png?raw=true) [食人魔法师](HeroesInfo/heroes_image/Ogre_Magi)
- ![](HeroesInfo/heroes_image/Treant_Protector/treant_sb.png?raw=true) [树精卫士](HeroesInfo/heroes_image/Treant_Protector)
- ![](HeroesInfo/heroes_image/Meepo/meepo_sb.png?raw=true) [米波](HeroesInfo/heroes_image/Meepo)
- ![](HeroesInfo/heroes_image/Chaos_Knight/chaos_knight_sb.png?raw=true) [混沌骑士](HeroesInfo/heroes_image/Chaos_Knight)
- ![](HeroesInfo/heroes_image/Lone_Druid/lone_druid_sb.png?raw=true) [德鲁伊](HeroesInfo/heroes_image/Lone_Druid)
- ![](HeroesInfo/heroes_image/Shadow_Demon/shadow_demon_sb.png?raw=true) [暗影夜魔](HeroesInfo/heroes_image/Shadow_Demon)
- ![](HeroesInfo/heroes_image/Brewmaster/brewmaster_sb.png?raw=true) [酒仙](HeroesInfo/heroes_image/Brewmaster)
- ![](HeroesInfo/heroes_image/Lycan/lycan_sb.png?raw=true) [狼人](HeroesInfo/heroes_image/Lycan)
- ![](HeroesInfo/heroes_image/Outworld_Devourer/obsidian_destroyer_sb.png?raw=true) [殁境神蚀者](HeroesInfo/heroes_image/Outworld_Devourer)
- ![](HeroesInfo/heroes_image/Silencer/silencer_sb.png?raw=true) [沉默术士](HeroesInfo/heroes_image/Silencer)
- ![](HeroesInfo/heroes_image/Invoker/invoker_sb.png?raw=true) [祈求者](HeroesInfo/heroes_image/Invoker)
- ![](HeroesInfo/heroes_image/Alchemist/alchemist_sb.png?raw=true) [炼金术士](HeroesInfo/heroes_image/Alchemist)
- ![](HeroesInfo/heroes_image/Gyrocopter/gyrocopter_sb.png?raw=true) [矮人直升机](HeroesInfo/heroes_image/Gyrocopter)
- ![](HeroesInfo/heroes_image/Spirit_Breaker/spirit_breaker_sb.png?raw=true) [裂魂人](HeroesInfo/heroes_image/Spirit_Breaker)
- ![](HeroesInfo/heroes_image/Ursa/ursa_sb.png?raw=true) [熊战士](HeroesInfo/heroes_image/Ursa)
- ![](HeroesInfo/heroes_image/Ancient_Apparition/ancient_apparition_sb.png?raw=true) [远古冰魄](HeroesInfo/heroes_image/Ancient_Apparition)
- ![](HeroesInfo/heroes_image/Doom/doom_bringer_sb.png?raw=true) [末日使者](HeroesInfo/heroes_image/Doom)
- ![](HeroesInfo/heroes_image/Spectre/spectre_sb.png?raw=true) [幽鬼](HeroesInfo/heroes_image/Spectre)
- ![](HeroesInfo/heroes_image/Chen/chen_sb.png?raw=true) [陈](HeroesInfo/heroes_image/Chen)
- ![](HeroesInfo/heroes_image/Batrider/batrider_sb.png?raw=true) [蝙蝠骑士](HeroesInfo/heroes_image/Batrider)
- ![](HeroesInfo/heroes_image/Jakiro/jakiro_sb.png?raw=true) [杰奇洛](HeroesInfo/heroes_image/Jakiro)
- ![](HeroesInfo/heroes_image/Weaver/weaver_sb.png?raw=true) [编织者](HeroesInfo/heroes_image/Weaver)
- ![](HeroesInfo/heroes_image/Bounty_Hunter/bounty_hunter_sb.png?raw=true) [赏金猎人](HeroesInfo/heroes_image/Bounty_Hunter)
- ![](HeroesInfo/heroes_image/Broodmother/broodmother_sb.png?raw=true) [育母蜘蛛](HeroesInfo/heroes_image/Broodmother)
- ![](HeroesInfo/heroes_image/Night_Stalker/night_stalker_sb.png?raw=true) [暗夜魔王](HeroesInfo/heroes_image/Night_Stalker)
- ![](HeroesInfo/heroes_image/Huskar/huskar_sb.png?raw=true) [哈斯卡](HeroesInfo/heroes_image/Huskar)
- ![](HeroesInfo/heroes_image/Enchantress/enchantress_sb.png?raw=true) [魅惑魔女](HeroesInfo/heroes_image/Enchantress)
- ![](HeroesInfo/heroes_image/Omniknight/omniknight_sb.png?raw=true) [全能骑士](HeroesInfo/heroes_image/Omniknight)
- ![](HeroesInfo/heroes_image/Clinkz/clinkz_sb.png?raw=true) [克林克兹](HeroesInfo/heroes_image/Clinkz)
- ![](HeroesInfo/heroes_image/Dark_Seer/dark_seer_sb.png?raw=true) [黑暗贤者](HeroesInfo/heroes_image/Dark_Seer)
- ![](HeroesInfo/heroes_image/Lifestealer/life_stealer_sb.png?raw=true) [噬魂鬼](HeroesInfo/heroes_image/Lifestealer)
- ![](HeroesInfo/heroes_image/Nature's_Prophet/furion_sb.png?raw=true) [先知](HeroesInfo/heroes_image/Nature's_Prophet)
- ![](HeroesInfo/heroes_image/Leshrac/leshrac_sb.png?raw=true) [拉席克](HeroesInfo/heroes_image/Leshrac)
- ![](HeroesInfo/heroes_image/Clockwerk/rattletrap_sb.png?raw=true) [发条技师](HeroesInfo/heroes_image/Clockwerk)
- ![](HeroesInfo/heroes_image/Dazzle/dazzle_sb.png?raw=true) [戴泽](HeroesInfo/heroes_image/Dazzle)
- ![](HeroesInfo/heroes_image/Dragon_Knight/dragon_knight_sb.png?raw=true) [龙骑士](HeroesInfo/heroes_image/Dragon_Knight)
- ![](HeroesInfo/heroes_image/Luna/luna_sb.png?raw=true) [露娜](HeroesInfo/heroes_image/Luna)
- ![](HeroesInfo/heroes_image/Earthshaker/earthshaker_sb.png?raw=true) [撼地者](HeroesInfo/heroes_image/Earthshaker)
- ![](HeroesInfo/heroes_image/Viper/viper_sb.png?raw=true) [冥界亚龙](HeroesInfo/heroes_image/Viper)
- ![](HeroesInfo/heroes_image/Templar_Assassin/templar_assassin_sb.png?raw=true) [圣堂刺客](HeroesInfo/heroes_image/Templar_Assassin)
- ![](HeroesInfo/heroes_image/Pugna/pugna_sb.png?raw=true) [帕格纳](HeroesInfo/heroes_image/Pugna)
- ![](HeroesInfo/heroes_image/Phantom_Assassin/phantom_assassin_sb.png?raw=true) [幻影刺客](HeroesInfo/heroes_image/Phantom_Assassin)
- ![](HeroesInfo/heroes_image/Death_Prophet/death_prophet_sb.png?raw=true) [死亡先知](HeroesInfo/heroes_image/Death_Prophet)
- ![](HeroesInfo/heroes_image/Wraith_King/skeleton_king_sb.png?raw=true) [骷髅王](HeroesInfo/heroes_image/Wraith_King)
- ![](HeroesInfo/heroes_image/Faceless_Void/faceless_void_sb.png?raw=true) [虚空假面](HeroesInfo/heroes_image/Faceless_Void)
- ![](HeroesInfo/heroes_image/Juggernaut/juggernaut_sb.png?raw=true) [主宰](HeroesInfo/heroes_image/Juggernaut)
- ![](HeroesInfo/heroes_image/Venomancer/venomancer_sb.png?raw=true) [剧毒术士](HeroesInfo/heroes_image/Venomancer)
- ![](HeroesInfo/heroes_image/Queen_of_Pain/queenofpain_sb.png?raw=true) [痛苦女王](HeroesInfo/heroes_image/Queen_of_Pain)
- ![](HeroesInfo/heroes_image/Beastmaster/beastmaster_sb.png?raw=true) [兽王](HeroesInfo/heroes_image/Beastmaster)
- ![](HeroesInfo/heroes_image/Warlock/warlock_sb.png?raw=true) [术士](HeroesInfo/heroes_image/Warlock)
- ![](HeroesInfo/heroes_image/Necrophos/necrolyte_sb.png?raw=true) [瘟疫法师](HeroesInfo/heroes_image/Necrophos)
- ![](HeroesInfo/heroes_image/Sniper/sniper_sb.png?raw=true) [狙击手](HeroesInfo/heroes_image/Sniper)
- ![](HeroesInfo/heroes_image/Tinker/tinker_sb.png?raw=true) [修补匠](HeroesInfo/heroes_image/Tinker)
- ![](HeroesInfo/heroes_image/Enigma/enigma_sb.png?raw=true) [谜团](HeroesInfo/heroes_image/Enigma)
- ![](HeroesInfo/heroes_image/Riki/riki_sb.png?raw=true) [力丸](HeroesInfo/heroes_image/Riki)
- ![](HeroesInfo/heroes_image/Witch_Doctor/witch_doctor_sb.png?raw=true) [巫医](HeroesInfo/heroes_image/Witch_Doctor)
- ![](HeroesInfo/heroes_image/Tidehunter/tidehunter_sb.png?raw=true) [潮汐猎人](HeroesInfo/heroes_image/Tidehunter)
- ![](HeroesInfo/heroes_image/Slardar/slardar_sb.png?raw=true) [斯拉达](HeroesInfo/heroes_image/Slardar)
- ![](HeroesInfo/heroes_image/Shadow_Shaman/shadow_shaman_sb.png?raw=true) [暗影萨满](HeroesInfo/heroes_image/Shadow_Shaman)
- ![](HeroesInfo/heroes_image/Lion/lion_sb.png?raw=true) [莱恩](HeroesInfo/heroes_image/Lion)
- ![](HeroesInfo/heroes_image/Lich/lich_sb.png?raw=true) [巫妖](HeroesInfo/heroes_image/Lich)
- ![](HeroesInfo/heroes_image/Kunkka/kunkka_sb.png?raw=true) [昆卡](HeroesInfo/heroes_image/Kunkka)
- ![](HeroesInfo/heroes_image/Zeus/zuus_sb.png?raw=true) [宙斯](HeroesInfo/heroes_image/Zeus)
- ![](HeroesInfo/heroes_image/Lina/lina_sb.png?raw=true) [丽娜](HeroesInfo/heroes_image/Lina)
- ![](HeroesInfo/heroes_image/Windranger/windrunner_sb.png?raw=true) [风行者](HeroesInfo/heroes_image/Windranger)
- ![](HeroesInfo/heroes_image/Vengeful_Spirit/vengefulspirit_sb.png?raw=true) [复仇之魂](HeroesInfo/heroes_image/Vengeful_Spirit)
- ![](HeroesInfo/heroes_image/Tiny/tiny_sb.png?raw=true) [小小](HeroesInfo/heroes_image/Tiny)
- ![](HeroesInfo/heroes_image/Sven/sven_sb.png?raw=true) [斯温](HeroesInfo/heroes_image/Sven)
- ![](HeroesInfo/heroes_image/Storm_Spirit/storm_spirit_sb.png?raw=true) [风暴之灵](HeroesInfo/heroes_image/Storm_Spirit)
- ![](HeroesInfo/heroes_image/Sand_King/sand_king_sb.png?raw=true) [沙王](HeroesInfo/heroes_image/Sand_King)
- ![](HeroesInfo/heroes_image/Razor/razor_sb.png?raw=true) [剃刀](HeroesInfo/heroes_image/Razor)
- ![](HeroesInfo/heroes_image/Bloodseeker/bloodseeker_sb.png?raw=true) [嗜血狂魔](HeroesInfo/heroes_image/Bloodseeker)
- ![](HeroesInfo/heroes_image/Pudge/pudge_sb.png?raw=true) [帕吉](HeroesInfo/heroes_image/Pudge)
- ![](HeroesInfo/heroes_image/Puck/puck_sb.png?raw=true) [帕克](HeroesInfo/heroes_image/Puck)
- ![](HeroesInfo/heroes_image/Axe/axe_sb.png?raw=true) [斧王](HeroesInfo/heroes_image/Axe)
- ![](HeroesInfo/heroes_image/Phantom_Lancer/phantom_lancer_sb.png?raw=true) [幻影长矛手](HeroesInfo/heroes_image/Phantom_Lancer)
- ![](HeroesInfo/heroes_image/Morphling/morphling_sb.png?raw=true) [变体精灵](HeroesInfo/heroes_image/Morphling)
- ![](HeroesInfo/heroes_image/Anti-Mage/antimage_sb.png?raw=true) [敌法师](HeroesInfo/heroes_image/Anti-Mage)
- ![](HeroesInfo/heroes_image/Shadow_Fiend/nevermore_sb.png?raw=true) [影魔](HeroesInfo/heroes_image/Shadow_Fiend)
- ![](HeroesInfo/heroes_image/Mirana/mirana_sb.png?raw=true) [米拉娜](HeroesInfo/heroes_image/Mirana)
- ![](HeroesInfo/heroes_image/Drow_Ranger/drow_ranger_sb.png?raw=true) [卓尔游侠](HeroesInfo/heroes_image/Drow_Ranger)
- ![](HeroesInfo/heroes_image/Crystal_Maiden/crystal_maiden_sb.png?raw=true) [水晶室女](HeroesInfo/heroes_image/Crystal_Maiden)
- ![](HeroesInfo/heroes_image/Bane/bane_sb.png?raw=true) [祸乱之源](HeroesInfo/heroes_image/Bane)


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
