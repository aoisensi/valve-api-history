import os
import urllib.request
import urllib.error
import time
import json
import sys

paths = [
    'IEconDota2_570/GetHeroes/v1',
    'IEconDota2_570/GetGameItems/v1',
    'IEconDota2_570/GetRarities/v1',
    'IEconItems_440/GetSchemaItems/v1',
    'IEconItems_440/GetSchemaOverview/v1',
    'IEconItems_440/GetSchemaURL/v1',
    'IEconItems_620/GetSchema/v1',
    # 'IEconItems_730/GetSchema/v2',
    'IEconItems_730/GetStoreMetaData/v1',
    'ISteamWebAPIUtil/GetSupportedAPIList/v1',
]

key = os.getenv('STEAM_API_KEY')
headers = {'User-Agent': 'https://github.com/aoisensi/valve-api-history'}

os.makedirs('./histories', exist_ok=True)

for path in paths:
    print(path)
    try:
        url = f'https://api.steampowered.com/{path}?key={key}'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.dumps(json.load(resp), indent=2)
            sp = path.split('/')
            name = f'./histories/{sp[0]}-{sp[1]}.json'
            with open(name, mode='w') as f:
                f.write(data)
            print(name)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print('Not Found')
        else:
            print('Error:', e)
            sys.exit(1)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
    finally:
        time.sleep(5)
