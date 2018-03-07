import datetime
import random
import json
from facebookads.api import FacebookAdsApi
from facebookads import adobjects
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.targeting import Targeting
from facebookads.adobjects.targetingsearch import TargetingSearch
my_app_id = '299363293779254'
my_app_secret = '3ec97126104c50bed63580b6968659fa'
# my_access_token = 'EAAEQRPLI1TYBABYxJaOLZCBNcBWH98EtWOXTnF8VZCd4Bk1FhHn0cWrFqXMypG4T18A6Vsv40AJniyQhHt7uLxDgIe04dRxonm54ULJQY8KoWVZBr6hZBaPTpO2PcX9G5klLzqx2HATdrvZCJv2C5FsKP82juToyUS6VpZA6j73gZDZD'
my_access_token='EAAEQRPLI1TYBAPKhsMWhWErLkzDalIM2qrii5bV7ZCKZA7LntVSKZC6PVyTzgB08a6RFNshHUZBrCT04W2RA8YnjZAX89XuBZBO7XYkHCVvFWdvUUk8or0cmz1to6KdfTbZAWcScyk6x5pAVBgH7OYujOMOhqYmUU4Hc5ISF7MvwIGd2VXOyGqnekBdZC4rBkUtOCg5IH7WyYwZDZD'
my_campaign_id = '23842782742530444'
my_ad_account_id = 'act_356288071441451'
my_page_id = '103185246428488'

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

params = {
    'q': 'mercosur',
    'type': 'adgeolocation',
    'location_types': ['country_group'],
}

resp = TargetingSearch.search(params=params)
print(resp)