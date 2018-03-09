import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads import adobjects
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData

my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
# my_access_token = 'EAAEQRPLI1TYBABYxJaOLZCBNcBWH98EtWOXTnF8VZCd4Bk1FhHn0cWrFqXMypG4T18A6Vsv40AJniyQhHt7uLxDgIe04dRxonm54ULJQY8KoWVZBr6hZBaPTpO2PcX9G5klLzqx2HATdrvZCJv2C5FsKP82juToyUS6VpZA6j73gZDZD'
my_access_token='EAAEQRPLI1TYBAJZAep79Waxr5btWUSGKWyS7vbi0rZAZAgfxBzviAZBEgZClZAsILatDwSOn1fnvOyvh12qorGB0FKV1s4XoJKa0wUSSlsCAz8GR553xdkZBjgTPpzB3flYUZByC9ZClSkX3IRH8hZCH3PuYyaS6bNWnuBP4alZAYnIVgZDZD'
my_campaign_id = '23842782742530444'
my_ad_account_id = 'act_356288071441451'
my_page_id = '103185246428488'

def get_campaign():
    """
    Fetching your campaign
    """
    campaign = Campaign(my_campaign_id)
    campaign.remote_read(fields=[Campaign.Field.name, Campaign.Field.objective])
    assert campaign[Campaign.Field.name] == 'my_man_joon SDK'
    assert campaign[Campaign.Field.objective] == Campaign.Objective.page_likes
    return campaign


def get_ad_set(campaign):
    adsets = campaign.get_ad_sets()
    
    """ 
    Check the ad set your campaign might have here
    """

    return adsets


def create_new_ad_set():
    """
    Create a new adset
    """
    ad_account = AdAccount(fbid=my_ad_account_id)
    
    """
    Create and update your ad set here
    """
#https://developers.facebook.com/docs/marketing-api/reference/ad-campaign
    params = {
        AdSet.Field.name: 'joon_SDK_competition',
        AdSet.Field.promoted_object: {
            'page_id': my_page_id,
        },
        AdSet.Field.campaign_id: my_campaign_id,
        AdSet.Field.is_autobid: True,
        AdSet.Field.start_time: 1520560800, 
        AdSet.Field.end_time: 1520701200,
        AdSet.Field.daily_budget: 200,
        AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.page_likes,
# https://developers.facebook.com/docs/marketing-api/targeting-specs
        AdSet.Field.targeting: {
            'geo_locations': {
                'countries': ['IN', 'ID'],
            },
            'age_min': 13,
            'age_max': 35,
            'flexible_spec': [
                {
            
                    'interests': [
                        {
                            'id': 6003332344237 ,
                            'name': 'Dogs',
                        },
                        {
                            'id': 6004037726009,
                            'name': 'Pets',
                        },
                        {
                            'id': 6003266061909,
                            'name': 'Food',
                        },
                        {
                            'id': 6003156370433,
                            'name': 'Cute Animals',
                        },
                        {
                            'id': 625163160959478,
                            'name': 'Adorable Animals',
                        },

                    ],
                },
            ]
        },
        AdSet.Field.status: AdSet.Status.active,
    }
    adset = ad_account.create_ad_set(params=params)



    image = AdImage(parent_id=my_ad_account_id)
    image[AdImage.Field.filename] = '/Users/deriknguyen/Desktop/CS144/clickmaniac/dog_ads/3.jpg'
    image.remote_create()

    # Output image Hash
    image_hash = image[AdImage.Field.hash]

    # First, upload the ad image that you will use in your ad creative
    # Please refer to Ad Image Create for details.

    link_data = AdCreativeLinkData()
    link_data[AdCreativeLinkData.Field.message] = '"Like" to find ways to help man\'s best friend.'
    link_data[AdCreativeLinkData.Field.name] = 'Puppy Love'
    link_data[AdCreativeLinkData.Field.link] = 'http://www.facebook.com/caltech.clickmaniac'
    link_data[AdCreativeLinkData.Field.image_hash] = image_hash

    # Then, use the image hash returned from above
    object_story_spec = AdCreativeObjectStorySpec()
    object_story_spec[AdCreativeObjectStorySpec.Field.page_id] = my_page_id
    object_story_spec[AdCreativeObjectStorySpec.Field.link_data] = link_data
    

    creative = AdCreative(parent_id='my_ad_account_id')
    # creative[AdCreative.Field.title] = 'Puppy Love'
    # creative[AdCreative.Field.body] = 'Cats are one of the deadliest local predators of birds. "Like" this post if you agree they\'re overated!'
    # creative[AdCreative.Field.link_url] = 'http://www.facebook.com/caltech.clickmaniac'
    # creative[AdCreative.Field.image_hash] = image_hash

    creative[AdCreative.Field.object_story_spec] = object_story_spec
    

    # Finally, create your ad along with ad creative.
    # Please note that the ad creative is not created independently, rather its
    # data structure is appended to the ad group
    ad = Ad(parent_id=my_ad_account_id)
    ad[Ad.Field.name] = 'joon_dog_pos_competition'
    ad[Ad.Field.adset_id] = adset[AdSet.Field.id]
    ad[Ad.Field.creative] = creative
    ad.remote_create(params={
        'status': Ad.Status.active,
    })
    return adset


if __name__ == "__main__":
    # FacebookAdsApi setup
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    # Fetching campaign
    campaign = get_campaign()

    # adset = get_ad_set(campaign)

    # # Creating a new ad set
    # if len(adset.get_ads()) > 0:
    #     print("# Ads:", len(adset.get_ads()))
    # else:
    #     create_new_ad_set(adset)
    create_new_ad_set()
    