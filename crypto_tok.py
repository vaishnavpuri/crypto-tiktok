from TikTokApi import TikTokApi
from playwright.sync_api import sync_playwright
___author____ = "vaishnav puri"

api =  TikTokApi.get_instance()

init_list = ['bitboycrypto', 'cryptocita', 'virtualbacon', 'cryptokang']
seed_ids = [api.get_user(user_name)['userInfo']['user']['id']for user_name in init_list]
suggest = [api.get_recommended_tiktoks_by_video_id(startingId=s_id, count=20) for s_id in seed_ids]

for i in range(len(suggest)):
    print("\nSeed: {}".format(init_list[i]))
    for u in suggest[i]:
        print('{} ({}, {} fans)'.format(u['subTitle'], u['title'], u['extraInfo']['fans']))
