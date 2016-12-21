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
#### initialising
```python
import dota2api
api = dota2.api.Initialise(API_KEY)
```

API_KEY就是前面申请的API key。

#### 开发接口
- get_match_details

```python
match = api.get_match_details(match_id)
```
match中包含的字段信息

| 字段  | 数据类型 | 说明 |
| :--: | :--: | :--: |
| -重要- | | |
| match_id  | int  | 比赛id  |
| picks_bans | list[dic] | 英雄禁选信息 |
| players | list[dic] | 玩家信息 |
| radiant_win | boolean | 近卫获胜True、False |
| radiant_team_id | int | 近卫方队伍id |
| radiant_name | string | 近卫方队伍名称 |
| radiant_captain | int | 近卫队伍队长id |
| radiant_team_complete | int | 近卫队伍人员是否完整(1、0) |
| dire_team_id  | int  | 夜魇方队伍id  |
| dire_name | string | 夜魇方队伍名称 |
| dire_captain | int | 夜魇队伍队长id |
| dire_team_complete | int | 夜魇队伍人员是否完整(1、0) |
| -可能重要- | | |
| radiant_score | int | 夜魇队伍得分 |
| tower_status_radiant | int | 近卫方建筑状态 |
| dire_score | int | *不知道如何计算的* |
| tower_status_dire | int | |
| barracks_status_radiant | int | 近卫支持数 |
| duration | int | 比赛持续时间 |
| first_blood_time | int | 一血产生时间 |
| negative_votes | int | 对比赛精彩程度的负面投票数量 |
| positive_votes | int | 对比赛精彩程度的正面投票数量 |
| -不太重要- | | |
| leagueid | int | 联赛id |
| game_mode_name | string | 对战模式 |
| engine | int | *不知道是啥* |
| start_time | int | 比赛开始时间Unix timestamp |
| match_seq_num | int | *不知道是啥* |
| game_mode | int | 对战模式对应id |
| dire_logo | int | 夜魇队伍logo id |
| flags | int | 不知道什么flag |
| pre_game_duration | int | *不知道* |
| lobby_name | string | 比赛模式 |
| lobby_type | int | 比赛模式对应id |
| cluster_name | string | 比赛的地理位置 |
| radiant_logo | int | 近卫队伍logo id |
| human_players | int | 真实玩家数量 |
| cluster | int | 比赛的服务器位置，用于比赛重启 |
| cluster_name | string | 和cluster含义相同 |


bans_picks字段包含了bp过程的完整信息



| 字段 | 数据类型 | 描述 |
| :--: | :--: | :-- : |
| team | int | 0表示近卫，1表示夜魇 |
| hero_id | int | 当前禁用或选用的英雄id |
| order | int | 当前的次序，总共20(0～19) |
| is_pick | boolean | false表示禁用，true表示选用 |


players字段包含了所有玩家的本场比赛数据


| 字段 | 数据类型 | 描述 |
| :--: | :--: | :-- : |
| hero_id | int | 英雄id |
| hero_name | string | 英雄id对应名称 |
| kills | int | 玩家击杀次数 |
| deaths | int | 死亡次数 |
| assists | int | 玩家助攻次数 |
| denies | int | 反补次数 |
| gold_spent | int | 花费金钱数 |
| gold | int | 持有金钱数 |
| hero_damage | int | 对英雄造成的伤害量
| tower_damage | int | 对塔造成的伤害量 |
| hero_healing | int | 英雄提供的治疗量 |
| gold_per_min | int | 平均每分钟的金钱数 |
| xp_per_min | int | 平均每分钟的经验值 |
| ability_upgrades | list[dic] | 技能升级路线 |
| level | int | 最终英雄等级 |
| item_# | int | 物品#(0-5)id |
| item_#_name | string | 物品#(0-5)名称 |
| backpack_# | int | 背包#(0-2)的物品id |
| 分割线 | 分割线 | 分割线 |
| account_id | int | 玩家账号id |
| player_slot | int | 玩家在队伍中的位置（实际并没有给出） |
| leaver_status | string | 玩家离开游戏状态id |
| leaver_status_name | string | 玩家离开游戏状态 |
| leaver_status_description | string | 玩家离开游戏状态对应描述 |
| scaled_hero_damage | int | |
| last_hists | int | |
| scaled_hero_healing | int | |
| scaled_tower_damage | int | |


