import collections


test_match_id = ['6508700610', '6508713704', '6508737615']


dict = collections.defaultdict(lambda key: None)

for n, match in enumerate(test_match_id):
    dict[f'name{n}'] = match

print(f"match{n} = {dict.get(f'match{n}'),},{match}")