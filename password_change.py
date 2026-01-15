import requests
import requests,SignerPy
from typing import Any
import time,random
def xor(string):
    return "".join([hex(ord(c) ^ 5)[2:] for c in string])
em=input("Enter email • ")
sessionid=input("Enter sessionid • ")
url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"

params = {
  'passport-sdk-version': "6031990",
  'device_platform': "android",
  'os': "android",
  'ssmix': "a",
  '_rticket': "1768039981030",
  'cdid': "df40fed9-674e-4ecb-af0f-9ed987880397",
  'channel': "googleplay",
  'aid': "1233",
  'app_name': "musical_ly",
  'version_code': "370805",
  'version_name': "37.8.5",
  'manifest_version_code': "2023708050",
  'update_version_code': "2023708050",
  'ab_version': "37.8.5",
  'resolution': "720*1532",
  'dpi': "320",
  'device_type': "Infinix X6528",
  'device_brand': "Infinix",
  'language': "ar",
  'os_api': "33",
  'os_version': "13",
  'ac': "wifi",
  'is_pad': "0",
  'current_region': "IQ",
  'app_type': "normal",
  'sys_region': "EG",
  'last_install_time': "1767344665",
  'mcc_mnc': "41805",
  'timezone_name': "Asia/Baghdad",
  'carrier_region_v2': "418",
  'residence': "IQ",
  'app_language': "ar",
  'carrier_region': "IQ",
  'timezone_offset': "10800",
  'host_abi': "arm64-v8a",
  'locale': "ar",
  'ac2': "wifi",
  'uoo': "0",
  'op_region': "IQ",
  'build_number': "37.8.5",
  'region': "EG",
  'ts': "1768039981",
  'iid': "7590687437694387985",
  'device_id': "7590636316863038993",
  'openudid': "28d7c85d87207258",
  'support_webview': "1",
  'reg_store_region': "IQ",
  'user_selected_region': "0",
  'cronet_version': "75b93580_2024-11-28",
  'ttnet_version': "4.2.210.6-tiktok",
  'use_store_region_cookie': "1"
}
cookies = {
    "d_ticket": "c8d63dec42721bf61777f2ec6c624d8cfa298",
    "multi_sids": "7585693484708201479:6003413efe9b08b7ec72cda84ccfa3d4",
    "odin_tt": "a24f0c7e1aa868fb95e3376a4b1dad699f75d7c6b66bf4ae5771e75d68662f542ee692017568d9c0b1643258746a3e6fba2068d326546ca9d835b63f1e01375d15702ba9471025caad88878d4f543df1",
    "cmpl_token": "AgQYAPOn_hfkT7C5eyKvEzXdPvN6od3_G_-Sp2CiyPI",
    "sid_guard": "6003413efe9b08b7ec72cda84ccfa3d4|1766769054|15552000|Wed, 24-Jun-2026 17:10:54 GMT",
    "uid_tt": "ddf8b04de63523bdc247e916832f46d6ac9742465baba9672a1f84a8ff129407",
    "uid_tt_ss": "ddf8b04de63523bdc247e916832f46d6ac9742465baba9672a1f84a8ff129407",
    "sid_tt": "6003413efe9b08b7ec72cda84ccfa3d4",
    "sessionid": "6003413efe9b08b7ec72cda84ccfa3d4",
    "sessionid_ss": "6003413efe9b08b7ec72cda84ccfa3d4",
    "tt_session_tlb_tag": "sttt|5|YANBPv6bCLfscs2oTM-j1P_________KLIgHhgAYNxhEHFz6X0_OdWWaTr7URx-0LSZdGxmjx6A=",
    "store-idc": "alisg",
    "store-country-code": "iq",
    "store-country-code-src": "uid",
    "tt-target-idc": "useast1a",
    "msToken": "K351LW75RnP_oX8FvMyiy-kcCzyfCHXK7gzagqzi2S36O6ook3OAZhc0Z8WrnzeeodL9y5jTjqmCs-PChf7t2ZNNoR8xGq8VPey6cXfhe2KWgAb3OBffJQFYu-9m",
    "passport_csrf_token": "d64c1bc82b8dce810aff1ceb8d54177e",
    "passport_csrf_token_default": "d64c1bc82b8dce810aff1ceb8d54177e",
    "store-country-sign": "MEIEDMPicVTskqK-72UF6gQgtJQQ2Z0iOPpHHP1PSt2Fkegg_U5Sv8Jl4hkurbTEJM8EEBsQnfRNX-we3CIGsbdqOmM"
}

payload = {
  'rules_version': "v2",
  'account_sdk_source': "app",
  'mix_mode': "1",
  'multi_login': "1",
  'type': "3436",
  'email': xor(em),
  'email_theme': "2",
  'use_passport_ticket': "1"
}