ability_upgrade字段


| 字段 | 数据类型 | 描述 |
| :--: | :--: | :-- : |
| level | int | 英雄等级 |
| ability | int | 升级的技能id |
| time ｜ int | 升级技能的时间 |

game_mode 

| Value | Description |
| :--: | :--: |
| 0 | Unknown |
| 1 | All Pick |
| 2 | Caption's Mode |
| 3 | Random Draft |
| 4 | Single Draft |
| 5 | All Random |
| 6 | Intro |
| 7 | Diretie |
| 8 | Reverse Captain's Mode |
| 9 | The Greeviling |
| 10 | Tutotial |
| 11 | Mid Only |
| 12 | Least Played |
| 13 | New Player Pool |
| 14 | Compendium Matchmaking |
| 15 | Custom |
| 16 | Captions Draft |
| 17 | Balanced Draft |
| 18 | Ability Draft |
| 19 | Event |
| 20 | All Random Death Match |
| 21 | Solo Mid 1 vs 1 |
| 22 | Ranked All Pick |

lobby_type

| Status | Description |
| :--: | :--: |
| -1 | Invalid |
| 0 | Public matchmaking |
| 1 | Practice |
| 2 | Tournament |
| 3 | Tutorial |
| 4 | Co-op with AI |
| 5 | Team match |
| 6 | Solo queue |
| 7 | Ranked matchmaking |
| 8 | Solo Mid 1 vs 1 |


