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
my_access_token='EAAEQRPLI1TYBAHPzz6epdlTckxZAWVrfbHvvv51gscjeP4ZCqZCTdtmJ6s7tZAAjJ8icTjxLOwQ3Dab1916ZC2HL9ZCEvdMj011sYZAVrTe0dEK86lanR7PH3AmqWoA7Eg4wMBeOmZBUskcVGcJThu2sswblVStOZCW7uwb4CiGQHDQZDZD'
my_ad_account_id = 'act_356288071441451'
my_page_id = '103185246428488'

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

params = {
    'q': 'Cute Animals',
    'type': 'adinterest',
}

resp = TargetingSearch.search(params=params)
print(resp)