m=SignerPy.sign(params=params,cookie=cookies,data=payload)
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2022707020 (Linux; U; Android 11; ar_EG; RMX3263; Build/RP1A.201005.001; Cronet/TTNetVersion:07232c86 2022-12-15 QuicVersion:5f23035d 2022-11-23)",
  'Content-Type': "application/x-www-form-urlencoded",
  'x-tt-passport-csrf-token': "d64c1bc82b8dce810aff1ceb8d54177e",
  'x-tt-multi-sids': "7585693484708201479%3A6003413efe9b08b7ec72cda84ccfa3d4",
  'sdk-version': "2",
  'x-tt-token': "036003413efe9b08b7ec72cda84ccfa3d404d9c7f0d074a0c3d4d7c1c06803fde3237d74ea581ca9c5384b5afe58f1af5d2bf7174974c2d51d8e3b844b7b19972c67814be8e85027375fc228a9687b86608d016b0e8edd28e9e011181304b1f06775e--0a4e0a203f4d0823c755fc4d10b7a67becad30d9c5c5856641c13574567aa3b24b58a1a91220f28cde49501a95f7333098bf9c5a2bc2be4893b77442a83e52860491a51fd4bd1801220674696b746f6b-3.0.1",
  'multi_login': "1",
  'passport-sdk-version': "19",
  'x-ss-req-ticket': "1766769206469",
  'x-bd-kmsv': "0",
  'x-vc-bdturing-sdk-version': "2.2.1.i18n",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-tt-cmpl-token': "AgQYAPOn_hfkT7C5eyKvEzXdPvN6od3_G_-Sp2CiyPM",
  'x-ss-stub': "E40575424774DEBDC28B8B061E1DEF97",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-dp': "1233",
  'x-tt-trace-id': "00-5ba6a66b10691b38ee5084c6104704d1-5ba6a66b10691b38-01",
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'x-khronos': m['x-khronos'],
  'x-ladon': m['x-ladon'],
 
}

response = requests.post(url, params=params, data=payload, headers=headers,cookies=cookies)

print(response.text)






url = "https://aggr32-normal.tiktokv.com/passport/password/change/v2/?device_platform=android&os=android&ssmix=a&_rticket=1766301629062&channel=googleplay&aid=1233&app_name=musical_ly&version_code=430003&version_name=43.0.3&manifest_version_code=2024300030&update_version_code=2024300030&ab_version=43.0.3&resolution=720*1504&dpi=320&device_type=RMX3263&device_brand=realme&language=ar&os_api=30&os_version=11&ac=wifi&is_pad=0&current_region=EG&app_type=normal&sys_region=EG&last_install_time=1766265116&mcc_mnc=60202&timezone_name=Africa%2FCairo&carrier_region_v2=602&residence=EG&app_language=ar&carrier_region=EG&timezone_offset=7200&host_abi=arm64-v8a&locale=ar&ac2=wifi&uoo=0&op_region=EG&build_number=43.0.3&region=EG&ts=1766301629&iid=7585683575648438034&device_id=7573709794557871632&support_webview=1&cronet_version=7db357f9_2025-12-03&ttnet_version=4.2.243.33-tiktok&use_store_region_cookie=1"
pas=input("Enter pass • ")
payload = {
  'password': xor(pas),
  'rule_strategies': "2",
  'mix_mode': "1"
}

headers = {
  'User-Agent': "com.zhiliaoapp.musically/2022707020 (Linux; U; Android 11; ar_EG; RMX3263; Build/RP1A.201005.001; Cronet/TTNetVersion:07232c86 2022-12-15 QuicVersion:5f23035d 2022-11-23)",
  'Content-Type': "application/x-www-form-urlencoded",
  'x-tt-passport-csrf-token': "d64c1bc82b8dce810aff1ceb8d54177e",
  'x-tt-multi-sids': "7585693484708201479%3A6003413efe9b08b7ec72cda84ccfa3d4",
  'sdk-version': "2",
  'x-tt-token': "036003413efe9b08b7ec72cda84ccfa3d404d9c7f0d074a0c3d4d7c1c06803fde3237d74ea581ca9c5384b5afe58f1af5d2bf7174974c2d51d8e3b844b7b19972c67814be8e85027375fc228a9687b86608d016b0e8edd28e9e011181304b1f06775e--0a4e0a203f4d0823c755fc4d10b7a67becad30d9c5c5856641c13574567aa3b24b58a1a91220f28cde49501a95f7333098bf9c5a2bc2be4893b77442a83e52860491a51fd4bd1801220674696b746f6b-3.0.1",
  'multi_login': "1",
  'passport-sdk-version': "19",
  'x-ss-req-ticket': "1766769206469",
  'x-bd-kmsv': "0",
  'x-vc-bdturing-sdk-version': "2.2.1.i18n",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-tt-cmpl-token': "AgQYAPOn_hfkT7C5eyKvEzXdPvN6od3_G_-Sp2CiyPM",
  'x-ss-stub': "E40575424774DEBDC28B8B061E1DEF97",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-ss-dp': "1233",
  'x-tt-trace-id': "00-5ba6a66b10691b38ee5084c6104704d1-5ba6a66b10691b38-01",
  'x-argus': m['x-argus'],
  'x-gorgon': m['x-gorgon'],
  'x-khronos': m['x-khronos'],
  'x-ladon': m['x-ladon'],
 
}

response = requests.post(url, data=payload, headers=headers,cookies={"sessionid": f"{sessionid}"})

print(response.text)