# -*- coding: utf-8 -*-
import sys
import json
import requests
import collections

if __name__ == "__main__":
    with open('GLOBAL.md', 'a+') as readme:
        readme.seek(0)
        sys.stdout = readme
        stringContent = requests.get('https://sg-public-api.serenetia.com/api/hyp_global?game_id=U5hbdsT9W7').content.decode('utf-8')
        
        try:
            jsonFile = json.loads(readme.read().strip().strip('```'), object_pairs_hook=collections.OrderedDict)
        except json.JSONDecodeError:
            jsonFile = collections.OrderedDict({
                "pre_download_game": "",
                "latest": None,
                "deprecated_packages": []
            })
        
        changed = False
        
        # Get pre_download_game
        try:
            pre_download_game = json.loads(stringContent)['data']['game_packages'][0]['pre_download']
        except KeyError:
            pre_download_game = ""

        if jsonFile['pre_download_game'] != pre_download_game:
            jsonFile['pre_download_game'] = pre_download_game
            changed = True

        # Get latest game package
        try:
            game_packages = json.loads(stringContent)['data']['game_packages']
            latest = game_packages[0]['main']['major']
        except (KeyError, IndexError):
            latest = None

        if jsonFile['latest'] != latest:
            deprecated_packages = jsonFile.get('deprecated_packages', [])
            if jsonFile['latest']:
                deprecated_packages.append(jsonFile['latest'])
            jsonFile['latest'] = latest
            jsonFile['deprecated_packages'] = deprecated_packages
            changed = True

        if changed:
            readme.seek(0)
            readme.truncate()
            print('```\n' + json.dumps(jsonFile, ensure_ascii=False, indent=4, separators=(',', ':')) + '\n```')
