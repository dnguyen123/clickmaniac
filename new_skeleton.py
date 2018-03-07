import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads import adobjects
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting

my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
# my_access_token = 'EAAEQRPLI1TYBABYxJaOLZCBNcBWH98EtWOXTnF8VZCd4Bk1FhHn0cWrFqXMypG4T18A6Vsv40AJniyQhHt7uLxDgIe04dRxonm54ULJQY8KoWVZBr6hZBaPTpO2PcX9G5klLzqx2HATdrvZCJv2C5FsKP82juToyUS6VpZA6j73gZDZD'
my_access_token='EAAEQRPLI1TYBALZBWA0MPO1miFhRtQRMxTdlaXClheN5nGZBmIDRne6hDVlfSGA6dwD74P4B4vEbQDcAF6rqbdJJrzyxA8rrqiKaqLQbmePvcVKd0xGjO1o9D9lIqTIFiLOi4Wo7MHYulJnCiOwcc4JX6iAt3NMY1B0kFlvSH1BFmuP2appWOqYsGAy2tVCHRnpBIqfKxJnpKY5DizzKhYExtZBCj0cV7q1VIaIywZDZD'
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
    adset = AdSet(parent_id=my_ad_account_id)
    
    """
    Create and update your ad set here
    """
#https://developers.facebook.com/docs/marketing-api/reference/ad-campaign
    params = {
        AdSet.Field.name: 'My Ad Set',
        AdSet.Field.campaign_id: my_campaign_id,
        AdSet.Field.is_autobid: TRUE,
        AdSet.Field.daily_budget: 2,
        AdSet.Field.billing_event: AdSet.BillingEvent.impressions,
        AdSet.Field.optimization_goal: AdSet.OptimizationGoal.page_likes,
# https://developers.facebook.com/docs/marketing-api/targeting-specs
        AdSet.Field.targeting: {
            Targeting.Field.geo_locations: {
                'countries': ['US'],
            },
            Targeting.Field.age_min: 15,
            Targeting.Field.age_max: 30,
            Targeting.Field.flexible_spec: {
            
                'interests': [
                    {
                        'id': ,
                        'name': ,
                    },
                    {
                        'id': ,
                        'name': ,
                    },
                ],
                'interested_in': []
            },
        },
        AdSet.Field.status: AdSet.Status.active,
    }
    adset = adset.create_ad_set(params=params)

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