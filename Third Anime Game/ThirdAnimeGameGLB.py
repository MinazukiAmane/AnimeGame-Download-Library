# -*- coding: utf-8 -*-
import sys
import json
import requests
import collections
if __name__ == "__main__":
    with open('GLOBAL.md','a+') as readme:
        readme.seek(0)
        sys.stdout = readme
        stringContent=str(requests.get('http://sg-public-api.serenetia.com/api/hyp_global?game_id=4ziysqXOQ8').content,'utf-8')
        jsonFile=json.loads(readme.read().strip().strip('```'),object_pairs_hook=collections.OrderedDict)
        changed = False
        pre_download_game=None
        try:
            pre_download_game=json.loads(stringContent)['data']['pre_download_game']
        except:
            pre_download_game=""
        if jsonFile['pre_download_game']!=pre_download_game:
            jsonFile['pre_download_game']=pre_download_game
            changed=True
        latest=json.loads(stringContent)['data']
        if jsonFile['latest']!=latest:
            deprecated_packages=jsonFile['deprecated_packages']
            deprecated_packages.append(jsonFile['latest'])
            jsonFile['latest']=latest
            changed=True
        if changed:
            readme.seek(0)
            readme.truncate()
            print('```\n'+json.dumps(jsonFile,ensure_ascii=False,indent=4,separators=(',',':'))+'\n```')