[英文原版在这里，好久没更新的样子](http://dota2api.readthedocs.io/en/latest/index.html)

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

- (1) 每个英雄的图片url信息存放在[heroes_name_portrait.json](https://github.com/journeycheng/DotA2/tree/master/HeroesInfo/heroes_name_portrait.json)文件中

每行内容形式如下，key为英雄的名字，value为url集合：
```json
{
    "Anti-Mage": {
        "small": "http://cdn.dota2.com/apps/dota2/images/heroes/antimage_sb.png",
        "large": "http://cdn.dota2.com/apps/dota2/images/heroes/antimage_lg.png",
        "full": "http://cdn.dota2.com/apps/dota2/images/heroes/antimage_full.png",
        "vertical": "http://cdn.dota2.com/apps/dota2/images/heroes/antimage_vert.jpg"
    }
}
```

- (2) 根据url下载图片的脚本[download_heroes_images.py](https://github.com/journeycheng/DotA2/tree/master/HeroesInfo/download_heroes_images.py)

- (3) 获取到的每个英雄图片分为small、large、full、vertical四种形式，分别存放在了相应的文件夹下面。

- > [所有图片的压缩包文件](https://github.com/journeycheng/DotA2/tree/master/HeroesInfo/heroes_image.zip)

- > 每个英雄的所有形式图片，下面是small的: 

- ![](HeroesInfo/heroes_image/Monkey_King/monkey_king_sb.png?raw=true)
![](HeroesInfo/heroes_image/Underlord/abyssal_underlord_sb.png?raw=true)
![](HeroesInfo/heroes_image/Arc_Warden/arc_warden_sb.png?raw=true)
![](HeroesInfo/heroes_image/Winter_Wyvern/winter_wyvern_sb.png?raw=true)
![](HeroesInfo/heroes_image/Techies/techies_sb.png?raw=true)
![](HeroesInfo/heroes_image/Oracle/oracle_sb.png?raw=true)
![](HeroesInfo/heroes_image/Phoenix/phoenix_sb.png?raw=true)
![](HeroesInfo/heroes_image/Terrorblade/terrorblade_sb.png?raw=true)

- [美猴王](HeroesInfo/heroes_image/Monkey_King)
[深渊领主](HeroesInfo/heroes_image/Underlord)
[天穹守望者](HeroesInfo/heroes_image/Arc_Warden)
[寒冬飞龙](HeroesInfo/heroes_image/Winter_Wyvern)
[炸弹人](HeroesInfo/heroes_image/Techies)
[神谕者](HeroesInfo/heroes_image/Oracle)
[凤凰](HeroesInfo/heroes_image/Phoenix)
[恐怖利刃](HeroesInfo/heroes_image/Terrorblade)

- ![](HeroesInfo/heroes_image/Earth_Spirit/earth_spirit_sb.png?raw=true)
![](HeroesInfo/heroes_image/Ember_Spirit/ember_spirit_sb.png?raw=true)
![](HeroesInfo/heroes_image/Legion_Commander/legion_commander_sb.png?raw=true)
![](HeroesInfo/heroes_image/Elder_Titan/elder_titan_sb.png?raw=true)
![](HeroesInfo/heroes_image/Abaddon/abaddon_sb.png?raw=true)
![](HeroesInfo/heroes_image/Skywrath_Mage/skywrath_mage_sb.png?raw=true)
![](HeroesInfo/heroes_image/Tusk/tusk_sb.png?raw=true)
![](HeroesInfo/heroes_image/Bristleback/bristleback_sb.png?raw=true)

- [大地之灵](HeroesInfo/heroes_image/Earth_Spirit)
[灰烬之灵](HeroesInfo/heroes_image/Ember_Spirit)
[军团指挥官](HeroesInfo/heroes_image/Legion_Commander)
[上古巨神](HeroesInfo/heroes_image/Elder_Titan)
[亚巴顿](HeroesInfo/heroes_image/Abaddon)
[天怒法师](HeroesInfo/heroes_image/Skywrath_Mage)
[巨牙海民](HeroesInfo/heroes_image/Tusk)
[钢背兽](HeroesInfo/heroes_image/Bristleback)

- ![](HeroesInfo/heroes_image/Timbersaw/shredder_sb.png?raw=true)
![](HeroesInfo/heroes_image/Magnus/magnataur_sb.png?raw=true)
![](HeroesInfo/heroes_image/Centaur_Warrunner/centaur_sb.png?raw=true)
![](HeroesInfo/heroes_image/Troll_Warlord/troll_warlord_sb.png?raw=true)
![](HeroesInfo/heroes_image/Medusa/medusa_sb.png?raw=true)
![](HeroesInfo/heroes_image/Slark/slark_sb.png?raw=true)
![](HeroesInfo/heroes_image/Visage/visage_sb.png?raw=true)
![](HeroesInfo/heroes_image/Io/wisp_sb.png?raw=true)

- [伐木机](HeroesInfo/heroes_image/Timbersaw)
[马格纳斯](HeroesInfo/heroes_image/Magnus)
[半人马战行者](HeroesInfo/heroes_image/Centaur_Warrunner)
[巨魔战将](HeroesInfo/heroes_image/Troll_Warlord)
[美杜莎](HeroesInfo/heroes_image/Medusa)
[斯拉克](HeroesInfo/heroes_image/Slark)
[维萨吉](HeroesInfo/heroes_image/Visage)
[小精灵](HeroesInfo/heroes_image/Io)

- ![](HeroesInfo/heroes_image/Keeper_of_the_Light/keeper_of_the_light_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Naga_Siren/naga_siren_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Nyx_Assassin/nyx_assassin_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Disruptor/disruptor_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Rubick/rubick_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Undying/undying_sb.png?raw=true)
![](HeroesInfo/heroes_image/Ogre_Magi/ogre_magi_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Treant_Protector/treant_sb.png?raw=true)
 
- [光之守卫](HeroesInfo/heroes_image/Keeper_of_the_Light)
[娜迦海妖](HeroesInfo/heroes_image/Naga_Siren)
[司夜刺客](HeroesInfo/heroes_image/Nyx_Assassin)
[干扰者](HeroesInfo/heroes_image/Disruptor)
[拉比克](HeroesInfo/heroes_image/Rubick)
[不朽尸王](HeroesInfo/heroes_image/Undying)
[食人魔法师](HeroesInfo/heroes_image/Ogre_Magi) 
[树精卫士](HeroesInfo/heroes_image/Treant_Protector)
 
- ![](HeroesInfo/heroes_image/Meepo/meepo_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Chaos_Knight/chaos_knight_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Lone_Druid/lone_druid_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Shadow_Demon/shadow_demon_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Brewmaster/brewmaster_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Lycan/lycan_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Outworld_Devourer/obsidian_destroyer_sb.png?raw=true) 
![](HeroesInfo/heroes_image/Silencer/silencer_sb.png?raw=true)
 
- [米波](HeroesInfo/heroes_image/Meepo)
[混沌骑士](HeroesInfo/heroes_image/Chaos_Knight)
[德鲁伊](HeroesInfo/heroes_image/Lone_Druid)
[暗影夜魔](HeroesInfo/heroes_image/Shadow_Demon)
[酒仙](HeroesInfo/heroes_image/Brewmaster)
[狼人](HeroesInfo/heroes_image/Lycan)
[殁境神蚀者](HeroesInfo/heroes_image/Outworld_Devourer)
[沉默术士](HeroesInfo/heroes_image/Silencer)
  
- ![](HeroesInfo/heroes_image/Invoker/invoker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Alchemist/alchemist_sb.png?raw=true)
![](HeroesInfo/heroes_image/Gyrocopter/gyrocopter_sb.png?raw=true)
![](HeroesInfo/heroes_image/Spirit_Breaker/spirit_breaker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Ursa/ursa_sb.png?raw=true)
![](HeroesInfo/heroes_image/Ancient_Apparition/ancient_apparition_sb.png?raw=true)
![](HeroesInfo/heroes_image/Doom/doom_bringer_sb.png?raw=true)
![](HeroesInfo/heroes_image/Spectre/spectre_sb.png?raw=true)

- [祈求者](HeroesInfo/heroes_image/Invoker)
[炼金术士](HeroesInfo/heroes_image/Alchemist)
[矮人直升机](HeroesInfo/heroes_image/Gyrocopter)
[裂魂人](HeroesInfo/heroes_image/Spirit_Breaker)
[熊战士](HeroesInfo/heroes_image/Ursa)
[远古冰魄](HeroesInfo/heroes_image/Ancient_Apparition)
[末日使者](HeroesInfo/heroes_image/Doom)
[幽鬼](HeroesInfo/heroes_image/Spectre)

- ![](HeroesInfo/heroes_image/Chen/chen_sb.png?raw=true)
![](HeroesInfo/heroes_image/Batrider/batrider_sb.png?raw=true)
![](HeroesInfo/heroes_image/Jakiro/jakiro_sb.png?raw=true)
![](HeroesInfo/heroes_image/Weaver/weaver_sb.png?raw=true)
![](HeroesInfo/heroes_image/Bounty_Hunter/bounty_hunter_sb.png?raw=true)
![](HeroesInfo/heroes_image/Broodmother/broodmother_sb.png?raw=true)
![](HeroesInfo/heroes_image/Night_Stalker/night_stalker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Huskar/huskar_sb.png?raw=true)

- [陈](HeroesInfo/heroes_image/Chen)
[蝙蝠骑士](HeroesInfo/heroes_image/Batrider)
[杰奇洛](HeroesInfo/heroes_image/Jakiro)
[编织者](HeroesInfo/heroes_image/Weaver)
[赏金猎人](HeroesInfo/heroes_image/Bounty_Hunter)
[育母蜘蛛](HeroesInfo/heroes_image/Broodmother)
[暗夜魔王](HeroesInfo/heroes_image/Night_Stalker)
[哈斯卡](HeroesInfo/heroes_image/Huskar)

- ![](HeroesInfo/heroes_image/Enchantress/enchantress_sb.png?raw=true)
![](HeroesInfo/heroes_image/Omniknight/omniknight_sb.png?raw=true)
![](HeroesInfo/heroes_image/Clinkz/clinkz_sb.png?raw=true)
![](HeroesInfo/heroes_image/Dark_Seer/dark_seer_sb.png?raw=true)
![](HeroesInfo/heroes_image/Lifestealer/life_stealer_sb.png?raw=true)
![](HeroesInfo/heroes_image/Nature's_Prophet/furion_sb.png?raw=true)
![](HeroesInfo/heroes_image/Leshrac/leshrac_sb.png?raw=true)
![](HeroesInfo/heroes_image/Clockwerk/rattletrap_sb.png?raw=true)

- [魅惑魔女](HeroesInfo/heroes_image/Enchantress)
[全能骑士](HeroesInfo/heroes_image/Omniknight)
[克林克兹](HeroesInfo/heroes_image/Clinkz)
[黑暗贤者](HeroesInfo/heroes_image/Dark_Seer)
[噬魂鬼](HeroesInfo/heroes_image/Lifestealer)
[先知](HeroesInfo/heroes_image/Nature's_Prophet)
[拉席克](HeroesInfo/heroes_image/Leshrac)
[发条技师](HeroesInfo/heroes_image/Clockwerk)

- ![](HeroesInfo/heroes_image/Dazzle/dazzle_sb.png?raw=true)
![](HeroesInfo/heroes_image/Dragon_Knight/dragon_knight_sb.png?raw=true)
![](HeroesInfo/heroes_image/Luna/luna_sb.png?raw=true)
![](HeroesInfo/heroes_image/Earthshaker/earthshaker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Viper/viper_sb.png?raw=true)
![](HeroesInfo/heroes_image/Templar_Assassin/templar_assassin_sb.png?raw=true)
![](HeroesInfo/heroes_image/Pugna/pugna_sb.png?raw=true)
![](HeroesInfo/heroes_image/Phantom_Assassin/phantom_assassin_sb.png?raw=true)

- [戴泽](HeroesInfo/heroes_image/Dazzle)
[龙骑士](HeroesInfo/heroes_image/Dragon_Knight)
[露娜](HeroesInfo/heroes_image/Luna)
[撼地者](HeroesInfo/heroes_image/Earthshaker)
[冥界亚龙](HeroesInfo/heroes_image/Viper)
[圣堂刺客](HeroesInfo/heroes_image/Templar_Assassin)
[帕格纳](HeroesInfo/heroes_image/Pugna)
[幻影刺客](HeroesInfo/heroes_image/Phantom_Assassin)

- ![](HeroesInfo/heroes_image/Death_Prophet/death_prophet_sb.png?raw=true)
![](HeroesInfo/heroes_image/Wraith_King/skeleton_king_sb.png?raw=true)
![](HeroesInfo/heroes_image/Faceless_Void/faceless_void_sb.png?raw=true)
![](HeroesInfo/heroes_image/Juggernaut/juggernaut_sb.png?raw=true)
![](HeroesInfo/heroes_image/Venomancer/venomancer_sb.png?raw=true)
![](HeroesInfo/heroes_image/Queen_of_Pain/queenofpain_sb.png?raw=true)
![](HeroesInfo/heroes_image/Beastmaster/beastmaster_sb.png?raw=true)
![](HeroesInfo/heroes_image/Warlock/warlock_sb.png?raw=true)

- [死亡先知](HeroesInfo/heroes_image/Death_Prophet)
[骷髅王](HeroesInfo/heroes_image/Wraith_King)
[虚空假面](HeroesInfo/heroes_image/Faceless_Void)
[主宰](HeroesInfo/heroes_image/Juggernaut)
[剧毒术士](HeroesInfo/heroes_image/Venomancer)
[痛苦女王](HeroesInfo/heroes_image/Queen_of_Pain)
[兽王](HeroesInfo/heroes_image/Beastmaster)
[术士](HeroesInfo/heroes_image/Warlock)

- ![](HeroesInfo/heroes_image/Necrophos/necrolyte_sb.png?raw=true)
![](HeroesInfo/heroes_image/Sniper/sniper_sb.png?raw=true)
![](HeroesInfo/heroes_image/Tinker/tinker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Enigma/enigma_sb.png?raw=true)
![](HeroesInfo/heroes_image/Riki/riki_sb.png?raw=true)
![](HeroesInfo/heroes_image/Witch_Doctor/witch_doctor_sb.png?raw=true)
![](HeroesInfo/heroes_image/Tidehunter/tidehunter_sb.png?raw=true)
![](HeroesInfo/heroes_image/Slardar/slardar_sb.png?raw=true)

- [瘟疫法师](HeroesInfo/heroes_image/Necrophos)
[狙击手](HeroesInfo/heroes_image/Sniper)
[修补匠](HeroesInfo/heroes_image/Tinker)
[谜团](HeroesInfo/heroes_image/Enigma)
[力丸](HeroesInfo/heroes_image/Riki)
[巫医](HeroesInfo/heroes_image/Witch_Doctor)
[潮汐猎人](HeroesInfo/heroes_image/Tidehunter)
[斯拉达](HeroesInfo/heroes_image/Slardar)
  
- ![](HeroesInfo/heroes_image/Shadow_Shaman/shadow_shaman_sb.png?raw=true)
![](HeroesInfo/heroes_image/Lion/lion_sb.png?raw=true)
![](HeroesInfo/heroes_image/Lich/lich_sb.png?raw=true)
![](HeroesInfo/heroes_image/Kunkka/kunkka_sb.png?raw=true)
![](HeroesInfo/heroes_image/Zeus/zuus_sb.png?raw=true)
![](HeroesInfo/heroes_image/Lina/lina_sb.png?raw=true)
![](HeroesInfo/heroes_image/Windranger/windrunner_sb.png?raw=true)
![](HeroesInfo/heroes_image/Vengeful_Spirit/vengefulspirit_sb.png?raw=true)

- [暗影萨满](HeroesInfo/heroes_image/Shadow_Shaman)
[莱恩](HeroesInfo/heroes_image/Lion)
[巫妖](HeroesInfo/heroes_image/Lich)
[昆卡](HeroesInfo/heroes_image/Kunkka)
[宙斯](HeroesInfo/heroes_image/Zeus)
[丽娜](HeroesInfo/heroes_image/Lina)
[风行者](HeroesInfo/heroes_image/Windranger)
[复仇之魂](HeroesInfo/heroes_image/Vengeful_Spirit)
 
- ![](HeroesInfo/heroes_image/Sven/sven_sb.png?raw=true)
![](HeroesInfo/heroes_image/Storm_Spirit/storm_spirit_sb.png?raw=true)
![](HeroesInfo/heroes_image/Sand_King/sand_king_sb.png?raw=true)
![](HeroesInfo/heroes_image/Razor/razor_sb.png?raw=true)
![](HeroesInfo/heroes_image/Bloodseeker/bloodseeker_sb.png?raw=true)
![](HeroesInfo/heroes_image/Pudge/pudge_sb.png?raw=true)
![](HeroesInfo/heroes_image/Puck/puck_sb.png?raw=true)
![](HeroesInfo/heroes_image/Axe/axe_sb.png?raw=true)

- [斯温](HeroesInfo/heroes_image/Sven)
[风暴之灵](HeroesInfo/heroes_image/Storm_Spirit)
[沙王](HeroesInfo/heroes_image/Sand_King)
[剃刀](HeroesInfo/heroes_image/Razor)
[嗜血狂魔](HeroesInfo/heroes_image/Bloodseeker)
[帕吉](HeroesInfo/heroes_image/Pudge)
[帕克](HeroesInfo/heroes_image/Puck)
[斧王](HeroesInfo/heroes_image/Axe)
       
- ![](HeroesInfo/heroes_image/Phantom_Lancer/phantom_lancer_sb.png?raw=true)
![](HeroesInfo/heroes_image/Morphling/morphling_sb.png?raw=true)
![](HeroesInfo/heroes_image/Anti-Mage/antimage_sb.png?raw=true)
![](HeroesInfo/heroes_image/Shadow_Fiend/nevermore_sb.png?raw=true)
![](HeroesInfo/heroes_image/Mirana/mirana_sb.png?raw=true)
![](HeroesInfo/heroes_image/Drow_Ranger/drow_ranger_sb.png?raw=true)
![](HeroesInfo/heroes_image/Crystal_Maiden/crystal_maiden_sb.png?raw=true)
![](HeroesInfo/heroes_image/Bane/bane_sb.png?raw=true)
![](HeroesInfo/heroes_image/Tiny/tiny_sb.png?raw=true)

- [幻影长矛手](HeroesInfo/heroes_image/Phantom_Lancer)
[变体精灵](HeroesInfo/heroes_image/Morphling)
[敌法师](HeroesInfo/heroes_image/Anti-Mage)
[影魔](HeroesInfo/heroes_image/Shadow_Fiend)
[米拉娜](HeroesInfo/heroes_image/Mirana)
[卓尔游侠](HeroesInfo/heroes_image/Drow_Ranger)
[水晶室女](HeroesInfo/heroes_image/Crystal_Maiden)
[祸乱之源](HeroesInfo/heroes_image/Bane)
[小小](HeroesInfo/heroes_image/Tiny)


## 三、2016 Boston Major

### 3.1 正赛match id

存放在[Boston_major_match_id.txt](https://github.com/journeycheng/DotA2/tree/master/BostonMajor/Boston_major_match_id.txt)文件中

（待添加爬取match id的程序，从dotamax上获取）

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

## 四、AF战队战绩分析

### 4.1 Boston Major黑马之旅

### 4.2 AF所有比赛数据
