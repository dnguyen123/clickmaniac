import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.campaign import Campaign
from facebookads import objects
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.targetingsearch import TargetingSearch
from facebookads.adobjects.adimage import AdImage
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.adcreativelinkdata import AdCreativeLinkData
from facebookads.adobjects.adcreativeobjectstoryspec \
    import AdCreativeObjectStorySpec
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.customaudience import CustomAudience


my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
my_access_token = 'EAAEQRPLI1TYBAETX4BT4QeumDM77p2lNqgdpbPWQfGvZCjbu4b9gtSd1yIcnLOQBWgt7KZAD8DxZAExBjlXymZAqE6LZA7PgXiakFjANfLBJbPgFHam8glqUHGKPFR2QzCubxzI1ZAqY5xzMbYvTSlZAxpVSyEF5m4ZD'
my_campaign_id = '23842782742530444'
my_ad_account_id = 'act_356288071441451'
my_page_id = '103185246428488'

def get_campaign():
    """
    Fetch your campaign
    """
    campaign = Campaign(my_campaign_id)
    pass

def get_ad_set(campaign):
    adsets = campaign.get_ad_sets()
    pass

def create_new_ad_set():
    """
    Create a new adset
    """
    adset = AdSet(parent_id=my_ad_account_id)

    pass

def create_new_ad(adset):
    pass

def create_filter_array(dict):
    pass

def remote_update(adset):
    """ Update your adset. """
    adset.remote_update(params = {"daily_budget": amount, 
                                    "status": AdSet.Status.active})
    
def get_clicks(adset):
    """ Get impressions...this could be used for anything. """
    params = {
    "fields": [
        AdsInsights.Field.unique_clicks
    ],
    "level": "ad", # maybe change this?
    "time_range": {
        "since": "2016-11-11",
        "until": "2016-11-13"
        }
    }
    # Returns an array of insights for each ad.
    clicks = set.get_insights(params = params)


if __name__ == "__main__":

    FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
    campaign = get_campaign()
    adset = get_ad_set(campaign)

    if len(adset.get_ads()) > 0:
        print ("# Ads:", len(adset.get_ads()))
    else:
        create_new_ad(adset)