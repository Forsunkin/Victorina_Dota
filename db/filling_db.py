import json
import requests

url_public = 'https://api.opendota.com/api/publicMatches'
url_match_id = 'https://api.opendota.com/api/matches/'
test_str = {'match_id': 6639990211, 'player_slot': 0, 'ability_targets': None, 'ability_upgrades_arr': [5044, 5046, 5046, 5045, 5044, 5047, 5044, 5044, 5046, 6366, 5046, 5047], 'ability_uses': None, 'account_id': None, 'actions': None, 'additional_units': None, 'assists': 11, 'backpack_0': 8, 'backpack_1': 0, 'backpack_2': 0, 'backpack_3': None, 'buyback_log': None, 'camps_stacked': None, 'connection_log': None, 'creeps_stacked': None, 'damage': None, 'damage_inflictor': None, 'damage_inflictor_received': None, 'damage_taken': None, 'damage_targets': None, 'deaths': 1, 'denies': 5, 'dn_t': None, 'firstblood_claimed': None, 'gold': 1111, 'gold_per_min': 374, 'gold_reasons': None, 'gold_spent': 6220, 'gold_t': None, 'hero_damage': 6380, 'hero_healing': 195, 'hero_hits': None, 'hero_id': 26, 'item_0': 223, 'item_1': 214, 'item_2': 188, 'item_3': 34, 'item_4': 218, 'item_5': 240, 'item_neutral': 840, 'item_uses': None, 'kill_streaks': None, 'killed': None, 'killed_by': None, 'kills': 2, 'kills_log': None, 'lane_pos': None, 'last_hits': 38, 'leaver_status': 0, 'level': 12, 'lh_t': None, 'life_state': None, 'max_hero_hit': None, 'multi_kills': None, 'net_worth': 6586, 'obs': None, 'obs_left_log': None, 'obs_log': None, 'obs_placed': None, 'party_id': 0, 'party_size': 1, 'performance_others': None, 'permanent_buffs': [{'permanent_buff': 7, 'stack_count': 3}], 'pings': None, 'pred_vict': None, 'purchase': None, 'purchase_log': None, 'randomed': None, 'repicked': None, 'roshans_killed': None, 'rune_pickups': None, 'runes': None, 'runes_log': None, 'sen': None, 'sen_left_log': None, 'sen_log': None, 'sen_placed': None, 'stuns': None, 'teamfight_participation': None, 'times': None, 'tower_damage': 3174, 'towers_killed': None, 'xp_per_min': 421, 'xp_reasons': None, 'xp_t': None, 'radiant_win': True, 'start_time': 1656502885, 'duration': 1085, 'cluster': 187, 'lobby_type': 7, 'game_mode': 22, 'is_contributor': False, 'patch': 50, 'region': 8, 'isRadiant': True, 'win': 1, 'lose': 0, 'total_gold': 6763, 'total_xp': 7613, 'kills_per_min': 0.11059907834101383, 'kda': 6, 'abandons': 0, 'rank_tier': None, 'cosmetics': [], 'benchmarks': {'gold_per_min': {'raw': 374, 'pct': 0.8481906443071492}, 'xp_per_min': {'raw': 421, 'pct': 0.3406884377758164}, 'kills_per_min': {'raw': 0.11059907834101382, 'pct': 0.46072374227714036}, 'last_hits_per_min': {'raw': 2.1013824884792625, 'pct': 0.8737864077669902}, 'hero_damage_per_min': {'raw': 352.8110599078341, 'pct': 0.7030008826125331}, 'hero_healing_per_min': {'raw': 10.783410138248847, 'pct': 0.9342453662842012}, 'tower_damage': {'raw': 3174, 'pct': 0.9810238305383936}, 'stuns_per_min': {'raw': 0, 'pct': 0}, 'lhten': {}}}

def get_public_matches():
    re = requests.get(url_public)
    for match in re.json():
        if match['game_mode'] == 22 and match['lobby_type'] == 7:
            get_players_info(match)


def get_players_info(obj):
   data = requests.get(url_match_id + str(obj['match_id'])).json()   #возвращает строку с данными нужного матча
   for player in data['players']:
       if player['win'] == 1 and player['abandons'] == 0:
           post_into_table(player)


def post_into_table(obj):
    match_id = obj['match_id']
    hero_id = obj['hero_id']
    dict = {}
    for n in range(6):
        try:
            item = obj[f'item_{n}']
        except KeyError:
            item = None
        dict.update({f'item{n}': item})
    print(dict)



post_into_table(test_str)
# get_public_matches()