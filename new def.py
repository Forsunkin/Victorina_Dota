test_roles = ['Support', 'Disabler', 'Nuker', 'Durable']
roles = {'role1': None, 'role2': None, 'role3': None, 'role4': None}

def replace_roles(obj):

    for n, role in enumerate(obj):
        roles[f'role{n+1}'] = role
    return roles




replace_roles(test_roles)

# можно легче сделать
# items = {‘slot1’: None, ’slot2’: None, ’slot3: None, ’slot5’: None, ’slot6’: None}
# for n, item in enumeration(obj[1]):
#   items[f’slot{n}’] = item