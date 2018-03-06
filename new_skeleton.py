import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads import adobjects
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet

my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAETX4BT4QeumDM77p2lNqgdpbPWQfGvZCjbu4b9gtSd1yIcnLOQBWgt7KZAD8DxZAExBjlXymZAqE6LZA7PgXiakFjANfLBJbPgFHam8glqUHGKPFR2QzCubxzI1ZAqY5xzMbYvTSlZAxpVSyEF5m4ZD'
my_campaign_id = '23842782742530444'
my_ad_account_id = 'act_356288071441451'
my_page_id = '103185246428488'

def get_campaign():
    """
    Fetching your campaign
    """
    campaign = Campaign(my_campaign_id)
    campaign.remote_read(fields=[Campaign.Field.name, Campaign.Field.objective])
    assert campaign[Campaign.Field.name] == 'my_man_joon_SDK'
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
    adset = AdSet(parent_id=my_ad_account_id)
    
    """
    Create and update your ad set here
    """
    return adset

            

if __name__ == "__main__":
    # FacebookAdsApi setup
    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

    # Fetching campaign
    campaign = get_campaign()

    adset = get_ad_set(campaign)

    # Creating a new ad set
    if len(adset.get_ads()) > 0:
        print("# Ads:", len(adset.get_ads()))
    else:
        create_new_ad_set(adset)